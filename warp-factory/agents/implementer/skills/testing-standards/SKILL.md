---
name: testing-standards
description: How the implementation agent proves a change works before opening a PR. Use when writing or running tests for a factory change.
---

# Testing standards

Only the implementer can read this skill; it lives under
`agents/implementer/skills/`.

The repo has no application test suite yet. Prove each change with the checks
that cover it:

- Factory files changed: `python3 -I tools/warp/validate_factory_files.py warp-factory`
  must print "factory files are valid". Exit code 2 means the server was not
  reached and nothing was checked; say so instead of claiming a pass.
- Skills or `vendor/warp-skills/skills.toml` changed: `python3 scripts/warp-skills.py check`
  must print `ok`.
- Python changed: run it with `python3 -I` on a small input and show the output.
  When you add logic with branches, add a stdlib `unittest` next to it and run it.
- YAML, TOML, or JSON changed: parse every changed file.
- Bug fix: show the failing check before the change and the passing one after.
