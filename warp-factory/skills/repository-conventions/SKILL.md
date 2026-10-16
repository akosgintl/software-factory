---
name: repository-conventions
description: Shared conventions for branches, commits, checks, and PRs in akosgintl/software-factory. Use before creating branches, commits, or pull requests.
---

# Repository conventions

Every agent in the factory can read this skill.

- Base branch: `warpdotdev-factory` while this factory is an experiment. Never
  target `main`, `staging`, or another experiment's branch.
- Branches: `factory/<work-item-id>-<slug>`, one git worktree each under
  `.worktrees/<work-item-id>-<slug>/`.
- Commits: imperative subject line; reference the issue as `#<n>`. Never
  rewrite pushed history.
- Checks: run the checks in `AGENTS.md` that cover the files you touched, and
  state each command and its result in the PR description.
- PRs: open as draft, carry the `factory:SoftwareFactory` label, link the
  issue, describe what changed and how it was verified. A human merges.
- Do not edit `vendor/`: it is copied from upstream repos. Change which skills
  are enabled with `scripts/warp-skills.py`, not by touching `.agents/skills`.
