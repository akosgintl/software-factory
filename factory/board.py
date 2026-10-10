#!/usr/bin/env python3
"""The factory's shared state: the only writer of board.json and of the ticks in backlog.md.

Several jobs move through the factory at once, possibly driven from several Claude sessions.
Every change goes through this script so that it is made under one lock, lands as one atomic
write, and leaves at most one job holding the landing slot (stage `approve`).

    board.py next [N]                  claim the first N unchecked backlog items and print them
    board.py open <slug> <feature>     add a job in stage spec; print its id, paths and base
    board.py set <job-id> key=value..  set stage, title, note, builder or fixes
    board.py round <job-id>            start the next review round; print its number and folder
    board.py verdicts <job-id>         copy this round's verdicts from the review files
    board.py land <job-id> [--wait]    take the landing slot (stage approve), or wait for it
    board.py show [job-id]             print the board, or one job with its paths
"""
import contextlib
import fcntl
import inspect
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

FACTORY = Path(__file__).resolve().parent
ROOT = FACTORY.parent
BOARD, BACKLOG, JOBS = FACTORY / "board.json", FACTORY / "backlog.md", FACTORY / "jobs"
STAGES = ["spec", "build", "review", "approve", "merged", "needs-human"]
REVIEWERS = ["security", "ux", "ui", "code"]
SETTABLE = ["stage", "title", "note", "builder", "fixes"]
POLL_SECONDS, WAIT_SECONDS = 3, 30 * 60


def fail(message, code=1):
    print(f"board.py: {message}", file=sys.stderr)
    sys.exit(code)


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).stdout.strip()


@contextlib.contextmanager
def lock():
    with open(FACTORY / ".lock", "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield


def write(path, text):
    """Replace the file in one step, so the dashboard never reads half of it."""
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(text)
    os.replace(tmp, path)


def load():
    try:
        return json.loads(BOARD.read_text()) if BOARD.exists() else {"jobs": []}
    except ValueError as e:
        fail(f"{BOARD} is not valid JSON ({e}); fix it by hand before going on")


def save(data):
    write(BOARD, json.dumps(data, indent=2) + "\n")


def find(data, job_id):
    for j in data["jobs"]:
        if j["id"] == job_id:
            return j
    fail(f"no job {job_id!r} on the board")


def move(j, stage):
    if j["stage"] != stage:
        j["stage"], j["since"] = stage, datetime.now(timezone.utc).isoformat(timespec="seconds")


def age(j):
    minutes = int((datetime.now(timezone.utc) - datetime.fromisoformat(j["since"])).total_seconds() // 60)
    return f"{minutes // 60}h{minutes % 60:02d}m" if minutes >= 60 else f"{minutes}m"


def paths(j):
    return {"folder": JOBS / j["id"], "worktree": ROOT / ".worktrees" / j["id"]}


def cmd_next(count="1"):
    if not count.isdigit() or int(count) < 1:
        fail("usage: board.py next [N]")
    with lock():
        lines, taken = BACKLOG.read_text().splitlines(keepends=True), []
        for i, line in enumerate(lines):
            m = re.match(r"- \[ \] +(\S.*)", line)   # column 0 only: the indented example is not an item
            if m and len(taken) < int(count):
                lines[i] = line.replace("- [ ]", "- [x]", 1)
                taken.append(m.group(1).strip())
        if not taken:
            fail(f"no unchecked items in {BACKLOG}")
        write(BACKLOG, "".join(lines))
    print("\n".join(taken))


def cmd_open(slug, *feature):
    feature = " ".join(feature).strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")[:40].strip("-")
    if not slug or not feature:
        fail("usage: board.py open <slug> <feature>")
    base = git("branch", "--show-current")
    if not base:
        fail(f"{ROOT} is not on a branch; check out the branch jobs should land on first")
    with lock():
        data = load()
        # Branch names are shared by every checkout of this repo, so they count as taken too.
        used = [j["id"] for j in data["jobs"]] + [p.name for p in JOBS.iterdir()]
        used += [b.split("/", 1)[1] for b in git("branch", "--list", "factory/*", "--format=%(refname:short)").split()]
        number = max((int(m.group(1)) for u in used if (m := re.match(r"(\d+)-", u))), default=0) + 1
        j = {"id": f"{number:03d}-{slug}", "title": feature[:80], "feature": feature, "base": base,
             "branch": f"factory/{number:03d}-{slug}", "stage": "", "round": 0, "fixes": 0,
             "reviews": {}, "builder": "", "note": "writing the spec"}
        move(j, "spec")
        paths(j)["folder"].mkdir(parents=True)
        data["jobs"].append(j)
        save(data)
    show_job(j)


def cmd_set(job_id, *pairs):
    with lock():
        data = load()
        j = find(data, job_id)
        if j["stage"] == "merged":
            fail(f"{job_id} is merged; it cannot change any more")
        for pair in pairs:
            key, sep, value = pair.partition("=")
            if not sep or key not in SETTABLE:
                fail(f"cannot set {pair!r}; expected key=value with key in {', '.join(SETTABLE)}")
            if key == "fixes":
                j[key] = int(value)
            elif key != "stage":
                j[key] = value
            elif value == "approve":
                fail("stage approve is the landing slot; take it with: board.py land <job-id>")
            elif value == "merged" and j["stage"] != "approve":
                fail(f"{job_id} is in stage {j['stage']}; only the job holding the landing slot can be merged")
            elif value not in STAGES:
                fail(f"unknown stage {value!r}; expected one of {', '.join(STAGES)}")
            else:
                move(j, value)
        save(data)


def cmd_round(job_id):
    with lock():
        data = load()
        j = find(data, job_id)
        if j["stage"] in ("approve", "merged"):
            fail(f"{job_id} is in stage {j['stage']}; it cannot start a review round")
        j["round"] += 1
        j["reviews"] = {r: "pending" for r in REVIEWERS}
        j["note"] = f"round {j['round']} in review"
        move(j, "review")
        folder = paths(j)["folder"] / f"round-{j['round']}"
        folder.mkdir(parents=True, exist_ok=True)
        save(data)
    print(j["round"], folder)


def cmd_verdicts(job_id):
    with lock():
        data = load()
        j = find(data, job_id)
        if not j["round"]:
            fail(f"{job_id} has no review round yet")
        shown = {}
        for r in REVIEWERS:
            path = paths(j)["folder"] / f"round-{j['round']}" / f"review-{r}.md"
            first = (path.read_text().splitlines() or [""])[0].strip() if path.exists() else None
            m = re.fullmatch(r"VERDICT:\s*(PASS|CHANGES)", first or "")
            j["reviews"][r] = m.group(1) if m else "pending"
            shown[r] = j["reviews"][r] if m or first is None else f"pending  BAD FIRST LINE {first!r}: respawn this reviewer"
        save(data)
    for r in REVIEWERS:
        print(f"{r:<9}{shown[r]}")
    verdicts = list(j["reviews"].values())
    done = len(verdicts) - verdicts.count("pending")
    result = f"OPEN ({done} of {len(REVIEWERS)} in)" if done < len(REVIEWERS) else "CHANGES" if "CHANGES" in verdicts else "PASS"
    print(f"ROUND {j['round']}: {result}")


def cmd_land(job_id, wait=""):
    if wait not in ("", "--wait"):
        fail("usage: board.py land <job-id> [--wait]")
    deadline = time.monotonic() + WAIT_SECONDS
    while True:
        with lock():
            data = load()
            j = find(data, job_id)
            if j["stage"] not in ("review", "needs-human", "approve"):
                fail(f"{job_id} is in stage {j['stage']}; only a reviewed or needs-human job can land", 3)
            if j["stage"] == "review" and "pending" in j["reviews"].values():
                fail(f"{job_id} still has reviews pending in round {j['round']}; run verdicts first", 3)
            holder = next((o for o in data["jobs"] if o["stage"] == "approve" and o is not j), None)
            if not holder:
                move(j, "approve")
                j["note"] = f"syncing with {j['base']}"
                save(data)
                print(f"{job_id} has the landing slot")
                return
            if j["note"] != (note := f"waiting to land behind {holder['id']}"):
                j["note"] = note
                save(data)
            busy = f"{holder['id']} has held the landing slot for {age(holder)}"
        if not wait:
            fail(f"busy: {busy}")
        if time.monotonic() > deadline:
            fail(f"gave up waiting: {busy}. If its session died, run /factory resume there.", 2)
        time.sleep(POLL_SECONDS)


def show_job(j):
    for key, value in {"id": j["id"], **paths(j), **{k: v for k, v in j.items() if k != "id"}}.items():
        print(f"{key:<9}{value}")


def cmd_show(job_id=None):
    data = load()
    if job_id:
        return show_job(find(data, job_id))
    for j in data["jobs"]:
        reviews = " ".join(f"{r}={v}" for r, v in j["reviews"].items())
        print(f"{j['id']:<34}{j['stage']:<12}{age(j):>6}  round {j['round']}  fixes {j['fixes']}  {reviews}  {j['note']}".rstrip())
    if not data["jobs"]:
        print("no jobs")


if __name__ == "__main__":
    if ROOT.parent.name == ".worktrees":
        fail(f"this is a job worktree's copy; run the one in {ROOT.parent.parent}/factory instead")
    commands = {name[4:]: fn for name, fn in globals().items() if name.startswith("cmd_")}
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        fail("usage:\n" + __doc__.split("\n\n", 2)[2].rstrip(), 2)
    command, args = commands[sys.argv[1]], sys.argv[2:]
    try:
        inspect.signature(command).bind(*args)
    except TypeError:
        fail(f"wrong arguments for {sys.argv[1]}; run board.py with no arguments for usage", 2)
    command(*args)
