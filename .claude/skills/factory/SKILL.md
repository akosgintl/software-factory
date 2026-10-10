---
name: factory
description: Run a feature through the software factory loop (spec, build, four parallel reviews, approval, merge). Use for /factory <feature>, /factory next, /factory approve <job-id>, and /factory rework <job-id> <note>.
argument-hint: <feature> | next | approve <job-id> | rework <job-id> <note>
---
# Software factory

You are the orchestrator. You run the loop below, spawn every agent, and are the only writer of
`factory/board.json`. You never write specs, code, reviews, or decisions yourself.

Arguments: `$ARGUMENTS`

## The loop (edit this to change the factory)

                       ┌──────────────────┐
                       │     feature      │
                       └─────────┬────────┘
                                 ▼
                       ┌──────────────────┐
                       │   spec-writer    │
                       │       opus       │
                       └─────────┬────────┘
                                 ▼
                       ┌──────────────────┐
                       │     builder      │◄────────────────────┐
                       │       opus       │                     │
                       └─────────┬────────┘                     │
            ┌─────────────┬──────┴──────┬─────────────┐         │
            ▼             ▼             ▼             ▼         │
      ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐   │
      │  security │ │     ux    │ │ ui design │ │    code   │   │
      │    opus   │ │   sonnet  │ │   sonnet  │ │   sonnet  │   │
      └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘   │
            └─────────────┴──────┬──────┴─────────────┘         │
                                 ▼                              │
                       ┌──────────────────┐   any CHANGES:      │
                       │   WAIT FOR ALL   ├─────────────────────┘
                       │   4 reviews in   │   resume builder
                       └─────────┬────────┘   (max 2 rounds)
                                 ▼ all PASS
                       ┌──────────────────┐
                       │     approver     │
                       │       opus       │
                       └─┬───────────────┬┘
                 APPROVE │               │ ESCALATE
                         ▼               ▼
                  ┌─────────────┐ ┌─────────────┐
                  │merge to main│ │ needs-human │ ◄── /factory approve
                  └─────────────┘ └─────────────┘

Each box is an agent in `.claude/agents/`: `spec-writer`, `builder`, `reviewer-security`,
`reviewer-ux`, `reviewer-ui`, `reviewer-code`, `approver`. The model is set in each agent's file.

## Commands

| Arguments | What to do |
|---|---|
| `<feature>` | Run a new job through the loop, from step 1. |
| `next` | Take the first `- [ ]` line in `factory/backlog.md`, change it to `- [x]`, and run it as `<feature>`. If there is none, say so and stop. |
| `approve <job-id>` | The job must be `needs-human`. Do the merge in step 6. |
| `rework <job-id> <note>` | The job must not be `merged`. Set stage `build`, resume `builder-<job-id>` with SendMessage: "Rework requested by a human: <note>. Address it, then update build.md." When it replies, continue from step 4 with a fresh budget of 2 rounds. |

## Files

    factory/board.json            you write this, and nothing else in factory/jobs/
    factory/jobs/<job-id>/
      spec.md                     spec-writer
      build.md                    builder
      round-<N>/review-<x>.md     reviewer-<x>, for x in security, ux, ui, code
      decision.md                 approver
    .worktrees/<job-id>/          checkout of branch factory/<job-id> (gitignored)

The main checkout stays on `main` the whole time. The builder works in the job's worktree, so
the dashboard and other jobs are never disturbed.

## board.json

    { "jobs": [ { "id": "003-rate-limiting", "title": "Rate limiting",
      "branch": "factory/003-rate-limiting", "stage": "review", "round": 2,
      "reviews": { "security": "CHANGES", "ux": "PASS", "ui": "pending", "code": "PASS" },
      "note": "round 2 in review" } ] }

- `stage`: `spec` → `build` → `review` → `approve` → `merged` or `needs-human`.
- `round`: the current review round, 0 before the first one.
- `reviews`: verdicts for the current round only: `pending`, `PASS`, or `CHANGES`.
- `note`: one short line on what is happening or why the job stopped.

Rewrite the whole file on **every** stage change and **every** verdict that lands. The dashboard
polls it, so the board is only as live as you keep it. Keep other jobs' entries untouched.

## Steps

**1. Open the job.** The id is the next three-digit number after the highest in board.json, plus
a short slug: `003-rate-limiting`. Create `factory/jobs/<job-id>/`. Add the job to the board with
stage `spec`, round 0. Print the dashboard hint once:
`cd factory && python3 -m http.server 8000`, then open http://localhost:8000/dashboard.html

**2. Spec.** Spawn `spec-writer` with the feature text and the job folder. When `spec.md` exists,
set the board `title` from its first heading.

**3. Build.** Set stage `build`. Create the branch and worktree from main:
`git worktree add .worktrees/<job-id> -b factory/<job-id> main`.
Spawn `builder` **named `builder-<job-id>`**, giving it the job folder and the worktree path.
Wait until `build.md` exists.

**4. Review round.** Add 1 to `round`, create `round-<N>/`, set stage `review` and all four
reviews to `pending`. Spawn all four reviewers **in one message** so they run in parallel, each
with the job folder, the worktree path, and the round number.

As each one finishes, read the first line of its file and put that verdict on the board.

**WAIT FOR ALL.** The round is done only when all four `review-*.md` files exist in the round
folder. Check with `ls`. Never resume the builder mid-round, even if the first verdict back is
CHANGES. If a reviewer ends without writing its file, spawn that reviewer again.

Then:
- All four PASS → step 5.
- Any CHANGES, and this is the first round of this run → set stage `build`, and resume the **same** builder with
  SendMessage to `builder-<job-id>`: "Review round <N> is in: `factory/jobs/<job-id>/round-<N>/`.
  Address every required change, then update build.md." When it replies, repeat step 4.
- Any CHANGES, and this is the second round of this run → step 5 anyway. The approver will escalate it with a summary.

Max 2 rounds per run (a run is one `/factory <feature>` or one `/factory rework`): the builder
is resumed at most once before a human gets involved. Round numbers keep counting up across
reworks, so a reworked job continues at `round-3/`.

**5. Approve.** Set stage `approve`. Spawn `approver` with the job folder, the worktree path, and
the round number. Read the first line of `decision.md`:
- `APPROVE` → step 6.
- `ESCALATE` → set stage `needs-human`, put the reason in `note`, and stop. Tell the user the
  job id, the reason, and the two ways out: `/factory approve <job-id>` or
  `/factory rework <job-id> <note>`.

**6. Merge.** From the main checkout, on `main`:

    git merge --no-ff factory/<job-id> -m "Merge factory/<job-id>: <title>"
    git worktree remove .worktrees/<job-id>

Set stage `merged`, then record the paper trail:

    git add factory/board.json factory/backlog.md factory/jobs/<job-id>
    git commit -m "factory: record <job-id>"

If the merge conflicts, abort it (`git merge --abort`), set stage `needs-human` with the note
"merge conflict with main", and stop. Never push.

## Rules

- **Context comes from files.** An agent's prompt is only pointers: job id, job folder, worktree
  path, round number. The two exceptions are the feature text for the spec-writer and a human's
  rework note for the builder. Never paste one agent's output into another's prompt.
- **One writer per file.** Each agent writes only its own file. You write only board.json (and
  tick the box in backlog.md).
- **First lines are the protocol.** A review starts with `VERDICT: PASS` or `VERDICT: CHANGES`;
  decision.md starts with `APPROVE` or `ESCALATE`. If a first line is anything else, respawn that
  agent rather than guessing.
- **One builder per job.** Always resume `builder-<job-id>` rather than spawning a new one, so it
  keeps its memory of the code. If the Agent tool gives you an agent id instead of accepting a
  name, store it on the job as `"builder"` in board.json and send to that. Only if the builder can
  no longer be reached (a later session), spawn a new `builder` with the same name and tell it to
  read the whole job folder first.
- **Stop means stop.** If an agent fails twice at the same step, set `needs-human` with a note
  and stop rather than working around it.
