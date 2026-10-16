# Warp app agent profiles

Agent profiles in the Warp app are set in the UI and synced to your account. No
file can define them. Create these two once, under **Settings → Agents →
Profiles → + Add**, and switch between them with `/profile`.

## Factory

Use it for `/factory-local` and day-to-day work.

| Setting | Value |
|---|---|
| Base model | An explicit Claude model, e.g. Claude Opus (not *Auto*: Auto always bills Warp credits, even with your own key) |
| Apply code diffs | Agent decides |
| Read files | Always allow |
| Execute commands | Agent decides |
| Command allowlist | `git (status\|diff\|log\|show\|branch\|switch\|worktree\|add\|commit\|fetch)(\s.*)?`<br>`gh (issue\|pr\|label\|api\|repo view)(\s.*)?`<br>`python3 (-I )?(scripts\|tools)/.*` |
| Command denylist | Keep the defaults (`wget`, `curl`, `rm`, `eval`, …). Add `git push --force.*` and `git merge.*`. |
| MCP | Allow `github` and `playwright` |
| Run until completion | Off. It bypasses the denylist by default. |

## Review (read-only)

Use it for `review-pr`, `review-pr-local`, `security-review-pr` and `cross-critique`.

| Setting | Value |
|---|---|
| Base model | A different model family from the one that wrote the code, if you have a key for one |
| Apply code diffs | Never |
| Read files | Always allow |
| Execute commands | Always ask |
| MCP | Allow `github` (read) |

## Your own model key (Free plan)

**Settings → AI → API keys** (search "API keys"): add your Anthropic key, then
pick a Claude model per profile. Keys stay on this machine. The Agent CLI keeps
its own copy:

```bash
warp --set-provider-api-key anthropic
```

Even with your key, these always use Warp-provided usage, so they will not run on
Free without purchased usage:
- *Auto* models;
- codebase indexing;
- cloud agents.
