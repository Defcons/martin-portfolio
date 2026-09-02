# OrientationMap — martin-portfolio (martindavidsen.cc)

_Last verified: 2026-09-02c (master) — OG share card REFRESHED + made generator-owned
(`gen-og-card.py` → `images/og-card.jpg`, photo-forward light card on the site palette,
supersampled for LinkedIn-downscale crispness); head og:image/twitter:image/JSON-LD now `?v=1`
(og-card left the unversioned-CF-purge list) + added `og:image:type`/`alt` + `twitter:image`.
Prior 09-02b: the `#work` grid is now **8 collapsible accordion
sections**: `.ai-sections` > `.ai-section` > (`.ai-cat` `<button>` header with `.ai-cat-name`
+ `.ai-cat-count` pill + `.ai-cat-chevron`) + `.ai-section-panel` > `.ai-section-inner` >
per-section `.ai-grid` of cards. **Default-collapsed**, smooth expand via animatable
`grid-template-rows: 0fr→1fr` toggled by the `.open` class. JS `initAccordions()` (script.js)
toggles `.open`/`aria-expanded`, injects each `.ai-cat-count` (card count), and adds `.visible`
to a section's `.ai-card`s on open (they carry `.fade-in` from `initScrollAnimations` but stay
unobserved while clipped). **"Business Automation" category was MERGED into Automation** (WebOps
+ Consulting Lead Engine now sit with Vehicle Telemetry); section order = Automation · Economy ·
Tools · Cyber Security · Analytics Platform · Apps · Games · Websites & Client Sites.
**Cache-bust v=10→v=11 (styles) + v=5→v=6 (script).** Prior 09-02 + 08-20 notes below._

_(prior 2026-09-02) career-alignment pass: introduced the category grouping (then 9 flat
`.ai-cat` labels) + 4 new modal cards (Automated Trading Platform, Table-Scout, AssistKey,
Consulting Lead Engine — no `data-shot`, modal hides the image area) + "Oslo-Scout" reframed to
"AI-Assisted Market Analysis" + Beyond "Life outside the screen" card + Siemens Symra first-oil/
well-builder line. Cache-bust was v=9→v=10._

_(prior) Last verified: 2026-08-20 @ ac64bfc — subsystem pointers spot-checked;
`#focus` "What I'm good at" + Private & On-Prem AI pillar; Local LLMs/Ollama in Skills._

Single-page static personal portfolio. No build step. Structure: see README.md.

**Bible docs** (all at repo root — no `docs/` dir): this file (hub) ·
[`KnowledgeBase.md`](KnowledgeBase.md) (behavior facts, FACT/HYP-tagged) ·
[`ResearchJournal.md`](ResearchJournal.md) (append-only history) ·
[`ToDo.md`](ToDo.md) (deferrals) · [`Testing.md`](Testing.md) (pending manual
tests). No `NavigationMap.md` — this file stays under the ~20 KB split line.

## Subsystems

- **Bilingual toggle** — `script.js` `setLanguage()`: swaps `textContent` from `data-en`/`data-no`
  attributes on every `[data-en][data-no]` element; persisted in `localStorage['cc-lang']`
  (legacy `cc-` key kept — renaming resets stored user prefs). Also translates a small set of
  control **aria-labels** (`#langToggle`, `#hamburger`, `#modalClose`) via a lang map — attributes
  aren't `data-en/no` elements so they're set explicitly here.
  **INVARIANT:** `el.textContent = …` destroys child nodes, so an element carrying
  `data-en`/`data-no` must contain plain text ONLY. Links with trailing arrows/icons must
  nest the translatable part in an inner `<span data-en data-no>` with the arrow outside
  (see `.timeline-links` / `.ai-card-cta` markup in `index.html`). A `&nbsp;` entity in a
  `data-no` value survives the swap (attribute decodes to U+00A0) — used to keep the Beyond
  heading's last word from orphaning.
- **Project modal** — `script.js` `initModal()`: any `.ai-card--modal` opens a modal fed by
  card `data-*` attrs (`data-shot`/`data-shot2` images, `data-link`/`data-link-label`,
  `data-link2…`, `data-private`, `data-fit="contain"`). Card screenshots appear ONLY in the
  modal, not on the card face. Cards get a JS-assigned `aria-labelledby` (their h3 id) so the
  role=button name follows the language toggle; the open dialog **traps Tab focus** (keydown
  handler cycles focusables within `#projectModal`).
- **Category accordion** — `script.js` `initAccordions()`: each `#work` category is a
  `.ai-section` whose `.ai-cat` `<button>` header toggles `.open` on the section (+ `aria-expanded`).
  Collapse/expand is pure CSS: `.ai-section-panel { grid-template-rows: 0fr }` → `1fr` under `.open`,
  with `.ai-section-inner { overflow:hidden; min-height:0 }` doing the clipping. JS also injects the
  `.ai-cat-count` pill and, on open, adds `.visible` to that section's cards (they get `.fade-in` from
  `initScrollAnimations` but are never observed-visible while clipped, so they'd stay at opacity 0
  otherwise). **INVARIANT:** the header label lives in `.ai-cat-name` (the ONLY `data-en/no` element
  in the header) — keep count/chevron OUTSIDE it (see the Bilingual-toggle text-only rule).
- **Email obfuscation** — `script.js` init: address base64-assembled at runtime into `#cc-email`
  (keeps plaintext out of the repo).
- **Fonts** — Inter is **self-hosted** (`fonts/inter-latin-var.woff2`, one variable file, weights
  300–800, LATIN subset only). `@font-face` at the top of `styles.css` + `<link rel=preload …
  crossorigin>` in the head; NO Google Fonts (removed to kill render-blocking). The latin
  unicode-range covers Norwegian æ/ø/å; adding glyphs outside latin needs a different subset file.

## Conventions / gotchas

- **Cache-bust:** `styles.css?v=N` + `script.js?v=N` in `index.html` — bump on any functional
  CSS/JS change (currently **v=11 / v=6**). Image `data-shot`s carry `?v=1`; new image = new
  filename instead of bump.
- **UNVERSIONED files + Cloudflare cache:** assets are served `Cache-Control: immutable, 30d`
  and Cloudflare caches them at the edge; the HTML is `no-cache` (nginx `expires -1` in `location /`).
  Files WITHOUT a `?v` (`robots.txt`, `favicon.*`, `apple-touch-icon.png`, and any
  image reused under the same name) can serve **stale from the CF edge after a deploy** — the origin
  is correct but `cf-cache-status: HIT` serves the old copy. After changing/deleting any unversioned
  file, **Custom-Purge that URL in Cloudflare** (verify with `curl '…?cb=1'` which bypasses the edge).
  `og-card.jpg` LEFT this list 2026-09-02: the head + JSON-LD now reference it `?v=1`, so a regen =
  bump N (no purge).
- **OG share card is generator-owned:** `images/og-card.jpg` (1200×630, photo-forward: circular
  headshot + gradient ring, name/role/domain) is generated by root `gen-og-card.py` — regenerate,
  don't hand-edit. Renders SUPERSAMPLED (3×→LANCZOS) on flat bgs so it stays crisp after LinkedIn's
  ~500px downscale (rule learned on the agentas-sites cards, see that repo's KB §SEO). Needs
  `_assets/inter.ttf` (gitignored; root `.py`/`_assets/` are never served — Dockerfile COPYs an
  explicit list). After a regen: bump `?v=` on og:image + twitter:image + JSON-LD `image`, then a
  LinkedIn Post-Inspector re-scrape.
- **Responsive nav:** the hamburger drawer activates at **≤1024px** (its own media query), NOT 768 —
  tablets/landscape phones would otherwise get the desktop navbar and wrap the logo/NO links into the
  sticky header. The `≤768` block handles grid-collapse only. Closed drawer is `visibility:hidden`
  (no phantom tab stops).
- **LF line endings** throughout (git core.autocrlf warns; repo stores LF).
- **Deploy:** push master → `.github/workflows/deploy.yml` → Tailscale SSH → LXC
  `/apps/martin-portfolio` → `docker compose build --no-cache && up -d`. Manual re-run via
  workflow_dispatch. Domain martindavidsen.cc is permanent (personal brand; distinct from
  agentas.net company sites — cross-link, don't duplicate).
- **Screenshot testing:** scroll fade-ins (`initScrollAnimations()` IntersectionObserver,
  opacity 0 until `.visible`) make one-shot headless-Chrome anchor captures render BLANK, and
  the 100vh hero defeats the tall-viewport trick. Verify renders with a real browser
  (Chrome MCP: navigate → wait ~1.5s → screenshot).
- **Images must be marketing-safe** (no client names/repo paths/failing tests) — same rule as
  agentas-sites. App screenshots are **staged with synthetic demo data** (never real user/family/
  client state; sync/API/DB neutered or stubbed so staging can't touch production) and shot in the
  app's **light theme where one exists** to match the site — dark-only apps shoot their real theme
  (David, 2026-08-03).
