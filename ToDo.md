# ToDo — martin-portfolio

<!-- STRICT deferral ledger (~/.claude/CLAUDE.md §5): the MOMENT anything is set aside /
     deferred / decided-not-now, it gets an entry here — session history routinely loses it.
     Lifecycle: done → check off, prune on the next touch. Never a write-only graveyard. -->

_Last touched 2026-09-28. (Pruned: the restyle pick — done as the Nordic restyle, RJ 2026-09-28b;
the hero-products follow-up — that image left the site with it.)_

## Open
- [ ] **Aurly shots follow apex** — `images/aurly.webp` is apex's `aurly-1` (region dropdown
  still reads "Rogaland"; apex ToDo re-shoots it after the national run). When apex
  re-shoots, copy the new file in under a NEW name (e.g. `aurly-3.webp`) and repoint the card.

## Blocked / needs the user
- [ ] **Desktop hero background — pick A / B / C** (2026-09-28). User: the hard-edged sand block
  behind the rounded portrait looks odd; maybe wider / further left. It also runs straight into
  the sand About section, so the text area reads as a cut-out. Options (desktop ≥901px only;
  hero background becomes plain `--bg-primary` in all three, so the hero ends cleanly before
  About): **A** a rounded (40px) sand panel behind the portrait, reaching 84px left of it
  (40–57px clear of the name at 1024–1440) — recommended; **B** a full-height panel from 54%
  with a 72px rounded bottom-left corner, stopping 64px above the hero bottom; **C** no panel,
  a large soft sand circle behind the portrait. Each option's CSS is the last `<style>` block in
  `drafts/mockups/hero-{a,b,c}.html` (gitignored, local only; open from disk to compare). Implementing = move
  the chosen block into the `#hero`/`.hero-visual` rules in `styles.css`, drop the split
  gradient, bump `?v=`.
- [ ] **Smaller style carry-overs from the apex 09-25 pass — proposed, awaiting OK:**
  section padding 120→80px (apex: "too much space between sections"); `h1,h2,h3
  { text-wrap: balance }`; drop the 01–04 numbers on the `#focus` cards (the Nordic mockup
  kept them, in green). (The pills/tags → plain text item shipped with the restyle.)

## Done (prune on next touch)
(nothing yet)
