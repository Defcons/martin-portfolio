# martin-portfolio — Knowledge Base

_The distilled truth about the site: what it is, stack, deploy, and the facts
that bite. The code index (where things live + invariants) is
[`OrientationMap.md`](OrientationMap.md); the chronological history is
[`ResearchJournal.md`](ResearchJournal.md)._

_The bible set: **OrientationMap = the machine · KnowledgeBase = the model ·
ResearchJournal = the history · ToDo = deferrals · Testing = pending verification.**_

_Last verified: 2026-09-28 — Nordic restyle: look now deliberately distinct from
agentas.net; two self-hosted fonts; OG card on the new palette. Prior: 2026-09-02
(master) — added the generator-owned OG-card FACT
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
  `<title>` "Martin Davidsen — AI Architect & Software Engineer" (changed 2026-09-25 from "Software & AI Engineer" — user's pick; must match apex founder line, CV and LinkedIn).
  **Person-first, not a company**: framed so employers see the individual,
  leading with software/AI, with the industrial track record as support.
- **[FACT]** Live at **martindavidsen.cc** (permanent personal-brand domain; born
  as `martin.defc0n.no`). Since 2026-09-28 its **look is deliberately its own**
  (sand + fjord green, Bricolage Grotesque headings, portrait hero) — until then it
  shared agentas.net's tokens, hero image and components so closely that it read
  as a copy (user's verdict; side-by-side audit in RJ 2026-09-28). Content is
  first-person; projects and screenshots are shared — **cross-link, don't duplicate**.

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
- **[FACT]** **Fonts are self-hosted** — Inter (body) and Bricolage Grotesque
  (display), each one variable **LATIN-subset** `woff2` in `fonts/`, each
  preloaded. NO Google Fonts (removed to kill render-blocking). The latin range
  covers Norwegian æ/ø/å and the em/en dashes; neither file has → (U+2192), so
  arrows render in a system fallback. Bricolage is Google Fonts' latin file for
  `opsz,wght` (77 KB) — the opsz axis matters: without it large headings lose
  their display cut.
- **[FACT]** **Email is base64-assembled at runtime** into `#cc-email` — the
  plaintext stays out of the committed source (bot-harvest defense). The address is
  `davidsen908@gmail.com` ON PURPOSE (user, 2026-09-28): the one exception to the career
  canon's martin@agentas.net — don't "unify" it.
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
  photo-forward card (circular headshot + `--accent` ring, name in Bricolage,
  role/"Founder of Agentas AS"/domain) on the site's own `:root` palette, whose
  RGB values are copied into the script by hand (2026-09-28: sand + fjord green). Rendered SUPERSAMPLED (3×→LANCZOS, flat
  backgrounds) because LinkedIn downscales cards to ~500px + re-encodes — fine
  detail turns to mush (rule established on the agentas-sites cards the same
  day). Regen = rerun + bump `?v=` (og:image, twitter:image, JSON-LD `image`)
  + LinkedIn Post-Inspector re-scrape. Needs `_assets/inter-var.ttf` + `_assets/bricolage.ttf`
  (gitignored; both = the site's woff2 saved with fontTools `flavor=None`).
- **[FACT]** LinkedIn's Post Inspector shows the card SOFTER than a plain ~523px
  LANCZOS + JPEG q85 downscale: the 2026-09-28 green card (31px secondary lines, green
  role text) passed that local check yet the user saw it blurry on LinkedIn. So the local
  check must be harsher (≈400px copy, JPEG q60, upscaled to 520).
- **[FACT]** Text ≥40px on the 1200px canvas, bold weights, dark ink instead of
  accent-coloured text (chroma subsampling smears coloured strokes) and a q95 4:4:4 source
  make the card read sharp on LinkedIn: the `?v=4` card passed the harsh local check where
  `?v=3` failed, and the user confirmed it in LinkedIn's Post Inspector (2026-09-28).
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
