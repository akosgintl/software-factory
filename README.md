# software-factory

A small, visual software factory for Claude Code: one skill, seven subagents, markdown files.

```
feature → spec-writer → builder → [security | ux | ui | code] → approver → merge
                           ▲              any CHANGES (max 2 rounds)
                           └──────────────────────┘        ESCALATE → needs-human
```

## Run it

```
/factory <feature>               run a new job through the loop
/factory next                    run the first unchecked item in factory/backlog.md
/factory approve <job-id>        merge a needs-human job into main
/factory rework <job-id> <note>  send a job back to the builder with feedback
```

Dashboard:

```
cd factory && python3 -m http.server 8080     # then open http://localhost:8080/dashboard.html
```

## Layout

```
.claude/skills/factory/SKILL.md   the orchestrator's instructions (the loop lives here)
.claude/agents/                   one file per agent: spec-writer, builder, reviewer-*, approver
factory/board.json                durable state; the orchestrator is its only writer
factory/dashboard.html            visual board, polls board.json every 2s
factory/backlog.md                queue for /factory next
factory/repo.md                   stack, test command, conventions; refreshed per job
factory/jobs/<id>/                request.md, spec.md, build.md, round-N/review-*.md, decision.md
.worktrees/<id>                   builder's checkout of factory/<id> (gitignored)
```

To change the factory, edit `SKILL.md` (loop, settings) or an agent file (what it reads, checks, writes).
