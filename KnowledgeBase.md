# martin-portfolio — Knowledge Base

_The distilled truth about the site: what it is, stack, deploy, and the facts
that bite. The code index (where things live + invariants) is
[`OrientationMap.md`](OrientationMap.md); the chronological history is
[`ResearchJournal.md`](ResearchJournal.md)._

_The bible set: **OrientationMap = the machine · KnowledgeBase = the model ·
ResearchJournal = the history · ToDo = deferrals · Testing = pending verification.**_

_Last verified: 2026-09-02 (master) — added the generator-owned OG-card FACT
(photo-forward refresh, supersampled crispness rule, `?v=` discipline; og-card
left the unversioned-purge list) + deferred volatile cache-bust N to
OrientationMap/code per this doc's own policy. Prior: 2026-08-20 @ ac64bfc
bible-freshening pass; Private & On-Prem AI framing fact (08-19)._

## How to read this doc
**[FACT]** = code/deploy-verified. **[HYP]** = hypothesis + confidence. Volatile
numbers a file owns (cache-bust `?v=`, breakpoints) live in OrientationMap and in the
code — code wins any conflict.

## 1. What it is
- **[FACT]** Single-page **personal portfolio** for **Martin Davidsen** —
  `<title>` "Martin Davidsen — Software & AI Engineer" (confirmed).
  **Person-first, not a company**: framed so employers see the individual,
  leading with software/AI, with the industrial track record as support.
- **[FACT]** Live at **martindavidsen.cc** (permanent personal-brand domain; born
  as `martin.defc0n.no`). Shares its **visual language** (dark theme, Inter, card
  styling) with agentas.net, but the content is re-framed first-person —
  **cross-link, don't duplicate** the two.

## 2. Stack
- **[FACT]** Plain **static** site, **no build step**: `index.html` +
  `styles.css` + `script.js` + `images/` + self-hosted `fonts/`. Served by
  **nginx:alpine** in a container (`Dockerfile` + `nginx.conf`), same shape as
  the Agentas sites.
- **[FACT]** `script.js` provides: bilingual EN/NO toggle, mobile menu,
  scroll-reveal animations, project modals, and a runtime-assembled email.

## 3. Facts that bite
- **[FACT]** **Bilingual is a `textContent` swap.** `setLanguage()` swaps
  `data-en`/`data-no` on every tagged node, persisted in `localStorage['cc-lang']`
  (confirmed — legacy `cc-` key kept; renaming it resets stored prefs).
  INVARIANT: a `data-en/no` element must hold **plain text only** (the swap
  destroys child nodes) — arrows/icons go OUTSIDE, around an inner translatable
  `<span>`. Adding content? Add BOTH languages or it won't translate.
- **[FACT]** **Inter is self-hosted** — one variable `woff2`, **LATIN subset
  only** (`fonts/inter-latin-var.woff2`, `<link rel=preload … crossorigin>`). NO
  Google Fonts (removed to kill render-blocking). The latin range covers
  Norwegian æ/ø/å; glyphs outside latin need a different subset file.
- **[FACT]** **Email is base64-assembled at runtime** into `#cc-email` — the
  plaintext stays out of the committed source (bot-harvest defense).
- **[FACT]** **Cache-bust discipline:** `styles.css?v=N` + `script.js?v=N` in
  `index.html` — bump on any functional CSS/JS change (current N lives in
  OrientationMap/code — code wins). Assets serve `immutable, 30d` and are
  Cloudflare-edge-cached; the HTML is `no-cache`. **Unversioned files**
  (`robots.txt`, `favicon.*`, `apple-touch-icon.png`, any reused image name) can
  serve **stale from the CF edge after a deploy** → Custom-Purge that URL in
  Cloudflare (the exact list + the verify-with-`?cb=1` trick are in
  OrientationMap). `og-card.jpg` left this list 2026-09-02 — now referenced
  `?v=N`, so a regen bumps N instead of purging.
- **[FACT]** **The OG share card is generator-owned** (2026-09-02):
  `gen-og-card.py` (repo root, not served) renders `images/og-card.jpg` —
  photo-forward refresh of the original hand-made card (circular headshot +
  `--gradient-accent` ring, name/role/"Founder of Agentas AS"/domain) on the
  site's own `:root` palette. Rendered SUPERSAMPLED (3×→LANCZOS, flat
  backgrounds) because LinkedIn downscales cards to ~500px + re-encodes — fine
  detail turns to mush (rule established on the agentas-sites cards the same
  day, incl. the eyeball-check: downscale to ~523×274 JPEG q85 and look at
  THAT). Regen = rerun + bump `?v=` (og:image, twitter:image, JSON-LD `image`)
  + LinkedIn Post-Inspector re-scrape. Needs `_assets/inter.ttf` (gitignored).
- **[FACT]** **Marketing-safe images only** — no client names / repo paths /
  failing tests visible (same rule as agentas-sites).
- **[FACT]** **Private & On-Prem AI pillar (added 2026-08-19) is framed as
  capability, not a shipped client deployment.** The full-width
  `.service-card--feature` card below `#focus`'s four cards says "I run
  open-weight LLMs on my own machines and homelab" — true (hands-on local
  models + a self-hosted inference box) — but does NOT claim a completed
  client on-prem AI project. Keep future AI copy on this site to the same
  honest line (standing capability-vs-deployment framing rule, David).

## 4. Deploy
- **[FACT]** Push **`master`** → `.github/workflows/deploy.yml` → Tailscale SSH →
  LXC `/apps/martin-portfolio` → `docker compose build --no-cache && up -d`.
  Manual re-run via `workflow_dispatch`. Host port **3040** (3030 was taken by
  epoch-sim).
