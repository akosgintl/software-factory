# software-factory
Software Factory

A small software factory built from one Claude Code skill, seven subagents, and markdown files.

    /factory <feature>               run a new job through the loop
    /factory next                    run the first unchecked item in factory/backlog.md
    /factory approve <job-id>        merge a needs-human job into main
    /factory rework <job-id> <note>  send a job back to the builder with feedback

Watch it work:

    cd factory && python3 -m http.server 8000
    # open http://localhost:8000/dashboard.html

The loop lives in `.claude/skills/factory/SKILL.md`, the agents in `.claude/agents/`, and each
job's paper trail in `factory/jobs/<job-id>/`.
