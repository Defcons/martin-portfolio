# martin-portfolio — Pending Tests (unconfirmed)

_Last verified: 2026-09-02 (master) — one pending item below (OG-card re-scrape).
Everything earlier (through the 09-02 accordion work) is live and human-verified._

## LinkedIn preview shows the REFRESHED OG card
- **Context:** `images/og-card.jpg` was regenerated 2026-09-02 (photo-forward
  refresh via `gen-og-card.py`, referenced `?v=1`) and deployed. LinkedIn still
  caches the OLD card from the last scrape.
- **Repro (needs a LinkedIn login):** https://www.linkedin.com/post-inspector/ →
  inspect `https://martindavidsen.cc/` (forces a fresh scrape).
- **Pass criteria:** the preview shows the NEW card — gradient ring around the
  headshot + gradient underline under the name — rendered crisp, with no
  ingestion warnings.
- **Already machine-verified (do not re-test):** new card is 1200×630 JPEG,
  crisp in a simulated LinkedIn downscale (~523×274); head carries
  `og:image`/`twitter:image` `?v=1` + `og:image:type`/`alt`; the site previewed
  fine on LinkedIn before, so the crawl chain is known-good.
- On confirmation: note the result in `ResearchJournal.md` (2026-09-02c) and
  DELETE this entry.
