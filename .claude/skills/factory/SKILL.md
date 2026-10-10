---
name: factory
description: Run features through the software factory loop (spec → build → 4 parallel reviews → sync → approve → merge), several jobs at a time. Handles /factory <feature>, /factory next [N], /factory status, /factory resume, /factory approve <job-id>, /factory rework <job-id> <note>.
argument-hint: <feature> | next [N] | status | resume | approve <job-id> | rework <job-id> <note>
---

# /factory — the orchestrator

You are the orchestrator. You run the loop for every in-flight job at once, spawn every agent, and are the **only writer of `factory/board.json`**.
Agents never see this conversation. They get context from files under `factory/jobs/<job-id>/` and each writes only its own file.
Keep your own messages to the user short: one line per stage transition, prefixed with the job id.

## Settings (edit these to change the factory)

| setting | value |
|---|---|
| BASE_BRANCH | `main` |
| MAX_JOBS | `3` — jobs in flight at once (any stage except `merged` / `needs-human`) |
| MAX_ROUNDS | `2` — after this many review rounds the job moves on regardless |
| REVIEWERS | `security` (opus), `ux` (sonnet), `ui` (sonnet), `code` (sonnet) |
| WORKTREES | `.worktrees/<job-id>` (gitignored) |
| DASHBOARD_PORT | `8090` — 8080 stays free for the code under test |

## The loop (per job)

```
feature → spec-writer → builder → [security | ux | ui | code] → WAIT FOR ALL
            any CHANGES and round < MAX_ROUNDS → resume builder → new round
            otherwise → sync: builder merges BASE_BRANCH into the branch
                          conflicts → one more review round
                      → approver → APPROVE: merge to BASE_BRANCH (one job at a time)
                                 → ESCALATE: needs-human (until /factory approve)
```

## Running many jobs at once

Every agent runs in the background and you are woken when one finishes. You never wait on a single job: start a stage, then handle whatever finishes next, for whichever job it belongs to.

- Name every agent `<role>-<id>` in its `description` (`spec-001-health`, `builder-001-health`, `review-security-001-health`, `approver-001-health`). When a completion arrives, the description tells you the job. Run that job's next step, then stop and wait again.
- Jobs advance independently. WAIT FOR ALL is per job: job A's round completing never touches job B.
- Spawn everything that is ready in one message: three spec-writers for three new jobs, four reviewers for one round.
- **Merge and Finish are the only synchronous steps.** Run them from start to end without spawning anything in between, so two merges never overlap. If a second job is also ready to merge, do it right after the first.
- Never have more than MAX_JOBS jobs in flight. Extra backlog items stay unchecked.
- Shared files: `repo.md` is rewritten only in **Finish** after a merge, and in **Setup** when no other job is in flight. `board.json` is read-modify-write on every transition; never cache it between transitions.

## Commands

Parse `$ARGUMENTS`:

| command | action |
|---|---|
| `/factory <feature text>` | new job, run the loop |
| `/factory next [N]` | take up to N (default 1) runnable backlog items, tick them, run them all (see **Backlog**) |
| `/factory status` | print one line per job from board.json (id, stage, round, reviews, note). Spawns nothing. |
| `/factory resume` | new session: pick every unfinished job up where its files say it is (see **Resume**) |
| `/factory approve <job-id>` | job must be `needs-human`; run **Merge**, then **Finish** |
| `/factory rework <job-id> <note>` | run **Rework**, then continue the loop |

### Preflight (every command except `status`)

From the primary checkout: `git symbolic-ref --short HEAD` must equal BASE_BRANCH and `git status --porcelain -- . ':!factory'` must be empty. If either fails, tell the user in one line and stop. A job that cannot merge should not start.

## board.json

```json
{
  "updated": "2026-10-10T17:30:00Z",
  "jobs": [
    {
      "id": "003-rate-limiting",
      "title": "Rate limiting",
      "branch": "factory/003-rate-limiting",
      "worktree": "/abs/path/.worktrees/003-rate-limiting",
      "stage": "review",
      "round": 2,
      "reviews": { "security": "CHANGES", "ux": "PASS", "ui": "pending", "code": "PASS" },
      "history": [ { "security": "CHANGES", "ux": "PASS", "ui": "PASS", "code": "CHANGES" } ],
      "decision": null,
      "note": "",
      "builder": "<agent id, if known>",
      "updated": "2026-10-10T17:30:00Z"
    }
  ]
}
```

- `stage` is one of `spec`, `build`, `review`, `sync`, `approve`, `merged`, `needs-human`.
- `reviews` is the current round; `history` holds every earlier round in order. `round` = `history.length + 1`.
- `decision` is `null`, `"APPROVE"` or `"ESCALATE"`. `note` is a one-liner for the dashboard (why it escalated, rework note, etc.).
- Every board write: read the file, change the job, set both `updated` fields to the current UTC time, write the whole file back. Never let an agent touch it.

## Procedure

### Setup (new job)

1. **Repo facts**: if no other job is in flight, inspect the repo and rewrite `factory/repo.md` (stack, test command, conventions, base branch; look at manifests, CI config, CLAUDE.md, the last build.md). If other jobs are in flight, leave it alone; it was refreshed at the last merge.
2. **Job id**: three-digit number = highest existing `factory/jobs/NNN-*` + 1 (start at `001`), then `-` and a 2–4 word kebab slug. Claim it with `mkdir factory/jobs/<id>`; if that fails because it exists, bump the number and retry. Title = short human name.
3. Write `factory/jobs/<id>/request.md` with the raw feature text (and, for `next`, the backlog line).
4. Branch + worktree from BASE_BRANCH:
   ```
   git worktree add .worktrees/<id> -b factory/<id> <BASE_BRANCH>
   ```
   If git reports `index.lock`, retry once after a second.
5. Add the job to board.json with `stage: "spec"`, `round: 0`, `reviews: {}`, `history: []`, `worktree` = absolute path.
6. Go to **Spec**.

### Backlog (`/factory next [N]`)

Items in `factory/backlog.md` look like `- [ ] #<n> <text>` and may end with `· after #<m>[, #<k>]`.
An item is **runnable** when it is unchecked and every `after` item is ticked **and** its job is `merged` on the board.

1. Walk from the top; collect the first N runnable items, skipping blocked ones. Stop early if MAX_JOBS would be exceeded.
2. Tick each one **before spawning anything**: `- [x] #<n> <text> … → <job-id>`.
3. Run **Setup** for each, then spawn all their spec-writers in one message.
4. If nothing is runnable, say which items are blocked on which jobs and stop.

### Spec

Spawn `spec-writer` (`subagent_type: spec-writer`, `description: spec-<id>`). Prompt, nothing more:
> Job `<id>`. Read `factory/repo.md` and `factory/jobs/<id>/request.md`. Write `factory/jobs/<id>/spec.md`.

When it returns, confirm `spec.md` exists. Board: `stage: "build"`. Go to **Build**.

### Build

Spawn the builder **once per job** (`subagent_type: builder`, `description: builder-<id>`; pass `name: builder-<id>` if the Agent tool accepts it). Prompt:
> Job `<id>`. Worktree `<abs path>/.worktrees/<id>`, branch `factory/<id>`, base `<BASE_BRANCH>`. Read `factory/repo.md` and `factory/jobs/<id>/spec.md`. Build and test in the worktree, commit on the branch, then write `factory/jobs/<id>/build.md`.

Record the returned agent id as `"builder"`. When it returns, confirm `build.md` exists and the branch has commits (`git log <BASE_BRANCH>..factory/<id>`). Go to **Review round**.

### Review round

1. `round = history.length + 1`. Board: `stage: "review"`, `round`, `reviews: {security:"pending", ux:"pending", ui:"pending", code:"pending"}`.
2. Create `factory/jobs/<id>/round-<round>/`.
3. Spawn all four reviewers **in one message** (`subagent_type: reviewer-security|reviewer-ux|reviewer-ui|reviewer-code`, `description: review-<name>-<id>`). Same prompt for each:
   > Job `<id>`, round `<round>`. Worktree `<abs path>`, branch `factory/<id>`, base `<BASE_BRANCH>`. Read `factory/repo.md`, `factory/jobs/<id>/spec.md`, `build.md`, and earlier `round-*/` files. Write `factory/jobs/<id>/round-<round>/review-<name>.md`.
4. As each reviewer returns, read the first line of its file and set `reviews.<name>` to `PASS` or `CHANGES`.
5. **WAIT FOR ALL (this job).** The round is complete only when all four `review-*.md` files exist in the round folder. If a reviewer returned without writing its file, re-spawn that reviewer alone. Never resume this job's builder before its round is complete.
6. Outcome:
   - **All PASS** → **Sync**.
   - **Any CHANGES and `round < MAX_ROUNDS`** → push `reviews` onto `history`, board `stage: "build"`, resume the builder (SendMessage to `builder-<id>` or the recorded id):
     > Round `<round>` reviews are in `factory/jobs/<id>/round-<round>/`. Address every CHANGES item, run the tests, commit on `factory/<id>`, and append a `## Round <round> fixes` section to `build.md`.
     If neither name nor id resolves, spawn a fresh builder (`description: builder-<id>`) with that prompt plus the Build prompt's first line. When it returns, start the next **Review round**.
   - **Any CHANGES and `round == MAX_ROUNDS`** → **Sync** anyway; the approver sees the unresolved reviews.
   - A round started by **Sync** (see below) is always final: when it completes, go to **Approve** whatever the verdicts.

### Sync

The branch was cut from BASE_BRANCH when the job started; other jobs may have merged since.

1. `git merge-base --is-ancestor <BASE_BRANCH> factory/<id>` → exit 0 means nothing to sync: go to **Approve**.
2. Board: `stage: "sync"`. Resume the builder (same resolution as above):
   > `<BASE_BRANCH>` has moved. In the worktree run `git merge <BASE_BRANCH>` into `factory/<id>`, resolve any conflicts, run the tests, commit, and append a `## Sync` section to `build.md`: the list of conflicted files, or the single word `clean`, then a `### Test run`.
3. When it returns, read `## Sync`:
   - `clean` and tests pass → **Approve**.
   - conflicted files listed and tests pass → push `reviews` onto `history` and run one more **Review round** (final).
   - tests fail, or no `## Sync` section → `stage: "needs-human"`, `note: "sync broke tests"`, then **Finish**.

### Approve

Board: `stage: "approve"`. Spawn `approver` (`subagent_type: approver`, `description: approver-<id>`):
> Job `<id>`. Worktree `<abs path>`, branch `factory/<id>`, base `<BASE_BRANCH>`. Read `factory/repo.md` and everything in `factory/jobs/<id>/`. Write `factory/jobs/<id>/decision.md`.

Read the first line of `decision.md`:
- `APPROVE` → board `decision: "APPROVE"`, then **Merge**, then **Finish**.
- `ESCALATE` → board `decision: "ESCALATE"`, `stage: "needs-human"`, `note` = the decision's one-line reason. Then **Finish**. Tell the user: `/factory approve <id>` merges it, `/factory rework <id> <note>` sends it back.

### Merge

**Synchronous**: no spawning from here to the end of Finish. Re-run **Preflight** first.

1. `git merge-base --is-ancestor <BASE_BRANCH> factory/<id>`. If it fails, another job merged since this one synced: go back to **Sync** (once; the second time set `stage: "needs-human"`, `note: "merge conflict"` and **Finish**).
2. From the primary checkout:
   ```
   git merge --no-ff factory/<id> -m "Merge factory/<id>: <title>"
   git worktree remove .worktrees/<id>
   ```
   If the merge conflicts: `git merge --abort`, `stage: "needs-human"`, `note: "merge conflict"`, **Finish**.
3. Board: `stage: "merged"`.

### Finish

1. If the job merged, rewrite `factory/repo.md` now (new stack, test command from build.md, conventions). This is the only time repo.md changes while other jobs are in flight.
2. Commit this job's record on BASE_BRANCH. Add only this job's files plus the shared factory state, never other jobs' half-written folders:
   ```
   git add factory/jobs/<id> factory/board.json factory/backlog.md factory/repo.md
   git commit -m "factory: <id> <stage>"
   ```
3. Report one line: id, stage, round count, dashboard URL.
4. If backlog items became runnable because of this merge, say so in the same line (do not start them unasked).

### Rework (`/factory rework <id> <note>`)

1. Job must not be `merged`. If `.worktrees/<id>` is missing: `git worktree add .worktrees/<id> factory/<id>`.
2. `round = history.length + 1`. Write `factory/jobs/<id>/round-<round>/review-human.md`:
   ```
   VERDICT: CHANGES

   <note>
   ```
3. Board: push `{human: "CHANGES"}` onto `history`, `stage: "build"`, `decision: null`, `note: "<note>"`.
4. Resume `builder-<id>` exactly as in **Review round** step 6 (pointing at `round-<round>/`), then run a fresh **Review round** with all four reviewers and continue the loop (Sync, Approve, …). Rework rounds do not count toward MAX_ROUNDS: treat the human round as round 0 of a new cycle.

### Resume (`/factory resume`)

Agent names and ids never survive a session, so every "resume the builder" becomes "spawn a fresh builder" with the same prompt. Read the board; for each job not `merged` / `needs-human`:

- Worktree missing → `git worktree add .worktrees/<id> factory/<id>`.
- `spec` → `spec.md` exists ? **Build** : **Spec**.
- `build` → `build.md` exists and the branch has commits newer than the last round folder ? **Review round** : spawn the builder (Build prompt; if `history` is non-empty, add the round-fixes prompt pointing at `round-<history.length>/`).
- `review` → all four files in `round-<round>/` ? step 6 : re-spawn only the missing reviewers.
- `sync` → `build.md` has `## Sync` ? Sync step 3 : spawn the builder with the Sync prompt.
- `approve` → `decision.md` exists ? act on it : spawn the approver.

Spawn everything that is ready in one message, then wait.

## Rules (do not relax)

- Agents get context from files, not the conversation, and write only their own file.
- Every review file starts with `VERDICT: PASS` or `VERDICT: CHANGES`; `decision.md` starts with `APPROVE` or `ESCALATE`. If a file violates this, re-spawn that agent once with the format reminder.
- The builder works and commits only in its worktree on `factory/<id>` and never commits `factory/`.
- WAIT FOR ALL per job before acting on a round. Never resume a builder mid-round.
- One named builder per job; resume it with SendMessage for each new round and for Sync.
- Merge + Finish run to completion before you spawn anything else. One merge at a time.
- You never edit code yourself. If something is broken outside the loop, set `needs-human` with a note.

## Dashboard

```
cd factory && python3 -m http.server 8090   →   http://localhost:8090/dashboard.html
```
