# Repo facts

Read by every agent. The orchestrator rewrites this file after each merge (and at job setup when nothing else is in flight), so it always describes the base branch, never a feature branch.

- **Language / stack:** none yet. The repo holds only `README.md` and the factory itself. The first job picks the stack.
- **Runtimes available:** Python 3.14, Node 26.
- **Test command:** none yet. The first builder must add one and record it in build.md; the orchestrator copies it here after the merge.
- **Conventions:** keep files small with one responsibility each; tests live next to the code they cover; commit messages are imperative one-liners.
- **Parallel jobs:** several jobs build and test in sibling worktrees at once. Servers under test bind ephemeral ports (`PORT=0` or the framework's equivalent), never a fixed one; tests write only under their own worktree; port 8090 belongs to the factory dashboard.
- **Base branch:** `main`. Feature branches are `factory/<job-id>`, each checked out in `.worktrees/<job-id>`.
- **Off limits for agents:** `factory/board.json` (orchestrator only) and any `factory/jobs/*` file that is not the agent's own.
