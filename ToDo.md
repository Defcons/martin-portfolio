# ToDo — martin-portfolio

<!-- STRICT deferral ledger (~/.claude/CLAUDE.md §5): the MOMENT anything is set aside /
     deferred / decided-not-now, it gets an entry here — session history routinely loses it.
     Lifecycle: done → check off, prune on the next touch. Never a write-only graveyard. -->

_Last touched 2026-09-25. (Pruned: the done Vehicle Telemetry image entry — history in
ResearchJournal 2026-09-02e.)_

## Open
- [ ] **Aurly shots follow apex** — `images/aurly.webp` is apex's `aurly-1` (region dropdown
  still reads "Rogaland"; apex ToDo re-shoots it after the national run). When apex
  re-shoots, copy the new file in under a NEW name (e.g. `aurly-3.webp`) and repoint the card.

## Blocked / needs the user
- [ ] **Deploy the 2026-09-25 apex-sync commit, then Cloudflare Custom-Purge the 5 deleted
  image URLs** (they stay edge-cached up to 30 d even after the files are gone — the
  4 leaky ones are the point): `https://martindavidsen.cc/images/{trading,watcher,homelab,osloscout,consulting}.jpg?v=1`
  (+ the same without `?v=1`). Verify each with `curl -sI '…?cb=1'` → 404.

## Done (prune on next touch)
(nothing yet)
