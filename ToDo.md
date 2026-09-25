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
- [ ] **Hero redesign — pick A / B / C (or keep current)** (2026-09-25). The current hero carries
  the same tells apex dropped as "AI-made" (pill badge, gradient text, grid bg + glow,
  bouncing scroll mouse, centred stack). Three variants mocked in the existing design
  system by `drafts/hero-variants.py` (DOM injection into the local site; not served —
  the Dockerfile COPYs an explicit list): **A** portrait split (text left, large 4:5
  portrait right), **B** work-forward (apex's Consult+Aurly composite + round avatar),
  **C** portrait + two floating product shots. All keep the name H1, role, current sub-copy,
  CTAs and stats (stats become plain dark numbers over a hairline). Implementing = move the
  chosen markup (with `data-en/no`) + CSS into `index.html`/`styles.css`, export a ~900px
  hero portrait from `C:\Dev\career\cv\martin@2x.jpg` to `images/`, bump `styles.css?v=`.
- [ ] **Smaller style carry-overs from the apex 09-25 pass — proposed, awaiting OK:**
  section padding 120→80px (apex: "too much space between sections"); `h1,h2,h3
  { text-wrap: balance }`; drop the 01–04 numbers on the `#focus` cards (apex removed
  its service numbers); older `#work` cards' status pills + tag rows → plain text per
  the no-badges rule (e.g. a "Status" line in the modal).
- [ ] **Deploy the 2026-09-25 apex-sync commit, then Cloudflare Custom-Purge the 5 deleted
  image URLs** (they stay edge-cached up to 30 d even after the files are gone — the
  4 leaky ones are the point): `https://martindavidsen.cc/images/{trading,watcher,homelab,osloscout,consulting}.jpg?v=1`
  (+ the same without `?v=1`). Verify each with `curl -sI '…?cb=1'` → 404.

## Done (prune on next touch)
(nothing yet)
