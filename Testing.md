# martin-portfolio — Pending Tests (unconfirmed)

_Last verified: 2026-09-28 — one pending item below (LinkedIn re-scrape of the green OG card).
Everything else is live and verified._

## LinkedIn preview shows the NEW (green) OG card
- **Context:** the 2026-09-28 Nordic restyle regenerated `images/og-card.jpg` via
  `gen-og-card.py` (sand + fjord-green palette, name in Bricolage Grotesque) and bumped it to
  `?v=3`. LinkedIn keeps the card from its last scrape until it is asked to re-scrape.
- **Repro (needs a LinkedIn login):** https://www.linkedin.com/post-inspector/ → inspect
  `https://martindavidsen.cc/` (forces a fresh scrape).
- **Pass criteria:** the preview shows the NEW card: warm sand/off-white background, green ring
  around the headshot, green underline under "Martin Davidsen", role "AI Architect & Software
  Engineer" in green; crisp, with no ingestion warnings. (Blue ring/underline = old card = fail.)
- **Already machine-verified (do not re-test):** card is 1200×630 JPEG and crisp in a simulated
  LinkedIn downscale (~523×274); head `og:image`/`twitter:image` and JSON-LD `image` all carry
  `?v=3`; the crawl chain is known-good from earlier scrapes.
- On confirmation: note the result in `ResearchJournal.md` (2026-09-28b) and DELETE this entry.
