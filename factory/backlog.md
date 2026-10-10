# Backlog

`/factory next` runs the first unchecked item and checks it off; `/factory next 3` runs the
first three at once. One feature per line, written the way you would say it to `/factory`:

    - [ ] Add rate limiting to the public API (100 requests/minute per key)

Items started together are built side by side from the same base, so none of them can use
another's code. If one feature builds on another, start it after the first has merged.

## Queue

