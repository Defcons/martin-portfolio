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
  Same for the hero: apex will regenerate `hero-products.webp` (its Aurly half shows the same
  dropdown) → copy over `images/hero-products.webp` and bump `?v=1` → `?v=2` in `index.html`.

## Blocked / needs the user
- [ ] **Restyle so the portfolio stops reading as an apex copy — pick 1 / 2 / 3 / 4** (2026-09-28).
  Audit: same tokens as apex (Inter, `#2563eb` + blue→cyan gradient, radius 12/8/20, 1200px),
  same hero layout AND the same `hero-products.webp`, same accordion + Products cards, same
  small-caps label over bold title, same tag pills + blue icon tiles. Four whole-page directions
  rendered by `drafts/restyle-mockups.py` (theme CSS + a hero-visual swap injected into the local
  page; copy unchanged): **1 Field Notes** (paper, Fraunces serif, copper, hairlines),
  **2 Control Room** (graphite, amber, Space Grotesk + JetBrains Mono, panels + career trace),
  **3 Nordic** (sand + fjord green, Bricolage Grotesque, soft cards, "Now building" note),
  **4 Swiss** (giant Archivo name, black/white, safety orange). All swap the apex composite for
  the portrait and turn tags/status pills/count bubbles into plain text. Implementing: self-host
  the chosen fonts (latin woff2, like Inter — no Google Fonts), move the theme into
  `styles.css`, export a hero portrait from `C:\Dev\career\cv\martin@2x.jpg`, decide the phone
  hero (portrait currently lands below the first screen), bump `?v=`. Absorbs most of the
  carry-overs below.
- [ ] **Contact email — which address?** The contact card assembles `davidsen908@gmail.com`
  (`script.js` `atob`), but the career canon (2026-09-03) made `martin@agentas.net` the one
  public contact on LinkedIn/GitHub. Keep Gmail here on purpose, or switch?
- [ ] **Smaller style carry-overs from the apex 09-25 pass — proposed, awaiting OK:**
  section padding 120→80px (apex: "too much space between sections"); `h1,h2,h3
  { text-wrap: balance }`; drop the 01–04 numbers on the `#focus` cards (apex removed
  its service numbers); older `#work` cards' status pills + tag rows → plain text per
  the no-badges rule (e.g. a "Status" line in the modal).

## Done (prune on next touch)
(nothing yet)
