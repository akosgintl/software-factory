# Backlog

`/factory next [N]` takes up to N runnable items from the top, ticks each one (`- [x] #n … → <job-id>`), and runs them through the loop at the same time.

Format: `- [ ] #<n> <text>` with an optional `· after #<m>[, #<k>]` suffix. An item is runnable only when every `after` item has been ticked **and** its job is `merged`. Items with no `after` can run in parallel with anything.

- [ ] #1 Health endpoint: a minimal HTTP service with `GET /health` returning `{"ok": true}`, plus the repo's first test setup and test command
- [ ] #2 Rate limiting: limit each client IP to 60 requests per minute on all endpoints, returning 429 with a `Retry-After` header · after #1
- [ ] #3 Request logging: one structured log line per request with method, path, status and duration · after #1
