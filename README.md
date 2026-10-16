# software-factory · warpdotdev-factory

This branch is the fourth software-factory experiment in this repo. It installs
**Warp's own factory tooling**, set up for the **Free plan** with your own
Anthropic API key and no cloud sandboxes:

- the official Factory definition (issue → triage → spec → implement → review → human merge);
- every public Warp skill pack;
- workflows and MCP config;
- the Warp app, the Agent CLI and the Oz CLI.

The other experiments are on `staging` (super-board), `fable-factory` and
`opus-factory`. The comparison is in `knowledge/experiments.md` on the
`knowledge` branch.

## What is here

| Path | Contents | Source |
|---|---|---|
| [`warp-factory/`](warp-factory/) | Factory as code: 6 agents, 5 automations (all off), 3 runners, 2 scorers, 2 skills | [`warp-factory-examples/02-sdlc-issue-to-pr`](https://github.com/warpdotdev/warp-factory-examples/tree/84e7c952f1506c4bd2784d96fd40a6f4d6398cad/examples/02-sdlc-issue-to-pr) (MIT) |
| [`.agents/skills/factory-local/`](.agents/skills/factory-local/SKILL.md) | `/factory-local`: runs `warp-factory/` on this machine | ours |
| [`vendor/warp-skills/common-skills/`](vendor/warp-skills/common-skills/) | 28 skills: PRs, specs, review, CI, merge conflicts, research, skill tooling | [`warpdotdev/common-skills`](https://github.com/warpdotdev/common-skills) (MIT) |
| [`vendor/warp-skills/oz-skills/`](vendor/warp-skills/oz-skills/) | 15 skills: CI fix, web testing/audits, MCP builder, issue triage | [`warpdotdev/oz-skills`](https://github.com/warpdotdev/oz-skills) (MIT; 2 Apache-2.0) |
| [`vendor/warp-skills/oz-for-oss/`](vendor/warp-skills/oz-for-oss/) | 18 skills: issue triage, specs, implement-issue, PR and security review | [`warpdotdev/oz-for-oss`](https://github.com/warpdotdev/oz-for-oss) (MIT) |
| [`vendor/warp-drive/do-things/`](vendor/warp-drive/do-things/IMPORT.md) | 35 community Warp Drive objects, imported by hand | [`warpdotdev/do-things`](https://github.com/warpdotdev/do-things) (MIT) |
| [`.warp/workflows/`](.warp/workflows/) | Workflow palette: run the factory, one agent, validate, worktree, skills | ours |
| [`.warp/.mcp.json`](.warp/.mcp.json) | Project MCP servers: GitHub (OAuth), Playwright | ours |
| [`AGENTS.md`](AGENTS.md) | Project rules Warp gives every agent | ours |
| [`warp/`](warp/) | Tab config, Agent CLI profiles, app profile guide | ours |
| [`scripts/warp-setup.sh`](scripts/warp-setup.sh) | Machine setup (Linux/WSL2) | ours |
| [`scripts/warp-skills.py`](scripts/warp-skills.py) | Skill pack manager | ours |
| [`tools/warp/validate_factory_files.py`](tools/warp/validate_factory_files.py) | Warp's factory validator | `warp-factory-examples` (MIT) |

Installed outside the repo, by `scripts/warp-setup.sh`:

- **In `~/.agents/skills/`:** `factory-setup` (`warpdotdev/warp-factories-skills`) and `oz` (`warpdotdev/oz-agent-skill`). These repos have no license, so they are not committed here.
- **Warp notification plugins** for the CLI agents on this machine: `warp@claude-code-warp`, `warp@codex-warp`, and `@warp-dot-dev/opencode-warp`.

Already inside the Warp app, nothing to install:

- **Bundled skills:** `factory-files`, `factory-mcp`, `oz-platform`, `create-skill`, `add-mcp-server`, `create-tab-config`, `tab-configs`, `pr-comments`, `modify-settings`, `warpctrl`, `claude-api` and others.
- **Community workflows:** `warpdotdev/workflows`, shown as "Global Workflows".

## Install (Linux / WSL2 with WSLg)

```bash
scripts/warp-setup.sh system   # Warp apt repo, warp-terminal, oz (asks for sudo)
scripts/warp-setup.sh user     # Agent CLI, global skills, CLI-agent plugins, tab config
scripts/warp-setup.sh manual   # prints the sign-in / key / MCP / profile steps
```

The manual steps cover:

1. Sign in.
2. Add your Anthropic key under Settings → API keys, and pick an explicit
   Claude model (not Auto).
3. Run `warp --set-provider-api-key anthropic` and `oz login`.
4. Enable the two project MCP servers.
5. Create the two profiles in [`warp/profiles.md`](warp/profiles.md).

## Use

- **Run the factory:** open the repo in Warp (or "+" → *Software factory*), and in an
  agent pane type `/factory-local <request>`. The agent acts as the foreman and
  runs triage, spec, implementer and reviewer as local child agents. It stops at a
  draft PR for you to merge. See [`warp-factory/README.md`](warp-factory/README.md).
- **Skills:** `/skills` lists them, and `/<skill-name>` runs one. Examples:
  - `/review-pr`, `/write-tech-spec`, `/resolve-merge-conflicts`;
  - `/triage-issue-local`, `/security-review-pr`;
  - `/council`, `/saga`.
- **Turn skills on or off:**
  ```bash
  python3 scripts/warp-skills.py list               # skill, source pack, on/off, note
  python3 scripts/warp-skills.py disable council saga
  python3 scripts/warp-skills.py enable council
  python3 scripts/warp-skills.py update oz-skills   # re-vendor, then review git diff
  ```
  `.agents/skills/` holds only relative symlinks into `vendor/warp-skills/<source>/`.
  Warp loads skills one level deep, so this is how the packs stay grouped and
  switchable. `ls -l .agents/skills` shows where each one comes from.
- **Workflows:** Ctrl+Shift+R, then "Factory: …" or "Skills: …".
- **Other built-in agent features:** `/plan`, `/orchestrate`, `/fork`, `/compact`,
  `/open-code-review`.
- **Third-party agents in Warp panes:** Claude Code, Codex and OpenCode, with notifications.
- **Agent CLI:** the same agent without the app is `warp` in any terminal.

**Off by default:**

| Skills | Why |
|---|---|
| `complain`, `suggestion-box` | Tell the agent to post to Warp's internal Slack without asking or telling you |
| `scan-new-specs` | Deprecated upstream |
| `brandalf` | Warp's brand guide |
| `slack-qa-investigate` | Needs Slack |
| `scheduler` | Oz cloud |
| `dbt-model-index`, `terraform-style-check` | Not our stack |

## Free plan: what works and what does not

**Works on Free with your own key:**
- the Warp Agent in the app and the CLI;
- skills, rules, MCP, profiles and workflows;
- `/plan`, code review, and local child agents;
- third-party CLI agents in Warp;
- `/factory-local`.

Local runs have no Warp platform charge.

**Needs Warp credits:**
- Auto models;
- codebase indexing, which also does not work in WSL sessions of the Windows app;
- cloud agents and `/handoff`;
- `oz agent run-cloud`;
- scheduled agents.

**Needs a paid plan:**

| Feature | Plan |
|---|---|
| A GitHub-backed Factory | Warp Factories "Build", $20/month |
| Claude Code / Codex as cloud harnesses | Build |
| Slack in Factories | Build |
| Self-hosted workers | Enterprise |

`warp-factory/README.md` describes how to switch the factory to the cloud.

**Not installed:**

| Item | Why |
|---|---|
| `oz-harness-support` / `orchestration` plugins | Only for Oz cloud environments |
| `oz-agent-action` | GitHub Action, needs credits |
| `figma-skills` | No Figma |
| `gemini-cli-warp` | Gemini CLI is not installed |
| Themes, keysets | Cosmetic |
| The domain agent repos (GTM, CRO, …) | Not relevant here |

## Known limits

- Project MCP servers must be enabled again after every Warp restart.
- Claude Code sessions do not appear in Warp's Agent Management panel.
- If `/skills` does not list the vendored skills, Warp is not following the
  symlinks. Run `python3 scripts/warp-skills.py sync --copy`. In copy mode,
  do not commit the copies in `.agents/skills/`.
