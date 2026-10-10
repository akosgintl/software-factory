---
name: factory
description: Run a feature through the software factory loop (spec → build → 4 parallel reviews → approve → merge). Handles /factory <feature>, /factory next, /factory approve <job-id>, /factory rework <job-id> <note>.
argument-hint: <feature> | next | approve <job-id> | rework <job-id> <note>
---

# /factory — the orchestrator

You are the orchestrator. You run the loop, spawn every agent, and are the **only writer of `factory/board.json`**.
Agents never see this conversation. They get context from files under `factory/jobs/<job-id>/` and each writes only its own file.
Keep your own messages to the user short: one line per stage transition.

## Settings (edit these to change the factory)

| setting | value |
|---|---|
| BASE_BRANCH | `main` |
| MAX_ROUNDS | `2` — after this many review rounds the approver decides regardless |
| REVIEWERS | `security` (opus), `ux` (sonnet), `ui` (sonnet), `code` (sonnet) |
| WORKTREES | `.worktrees/<job-id>` (gitignored) |

## The loop

```
feature → spec-writer → builder → [security | ux | ui | code] → WAIT FOR ALL
            any CHANGES and round < MAX_ROUNDS → resume builder → new round
            otherwise → approver → APPROVE: merge to BASE_BRANCH
                                 → ESCALATE: needs-human (until /factory approve)
```

## Commands

Parse `$ARGUMENTS`:

| command | action |
|---|---|
| `/factory <feature text>` | new job, run the full loop |
| `/factory next` | take the first `- [ ]` line in `factory/backlog.md`, tick it to `- [x] … → <job-id>`, run the full loop |
| `/factory approve <job-id>` | job must be `needs-human`; run **Merge**, then **Finish** |
| `/factory rework <job-id> <note>` | run **Rework**, then continue from **Review round** |

## board.json

```json
{
  "updated": "2026-10-10T17:30:00Z",
  "jobs": [
    {
      "id": "003-rate-limiting",
      "title": "Rate limiting",
      "branch": "factory/003-rate-limiting",
      "stage": "review",
      "round": 2,
      "reviews": { "security": "CHANGES", "ux": "PASS", "ui": "pending", "code": "PASS" },
      "history": [ { "security": "CHANGES", "ux": "PASS", "ui": "PASS", "code": "CHANGES" } ],
      "decision": null,
      "note": "",
      "updated": "2026-10-10T17:30:00Z"
    }
  ]
}
```

- `stage` is one of `spec`, `build`, `review`, `approve`, `merged`, `needs-human`.
- `reviews` is the current round; `history` holds every earlier round in order. `round` = `history.length + 1`.
- `decision` is `null`, `"APPROVE"` or `"ESCALATE"`. `note` is a one-liner for the dashboard (why it escalated, rework note, etc.).
- Every board write: read the file, change the job, set both `updated` fields to the current UTC time, write the whole file back. Never let an agent touch it.

## Procedure

### Setup (new job)

1. **Inspect the repo** and rewrite `factory/repo.md`: language/stack, test command, conventions, base branch. Look at manifests (`package.json`, `pyproject.toml`, …), CI config, CLAUDE.md, and the last build.md if any. If the repo is empty, say so and list the available runtimes.
2. **Job id**: three-digit number = highest existing `factory/jobs/NNN-*` + 1 (start at `001`), then `-` and a 2–4 word kebab slug of the feature. Title = short human name.
3. Create `factory/jobs/<id>/` and write `request.md` containing the raw feature text (and, for `next`, the backlog line).
4. Branch + worktree from BASE_BRANCH:
   ```
   git worktree add .worktrees/<id> -b factory/<id> <BASE_BRANCH>
   ```
5. Add the job to board.json with `stage: "spec"`, `round: 0`, `reviews: {}`, `history: []`.

### Spec

Spawn `spec-writer` (Agent tool, `subagent_type: spec-writer`). Prompt, nothing more:
> Job `<id>`. Read `factory/repo.md` and `factory/jobs/<id>/request.md`. Write `factory/jobs/<id>/spec.md`.

When it returns, confirm `spec.md` exists. Board: `stage: "build"`.

### Build

Spawn the builder **once per job**, named `builder-<id>` (`subagent_type: builder`, `description: builder-<id>`; pass `name: builder-<id>` if the Agent tool accepts it). Prompt:
> Job `<id>`. Worktree `<abs path>/.worktrees/<id>`, branch `factory/<id>`, base `<BASE_BRANCH>`. Read `factory/repo.md` and `factory/jobs/<id>/spec.md`. Build and test in the worktree, commit on the branch, then write `factory/jobs/<id>/build.md`.

Record the returned agent id in the job as `"builder": "<agentId>"`. When it returns, confirm `build.md` exists and the branch has commits (`git log <BASE_BRANCH>..factory/<id>`). If the test command in build.md differs from repo.md, update repo.md.

### Review round

1. `round = history.length + 1`. Board: `stage: "review"`, `round`, `reviews: {security:"pending", ux:"pending", ui:"pending", code:"pending"}`.
2. Create `factory/jobs/<id>/round-<round>/`.
3. Spawn all four reviewers **in one message** (`subagent_type: reviewer-security`, `reviewer-ux`, `reviewer-ui`, `reviewer-code`). Same prompt for each:
   > Job `<id>`, round `<round>`. Worktree `<abs path>`, branch `factory/<id>`, base `<BASE_BRANCH>`. Read `factory/repo.md`, `factory/jobs/<id>/spec.md`, `build.md`, and earlier `round-*/` files. Write `factory/jobs/<id>/round-<round>/review-<name>.md`.
4. As each reviewer returns, read the first line of its file and set `reviews.<name>` to `PASS` or `CHANGES` on the board.
5. **WAIT FOR ALL.** The round is complete only when all four `review-*.md` files exist in the round folder. If a reviewer returned without writing its file, re-spawn that reviewer alone. Never resume the builder before the round is complete.
6. Outcome:
   - **All PASS** → **Approve**.
   - **Any CHANGES and `round < MAX_ROUNDS`** → push `reviews` onto `history`, board `stage: "build"`, then resume the builder with SendMessage to `builder-<id>` (or the recorded agent id):
     > Round `<round>` reviews are in `factory/jobs/<id>/round-<round>/`. Address every CHANGES item, run the tests, commit on `factory/<id>`, and append a `## Round <round> fixes` section to `build.md`.
     If neither name nor id resolves (new session), spawn a fresh builder named `builder-<id>` with that prompt plus the Build prompt's first line. When it returns, start the next **Review round**.
   - **Any CHANGES and `round == MAX_ROUNDS`** → **Approve** anyway; the approver sees the unresolved reviews.

### Approve

Board: `stage: "approve"`. Spawn `approver` (`subagent_type: approver`):
> Job `<id>`. Worktree `<abs path>`, branch `factory/<id>`, base `<BASE_BRANCH>`. Read `factory/repo.md` and everything in `factory/jobs/<id>/`. Write `factory/jobs/<id>/decision.md`.

Read the first line of `decision.md`:
- `APPROVE` → board `decision: "APPROVE"`, then **Merge**, then **Finish**.
- `ESCALATE` → board `decision: "ESCALATE"`, `stage: "needs-human"`, `note` = the decision's one-line reason. Then **Finish**. Tell the user: `/factory approve <id>` merges it, `/factory rework <id> <note>` sends it back.

### Merge

From the main checkout (on BASE_BRANCH, clean tree):
```
git merge --no-ff factory/<id> -m "Merge factory/<id>: <title>"
git worktree remove .worktrees/<id>
```
Board: `stage: "merged"`. If the merge conflicts, abort it (`git merge --abort`), set `stage: "needs-human"` and `note: "merge conflict"`, and stop.

### Finish

Commit the job's factory files on BASE_BRANCH so the record travels with the code:
```
git add factory && git commit -m "factory: <id> <stage>"
```
Report one line to the user: id, stage, round count, and the dashboard path.

### Rework (`/factory rework <id> <note>`)

1. Job must not be `merged`. If `.worktrees/<id>` is missing: `git worktree add .worktrees/<id> factory/<id>`.
2. `round = history.length + 1`. Write `factory/jobs/<id>/round-<round>/review-human.md`:
   ```
   VERDICT: CHANGES

   <note>
   ```
3. Board: push `{human: "CHANGES"}` onto `history`, `stage: "build"`, `decision: null`, `note: "<note>"`.
4. Resume `builder-<id>` exactly as in **Review round** step 6 (pointing at `round-<round>/`), then run a fresh **Review round** with all four reviewers, and continue the loop. Rework rounds do not count toward MAX_ROUNDS; reset the count by treating the human round as round 0 of a new cycle.

## Rules (do not relax)

- Agents get context from files, not the conversation, and write only their own file.
- Every review file starts with `VERDICT: PASS` or `VERDICT: CHANGES`; `decision.md` starts with `APPROVE` or `ESCALATE`. If a file violates this, re-spawn that agent once with the format reminder.
- The builder works and commits only in its worktree on `factory/<id>` and never commits `factory/`.
- WAIT FOR ALL before acting on a round. Never resume the builder mid-round.
- One named builder per job; resume it with SendMessage for each new round.
- You never edit code yourself. If something is broken outside the loop, set `needs-human` with a note.

## Dashboard

```
cd factory && python3 -m http.server 8080   →   http://localhost:8080/dashboard.html
```
