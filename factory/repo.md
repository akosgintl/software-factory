# Repo facts

Read by every agent. The orchestrator rewrites this file at the start of each job.

- **Language / stack:** none yet. The repo holds only `README.md` and the factory itself. The first job picks the stack.
- **Runtimes available:** Python 3.14, Node 26.
- **Test command:** none yet. The first builder must add one and record it here via build.md; the orchestrator copies it into this file.
- **Conventions:** keep files small with one responsibility each; tests live next to the code they cover; commit messages are imperative one-liners.
- **Base branch:** `main`. Feature branches are `factory/<job-id>`.
- **Off limits for agents:** `factory/board.json` (orchestrator only) and any `factory/jobs/*` file that is not the agent's own.
