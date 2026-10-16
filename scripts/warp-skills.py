#!/usr/bin/env python3
"""Manage the vendored Warp skill packs.

Skills live grouped by source under vendor/warp-skills/<source>/<skill>/.
Warp only discovers skills one level below a provider directory, so the
enabled ones are exposed as relative symlinks in .agents/skills/<skill>.
vendor/warp-skills/skills.toml says where each source came from and which
skills are disabled. Real directories in .agents/skills are local skills and
are never touched.

  warp-skills.py list                  every skill, its source and state
  warp-skills.py enable  <skill>...    remove from the source's disabled list, sync
  warp-skills.py disable <skill>...    add to the source's disabled list, sync
  warp-skills.py sync                  rebuild .agents/skills from the manifest
  warp-skills.py check                 frontmatter, name clashes, broken links
  warp-skills.py update <source> [ref] re-vendor a source from GitHub, then review the diff
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "vendor" / "warp-skills"
MANIFEST = VENDOR / "skills.toml"
SKILLS = ROOT / ".agents" / "skills"
COPY_MARKER = ".warp-skills-copy"
SHARED_DIR = "_shared"


def load():
    with MANIFEST.open("rb") as f:
        return tomllib.load(f)


def mode(manifest):
    return manifest.get("settings", {}).get("mode", "symlink")


def vendored(manifest):
    """Yield (source, skill, path) for every vendored skill."""
    for source in manifest["sources"]:
        base = VENDOR / source
        for d in sorted(base.iterdir()) if base.is_dir() else []:
            if d.is_dir() and (d / "SKILL.md").is_file():
                yield source, d.name, d


def frontmatter(skill_md):
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[k.strip()] = v.strip().strip("'\"")
    return fields


def is_managed(entry):
    """A symlink into the vendor tree, or a copy made by --copy mode."""
    if entry.is_symlink():
        target = (entry.parent / os.readlink(entry)).resolve()
        return VENDOR.resolve() in target.parents
    return entry.is_dir() and (entry / COPY_MARKER).exists()


def remove(entry):
    if entry.is_symlink():
        entry.unlink()
    else:
        shutil.rmtree(entry)


def place(src, dest, how):
    if how == "copy":
        shutil.copytree(src, dest, symlinks=False)
        (dest / COPY_MARKER).write_text(f"copied from {src.relative_to(ROOT)}\n")
    else:
        dest.symlink_to(os.path.relpath(src, dest.parent), target_is_directory=True)


def link_ok(entry, src, how):
    if how == "copy":
        return entry.is_dir() and not entry.is_symlink() and (entry / COPY_MARKER).exists()
    return entry.is_symlink() and os.readlink(entry) == os.path.relpath(src, entry.parent)


def sync(manifest):
    how = mode(manifest)
    SKILLS.mkdir(parents=True, exist_ok=True)
    wanted = {}
    for source, name, path in vendored(manifest):
        if name not in manifest["sources"][source].get("disabled", []):
            if name in wanted:
                sys.exit(f"error: skill '{name}' is enabled in both {wanted[name][0]} and {source}")
            wanted[name] = (source, path)

    for entry in sorted(SKILLS.iterdir()):
        if not is_managed(entry):
            if entry.name in wanted:
                sys.exit(f"error: .agents/skills/{entry.name} is a local skill and clashes with {wanted[entry.name][0]}")
            continue
        src = wanted.get(entry.name, (None, None))[1]
        if src is None or not link_ok(entry, src, how):
            remove(entry)

    added = 0
    for name, (source, path) in wanted.items():
        dest = SKILLS / name
        if not dest.exists() and not dest.is_symlink():
            place(path, dest, how)
            added += 1

    # Trees the skills reference by repo-relative path, e.g. .agents/shared/scripts.
    for source, cfg in manifest["sources"].items():
        if "shared" in cfg:
            dest = ROOT / cfg["shared"]
            src = VENDOR / source / SHARED_DIR
            if (dest.exists() or dest.is_symlink()) and not link_ok(dest, src, "symlink"):
                if not dest.is_symlink():
                    sys.exit(f"error: {cfg['shared']} exists and is not a managed link")
                dest.unlink()
            if not dest.is_symlink():
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.symlink_to(os.path.relpath(src, dest.parent), target_is_directory=True)

    print(f"synced .agents/skills ({how}): {len(wanted)} vendored skills enabled, {added} added")


def cmd_list(manifest, _args):
    rows = []
    for source, name, _ in vendored(manifest):
        cfg = manifest["sources"][source]
        state = "off" if name in cfg.get("disabled", []) else "on"
        rows.append((name, source, state, cfg.get("notes", {}).get(name, "")))
    for entry in sorted(SKILLS.iterdir()) if SKILLS.is_dir() else []:
        if not is_managed(entry) and (entry / "SKILL.md").is_file():
            rows.append((entry.name, "local", "on", ""))
    width = max(len(r[0]) for r in rows)
    swidth = max(len(r[1]) for r in rows)
    for name, source, state, note in rows:
        print(f"{name:<{width}}  {source:<{swidth}}  {state:<3}  {note}".rstrip())
    on = sum(r[2] == "on" for r in rows)
    print(f"\n{on} on, {len(rows) - on} off")


def set_disabled(source, names):
    """Rewrite one source's `disabled = [...]` line, keeping the rest of the file."""
    text = MANIFEST.read_text(encoding="utf-8")
    section = re.search(rf"^\[sources\.{re.escape(source)}\]\n(.*?)(?=^\[|\Z)", text, re.S | re.M)
    line = re.search(r"^disabled\s*=.*$", section.group(1), re.M)
    new = "disabled = [" + ", ".join(f'"{n}"' for n in sorted(names)) + "]"
    start = section.start(1) + line.start()
    end = section.start(1) + line.end()
    MANIFEST.write_text(text[:start] + new + text[end:], encoding="utf-8")


def toggle(manifest, args, enable):
    owners = {}
    for source, name, _ in vendored(manifest):
        owners.setdefault(name, []).append(source)
    for name in args.skills:
        if name not in owners:
            sys.exit(f"error: no vendored skill named '{name}'")
        for source in owners[name]:
            disabled = set(manifest["sources"][source].get("disabled", []))
            disabled = disabled - {name} if enable else disabled | {name}
            manifest["sources"][source]["disabled"] = sorted(disabled)
            set_disabled(source, disabled)
    sync(load())


def cmd_check(manifest, _args):
    problems = []
    names = {}
    for source, name, path in vendored(manifest):
        fm = frontmatter(path / "SKILL.md")
        if not fm.get("name") or not fm.get("description"):
            problems.append(f"{source}/{name}: frontmatter needs name and description")
        elif fm["name"] != name:
            print(f"note: {source}/{name}: frontmatter name is '{fm['name']}'")
        if name not in manifest["sources"][source].get("disabled", []):
            names.setdefault(fm.get("name", name), []).append(f"{source}/{name}")
    for entry in sorted(SKILLS.iterdir()) if SKILLS.is_dir() else []:
        if entry.is_symlink() and not entry.exists():
            problems.append(f".agents/skills/{entry.name}: broken symlink")
        elif not is_managed(entry):
            fm = frontmatter(entry / "SKILL.md") if (entry / "SKILL.md").is_file() else {}
            if not fm.get("name") or not fm.get("description"):
                problems.append(f".agents/skills/{entry.name}: frontmatter needs name and description")
            names.setdefault(fm.get("name", entry.name), []).append(f"local/{entry.name}")
    for skill_name, where in names.items():
        if len(where) > 1:
            problems.append(f"skill name '{skill_name}' is enabled more than once: {', '.join(where)}")
    for p in problems:
        print(f"problem: {p}")
    if problems:
        sys.exit(1)
    print("ok")


def cmd_update(manifest, args):
    cfg = manifest["sources"].get(args.source)
    if cfg is None:
        sys.exit(f"error: unknown source '{args.source}'")
    with tempfile.TemporaryDirectory(prefix="warp-skills-") as tmp:
        clone = Path(tmp) / "repo"
        url = f"https://github.com/{cfg['repo']}.git"
        subprocess.run(["git", "clone", "--quiet", url, str(clone)], check=True)
        if args.ref:
            subprocess.run(["git", "-C", str(clone), "checkout", "--quiet", args.ref], check=True)
        sha = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"],
                             check=True, capture_output=True, text=True).stdout.strip()
        dest = VENDOR / args.source
        shutil.rmtree(dest)
        shutil.copytree(clone / cfg["path"], dest, symlinks=False)
        shutil.copy2(clone / "LICENSE", dest / "LICENSE")
        if "shared" in cfg:
            shutil.copytree(clone / cfg["shared"], dest / SHARED_DIR, symlinks=False)
    text = MANIFEST.read_text(encoding="utf-8")
    text = re.sub(rf'(^\[sources\.{re.escape(args.source)}\]\n(?:(?!^\[).*\n)*?^sha\s*=\s*)"[0-9a-f]*"',
                  rf'\g<1>"{sha}"', text, count=1, flags=re.M)
    MANIFEST.write_text(text, encoding="utf-8")
    print(f"{args.source} vendored at {sha}. Review before committing:")
    print(f"  git diff --stat -- {dest.relative_to(ROOT)}")
    sync(load())


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("check")
    sync_p = sub.add_parser("sync")
    sync_p.add_argument("--copy", action="store_true", help="copy instead of symlink (if Warp ignores symlinks)")
    sync_p.add_argument("--symlink", action="store_true", help="switch back to symlinks")
    for name in ("enable", "disable"):
        sub.add_parser(name).add_argument("skills", nargs="+")
    up = sub.add_parser("update")
    up.add_argument("source")
    up.add_argument("ref", nargs="?")
    args = p.parse_args()

    manifest = load()
    if args.cmd == "list":
        cmd_list(manifest, args)
    elif args.cmd == "check":
        cmd_check(manifest, args)
    elif args.cmd == "sync":
        if args.copy or args.symlink:
            new = "copy" if args.copy else "symlink"
            text = MANIFEST.read_text(encoding="utf-8")
            MANIFEST.write_text(re.sub(r'^mode\s*=\s*"\w+"', f'mode = "{new}"', text, count=1, flags=re.M),
                                encoding="utf-8")
            manifest = load()
        sync(manifest)
    elif args.cmd in ("enable", "disable"):
        toggle(manifest, args, args.cmd == "enable")
    elif args.cmd == "update":
        cmd_update(manifest, args)


if __name__ == "__main__":
    main()
