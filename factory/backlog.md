# Backlog

`/factory next` takes the first unchecked item, ticks it, appends the job id, and runs it through the loop.

- [ ] Health endpoint: a minimal HTTP service with `GET /health` returning `{"ok": true}`, plus the repo's first test setup and test command
- [ ] Rate limiting: limit each client IP to 60 requests per minute on all endpoints, returning 429 with a `Retry-After` header
- [ ] Request logging: one structured log line per request with method, path, status and duration
