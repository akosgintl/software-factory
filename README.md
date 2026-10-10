# software-factory
Software Factory

A small software factory built from one Claude Code skill, seven subagents, one script, and
markdown files.

    /factory <feature>               run a new job through the loop
    /factory next [N]                run the first N unchecked items in factory/backlog.md
    /factory resume                  pick up jobs an earlier session left in flight
    /factory approve <job-id>        merge a needs-human job into its base branch
    /factory rework <job-id> <note>  send a job back to the builder with feedback

Several jobs run at once: give `/factory` another feature while the first is still going, or
start a batch with `/factory next 3`. Each job is built and reviewed on its own branch
(`factory/<job-id>`) in its own git worktree (`.worktrees/<job-id>/`). They land one at a time:
a job is merged with the base branch and tested again before it is approved, so it is checked
against everything that landed while it was being built. Each job in review runs four reviewers
at once, so three or four jobs is a sensible batch.

The base branch is the one this checkout is on when a job is opened. Leave the checkout on it
while jobs are in flight.

Watch it work:

    cd factory && python3 -m http.server 8000
    # open http://localhost:8000/dashboard.html

The loop lives in `.claude/skills/factory/SKILL.md`, the agents in `.claude/agents/`, and each
job's paper trail in `factory/jobs/<job-id>/`. `factory/board.py` is the one writer of
`factory/board.json`; `python3 factory/board.py show` prints the board in the terminal.
