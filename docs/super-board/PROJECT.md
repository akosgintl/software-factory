# software-factory

Software Factory — a new project driven by the super-board pipeline. No application code yet; the
first cards on the board define the stack.

| What | Value |
|---|---|
| Repo | github.com/akosgintl/software-factory |
| Board | Software-factory board — github.com/users/akosgintl/projects/2 |
| Base branch | `staging` (cards merge here; promote to `main` by hand) |
| Stack | none yet — record it here once the first card picks one |
| Build / test | none yet — add them to `verify_commands` in `.claude/super-board/configs/software-factory-board.json` |
| Deploy | none detected |

## Layout

| Path | Holds |
|---|---|
| `AGENTS.md` | project rules for every agent (CLAUDE.md imports it) |
| `docs/agents/issue-tracker.md` | ticket format the board expects |
| `.claude/` | super-board skills, scripts, hooks and config |
