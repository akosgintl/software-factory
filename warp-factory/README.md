# warp-factory

A [Warp Factory](https://docs.warp.dev/factories/factory-as-code/) defined as
files. It is Warp's official issue-to-PR example,
[`02-sdlc-issue-to-pr`](https://github.com/warpdotdev/warp-factory-examples/tree/84e7c952f1506c4bd2784d96fd40a6f4d6398cad/examples/02-sdlc-issue-to-pr)
(MIT, commit `84e7c95`), pointed at this repo. The upstream README, which explains
the runners, routing and trigger shapes, is kept as
[`UPSTREAM-README.md`](UPSTREAM-README.md).

```
factory.yaml                     name software-factory, alias SoftwareFactory
agents/
  foreman/      FOREMAN          orchestrates, owns the human gates
  triage/       TRIAGE           model auto-efficient
  spec/         SPEC
  implementer/  IMPLEMENT        runner linux-build, skill testing-standards
  reviewer/     REVIEW           model auto-genius
  mobile-build/ CUSTOM           runner macos-build (no iOS repo attached)
automations/                     all five present, all enabled: false
  slack-app-mentions/  slack-dms/  linear-agent-sessions/
  github-mention-assign/  github-pr-closed-or-merged/
runners/        linux-standard, linux-build, macos-build
scorers/        task-compliance, review-quality
skills/         repository-conventions
local-runs/     run logs from /factory-local (git-ignored)
```

## What changed from upstream

- `factory.yaml`: name, alias and description; the only repository is
  `akosgintl/software-factory`.
- Automations: `enabled: false` on all five; GitHub filters point at this repo
  and the `factory:SoftwareFactory` label.
- `acme/ios-app` in the foreman and mobile-build prompts now reads "the iOS app
  repository (none is attached to this factory yet)".
- `runners/linux-build.yaml`: `python:3.12-bookworm` instead of the Go image, and
  no Go setup command.
- The two skill stubs now hold this repo's conventions and checks.
- Scorers: a `name` field in each `scorer.md`, which the published schema
  requires.

The agent prompts and scorer rubrics are otherwise verbatim.

## Names

Agents, automations and runners take their name from their path. To rename
one, move its file or directory.

Scorers are the exception. A Scorer's identity is the `name` field in its
frontmatter, and its directory is only a filesystem slug. Keep `name` equal to
the directory name, and when you rename a Scorer, change both together. Moving
the directory alone does not rename it.

## Run it locally (Free plan)

Ask the Warp Agent, in this repo, with your own Anthropic key selected:

```
/factory-local <what you want done>
```

The [`factory-local`](../.agents/skills/factory-local/SKILL.md) skill makes the
agent act as the foreman and run the other agents as local child agents. It
also maps the cloud-only parts:

- Slack and Linear become this conversation.
- The tracker is GitHub Issues.
- Automations are off.
- `mobile-build` is unavailable.

The human gates stay: spec approval, and a draft PR that a human merges. Local
runs carry no Warp platform charge. Inference is billed to your own key.

You can also start it from the workflow palette (Ctrl+Shift+R → "Factory: run
locally"), which wraps `oz agent run`.

## Validate

```bash
python3 -I tools/warp/validate_factory_files.py warp-factory
```

The validator sends the files to Warp's server-side parser. It needs network
access but no login.

| Exit | Meaning |
|---|---|
| 0 | valid |
| 1 | diagnostics |
| 2 | not checked (e.g. offline) |

Model ids, runners, secrets and integrations are only checked when the factory
is applied.

## Run it in Warp's cloud (paid)

None of this is needed for local use.

1. Plan:
   - Warp Factories "Build" ($20/month, usage at API rates) is required to keep
     the definition in this GitHub repo.
   - Pay-as-you-go ($0/month, usage at API rates +20%) only supports
     Warp-hosted definitions edited in the web app.
   - Cloud runs bill inference, compute and platform time, and personal BYOK
     keys are not used.
2. Connect GitHub (and Slack/Linear if you want those automations) to the Warp
   team, and register this directory as the factory root.
3. Set `enabled: true` on the automations you want, one at a time.
