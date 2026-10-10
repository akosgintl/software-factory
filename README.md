# software-factory

A small, visual software factory for Claude Code: one skill, seven subagents, markdown files. Several jobs run through it at once, each on its own branch in its own git worktree.

```
feature → spec-writer → builder → [security | ux | ui | code] → sync → approver → merge
                           ▲              any CHANGES (max 2 rounds)   ▲
                           └──────────────────────┘    conflicts → one more round
                                                             ESCALATE → needs-human
```

## Run it

```
/factory <feature>               run a new job through the loop
/factory next [N]                run the first N runnable items in factory/backlog.md (default 1)
/factory status                  one line per job
/factory resume                  new session: pick up every unfinished job
/factory approve <job-id>        merge a needs-human job into main
/factory rework <job-id> <note>  send a job back to the builder with feedback
```

The primary checkout must sit on the base branch with a clean tree (outside `factory/`); the orchestrator checks this before starting anything, because that is where merges land.

Dashboard:

```
cd factory && python3 -m http.server 8090     # then open http://localhost:8090/dashboard.html
```

## Parallel jobs

- Each job gets `factory/<job-id>` checked out in `.worktrees/<job-id>`; builders, reviewers and the approver only ever touch that worktree.
- The orchestrator is event-driven: every agent runs in the background, and whichever job's agent finishes next is the job that advances. Up to `MAX_JOBS` (3) are in flight.
- Before approval a job **syncs**: the builder merges the base branch into its branch and re-runs the tests. Conflicts trigger one more review round. Merges happen one at a time.
- Backlog items can declare `· after #n`; `/factory next` only picks items whose dependencies have merged.
- Tests must use ephemeral ports and stay inside their worktree, since neighbouring jobs run tests at the same time.

## Layout

```
.claude/skills/factory/SKILL.md   the orchestrator's instructions (the loop lives here)
.claude/agents/                   one file per agent: spec-writer, builder, reviewer-*, approver
factory/board.json                durable state for every job; the orchestrator is its only writer
factory/dashboard.html            visual board, polls board.json every 2s
factory/backlog.md                numbered queue for /factory next, with `after` dependencies
factory/repo.md                   stack, test command, conventions; refreshed after each merge
factory/jobs/<id>/                request.md, spec.md, build.md, round-N/review-*.md, decision.md
.worktrees/<id>                   the job's checkout of factory/<id> (gitignored)
```

To change the factory, edit `SKILL.md` (loop, settings) or an agent file (what it reads, checks, writes).
