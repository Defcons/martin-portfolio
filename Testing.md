# martin-portfolio — Pending Tests (unconfirmed)

_Last verified: 2026-09-28c — one pending item below (LinkedIn re-scrape of the re-laid-out OG card).
Everything else is live and verified._

## LinkedIn preview of the OG card is SHARP (card `?v=4`)
- **Context:** the first green card (`?v=3`) showed up on LinkedIn but blurry (user, 2026-09-28).
  `gen-og-card.py` was re-laid-out for legibility: name bigger, role on two lines in bold DARK
  text, one "Founder of Agentas AS" line (the "Stavanger, Norway" line is gone), domain in bold,
  thicker ring, saved at JPEG q95 with full colour detail (4:4:4). Referenced as `?v=4`.
- **Repro (needs a LinkedIn login):** https://www.linkedin.com/post-inspector/ → inspect
  `https://martindavidsen.cc/` (forces a fresh scrape).
- **Pass criteria:** the preview shows the NEW layout (role split over two lines, no
  "Stavanger, Norway" line) and "Founder of Agentas AS" and "martindavidsen.cc" are readable
  without squinting. Old layout (role on one green line + a Stavanger line) = LinkedIn still
  cached `?v=3`: inspect again.
- **Already machine-verified (do not re-test):** 1200×630 JPEG, q95 4:4:4; head `og:image`,
  `twitter:image` and JSON-LD `image` carry `?v=4`; under a harsh local stand-in for LinkedIn
  (≈400px copy, JPEG q60, shown at 520px) every line is legible, where `?v=3` was not.
- On pass: move the KnowledgeBase OG-legibility HYP to FACT, note it in `ResearchJournal.md`
  (2026-09-28c) and DELETE this entry. On fail: go bigger still / drop the founder line.
