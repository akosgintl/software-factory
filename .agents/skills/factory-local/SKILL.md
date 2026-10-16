---
name: factory-local
description: Run a request through this repo's Warp factory (warp-factory/) on the local machine instead of Warp's cloud. Use when the user invokes /factory-local, or asks to run, triage, spec, implement, or review work "through the factory" locally.
---

# Factory, run locally

`warp-factory/` is a Warp Factory definition: a foreman plus triage, spec,
implementer, reviewer, and mobile-build agents. In Warp's cloud the platform
dispatches those agents, runs them on runners, and fires the automations. On the
Free plan we run the same agents here: you are the foreman, and the other
agents run as local child agents.

The request is: $ARGUMENTS

## Before you start

1. Read `warp-factory/agents/foreman/agent.md`. Its body (after the closing
   `---`) is your procedure, communication rules, and human gates. Follow it,
   with the local translations below.
2. Read `warp-factory/skills/repository-conventions/SKILL.md` and `AGENTS.md`.
3. Pick a run id `<YYYYMMDD-HHMM>-<slug>` and start the run log
   `warp-factory/local-runs/<run-id>.md` with the request verbatim. Append one
   line per stage: what was dispatched, to which agent, and the outcome.

## Dispatching an agent

Each factory agent is `warp-factory/agents/<name>/agent.md`. Start it as a
local child agent (Warp's local-to-local orchestration). The child's prompt is:

```
You are the <name> agent of this repo's software factory, running locally.
Read warp-factory/agents/<name>/agent.md and follow its body as your
instructions. Also read warp-factory/skills/repository-conventions/SKILL.md
and every skill under warp-factory/agents/<name>/skills/.
Report to the orchestrator (the parent conversation), never to the user.
Local rules: <the "Local translations" section of this skill>.
Brief: <the brief the foreman procedure says this stage needs>
```

- Give the implementer its own worktree. Before you dispatch it, run
  `git worktree add .worktrees/<run-id> -b factory/<run-id> <base>` from the
  repo root, where `<base>` is the branch the user is on, and tell the child to
  work only inside `.worktrees/<run-id>`.
- Send follow-ups (review findings, the user's answers, spec feedback) to the
  child that already has the context, as the foreman prompt says. Do not
  start a new child for the same stage.
- If you cannot start child agents in this session, run each stage yourself,
  in order, in a clearly separated step: re-read that agent's `agent.md`
  first, do only that stage's job, and write its report into the run log
  before you continue. Say once, at the start, that the stages run in one
  conversation.

## Local translations

| Factory concept | Locally |
|---|---|
| Automations (`warp-factory/automations/`) | Disabled. The user's message is the trigger. Skip the addressing check. |
| Slack thread, Linear issue | This conversation. Do not post to Slack or Linear. |
| Tracker / work item | A GitHub issue in `akosgintl/software-factory`, created with `gh issue create` when triage decides the work needs tracking. |
| Routing label `factory:<alias>` | `factory:SoftwareFactory`. Create it once with `gh label create factory:SoftwareFactory` if it is missing. |
| Runners (`warp-factory/runners/`) | This machine. |
| `mobile-build` (macOS runner) | Not available locally, and no iOS repo is attached. If the work needs it, stop and tell the user. |
| `complete_task` / task completion | Mark the run log `DONE` and close the issue when the user says the PR merged. |
| Scorers (`warp-factory/scorers/`) | Not run automatically. If the user asks, apply a scorer's rubric to the run log and quote the label. |

## Human gates (unchanged)

- Spec approval before implementation, when a spec was written.
- Questions go to the user through you, and you wait for the answer.
- PR hand-off: open the PR as a draft with `gh pr create --draft`, give the
  user the link, and stop.
- Never merge. Never push to `main`, `staging`, `warpdotdev-factory`, or
  another experiment's branch. Push only the `factory/<run-id>` branch, and
  only to open the PR.
