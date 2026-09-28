# OrientationMap — martin-portfolio (martindavidsen.cc)

_Last verified: 2026-09-28d — desktop hero background = option A: plain hero bg + a rounded (40px) sand panel as `.hero-visual::before` (84px left of the photo, 44px at ≤1160px so it never covers the text column; hidden ≤900px); `styles.css?v=16`. Detail → RJ 2026-09-28d._

_(prior 2026-09-28c) OG card re-laid-out for LinkedIn legibility (bigger/bolder DARK text, 2-line role, q95 4:4:4 → `?v=4`); phones show the hero portrait FIRST (`order:-1`, 260px, note hangs off its bottom edge); `styles.css?v=15`; contact email stays Gmail (user). Detail → RJ 2026-09-28c._

_(prior 2026-09-28b) **Nordic restyle** (user picked mockup 3 of 4): sand + fjord-green `:root` palette, Bricolage Grotesque display face (self-hosted) + Inter body, soft borderless cards, pill buttons, portrait hero with a "Now building" link (no more apex composite), status/tags/counts as plain text; OG card + favicons regenerated green (og `?v=3`, icons `?v=2`); `styles.css?v=14`. Detail → RJ 2026-09-28b._

_(prior 2026-09-25c) personal title → **"AI Architect & Software Engineer"** (NO "KI-arkitekt og programvareingeniør"; user's pick, matches agentas.net founder line; CV/LinkedIn via the career session): hero-role, about-role, <title>, meta/OG/alt, JSON-LD jobTitle; `gen-og-card.py` role line now auto-shrinks to fit → og-card `?v=2`. Detail → RJ 2026-09-25c._

_(prior 2026-09-25b) — hero redesigned (David picked mockup B): left text + `hero-products.webp` (the apex Consult/Aurly composite) with a round avatar; pill badge / gradient text / grid bg / scroll mouse and their CSS removed; `styles.css?v=13`. Detail → RJ 2026-09-25b._

_(prior 2026-09-25) apex-sync pass: new FIRST `#work` category **Products** (Agentas Consult + Aurly, no badge/tags); Consulting Lead Engine card retired (Consult is its successor); the 4 images apex git-rm'd for career-KB §4 leaks replaced by apex's diagrams/redaction; every card links its apex showcase; Dreadmark = Unity 6. HTML+images only (cache-bust unchanged). Detail → RJ 2026-09-25._

_(prior 2026-09-02d) **every one of the 17 work cards now has a `data-shot`**
(4 new: consulting/trading/tablescout/assistkey; nobs + clouddrive replaced → `?v=2`;
`nobs-2.jpg` deleted). consulting + tablescout shots are PIL-pixelated for publish-safety
(real names/companies/hostname; home address) — see RJ 2026-09-02d. Games order:
**Dreadmark (Live) before Frostwake (In dev)**. clouddrive card is now **Open source**
(badge + GitHub link, no `data-private`). HTML+images only — cache-bust still v=11/v=6.
Pending: new vehicle-telemetry image (ToDo). Prior 09-02c: OG share card REFRESHED + made generator-owned
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
- **Fonts** — two **self-hosted** variable woff2 files, LATIN subset only: Inter
  (`fonts/inter-latin-var.woff2`, body, wght 300–800) and Bricolage Grotesque
  (`fonts/bricolage-latin-var.woff2`, display, axes opsz 12–96 + wght 200–800 — the opsz axis
  gives the big headings their tighter cut, so keep it on a re-download). `@font-face` at the top
  of `styles.css` + a `<link rel=preload … crossorigin>` each in the head; NO Google Fonts.
  Display face = `var(--font-display)`, applied by ONE grouped selector rule under
  `.section-title` in `styles.css`. Neither subset has → (U+2192): arrows fall back to a system font.
- **Look & tokens** — the palette, radii and shadows live in `:root` (`styles.css`); components use
  the tokens, so a colour change is a token change. Status (`.ai-badge`, `.modal-badge`), tech tags
  (`.service-tags`) and accordion counts (`.ai-cat-count`) render as PLAIN TEXT per the no-badges
  rule — don't reintroduce pills. Hero: DOM order is text then `.hero-visual` (portrait +
  `.hero-now` link); at ≤900px CSS `order: -1` shows the portrait FIRST (user's call via
  "as you recommend", 2026-09-28) — screen readers still get the name first. The sand panel
  behind the desktop portrait is `.hero-visual::before` (`isolation: isolate` keeps its
  `z-index: -1` inside the figure). Its left reach must stay below the 72px column gap once the
  photo fills its column (≤~1160px), or it paints over the intro paragraph — hence the
  ≤1160px override; sweep 901–1440px for text clearance after touching the grid or panel.

## Conventions / gotchas

- **Cache-bust:** `styles.css?v=N` + `script.js?v=N` in `index.html` — bump on any functional
  CSS/JS change (currently **v=16 / v=6**). Image `data-shot`s carry `?v=1`; new image = new
  filename instead of bump.
- **UNVERSIONED files + Cloudflare cache:** assets are served `Cache-Control: immutable, 30d`
  and Cloudflare caches them at the edge; the HTML is `no-cache` (nginx `expires -1` in `location /`).
  Files WITHOUT a `?v` (`robots.txt`, and any image reused under the same name) can serve
  **stale from the CF edge after a deploy** — the origin is correct but `cf-cache-status: HIT`
  serves the old copy. After changing/deleting any unversioned file, **Custom-Purge that URL in
  Cloudflare** (verify with `curl '…?cb=1'` which bypasses the edge). `og-card.jpg` (2026-09-02)
  and the icon links (`favicon.*`, `apple-touch-icon.png`, 2026-09-28) are referenced `?v=N` in the
  head, so a regen = bump N, no purge — only a bare `/favicon.ico` hit can still get the old icon.
- **OG share card is generator-owned:** `images/og-card.jpg` (1200×630, photo-forward: circular
  headshot + accent ring, name in the display face, role/domain) is generated by root
  `gen-og-card.py` — regenerate, don't hand-edit; its palette constants mirror `:root` BY HAND
  (change both). Renders SUPERSAMPLED (3×→LANCZOS) on flat bgs so it stays crisp after LinkedIn's
  ~500px downscale (rule learned on the agentas-sites cards, see that repo's KB §SEO). Needs
  `_assets/inter-var.ttf` + `_assets/bricolage.ttf` (gitignored; both = the site's woff2 files
  decompressed with fontTools). LinkedIn legibility rules (≥40px text, dark ink not accent-coloured
  text, q95 4:4:4) are in the script's docstring; root `.py`/`_assets/` are never served — Dockerfile COPYs an
  explicit list). Favicons (`favicon.svg/-32.png/.ico`, `apple-touch-icon.png`) are hand-made
  to match the nav monogram (green circle, white "MD"). After a regen: bump `?v=` on og:image + twitter:image + JSON-LD `image`, then a
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
- **`drafts/`** — preview/mockup scripts (e.g. `restyle-mockups.py`), NOT served: the Dockerfile
  COPYs an explicit file list.
- **`#work` cards MIRROR apex `#ai`** (agentas-sites `apex/index.html`): same projects, near-same copy,
  shared image files (copied in under their own names). Apex is where the publish-safety review happens
  (binding rules: `C:\Dev\career\KnowledgeBase.md` §4 + "no grey-zone details", e.g. Watcher never names
  its sources) — when apex changes a shared card's claim or image, mirror it here, or a leak apex fixed stays
  live on this site (happened: 09-25). Each card's modal links its apex showcase
  `https://agentas.net/projects/<slug>/` (cross-link, don't duplicate); live-site/GitHub link stays first.
  New cards follow the no-badges rule (no status pill, no tag row) — older siblings keep theirs until touched.
  The LOOK is deliberately NOT apex's (2026-09-28 audit: tokens, hero, section heads and pills had
  made this site read as an apex copy) — share projects and screenshots, never the hero image,
  palette or component styling.
- **Images must be marketing-safe** (no client names/repo paths/failing tests) — same rule as
  agentas-sites. App screenshots are **staged with synthetic demo data** (never real user/family/
  client state; sync/API/DB neutered or stubbed so staging can't touch production) and shot in the
  app's **light theme where one exists** to match the site — dark-only apps shoot their real theme
  (David, 2026-08-03).
