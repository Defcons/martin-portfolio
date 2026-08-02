# CodeMap — martin-portfolio (martindavidsen.cc)

_Last verified: 2026-08-03 @ ac9caf7 (master) — standardized filename → CodeMap.md; pointers spot-checked_

Single-page static personal portfolio. No build step. Structure: see README.md.

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
- **Email obfuscation** — `script.js` init: address base64-assembled at runtime into `#cc-email`
  (keeps plaintext out of the repo).
- **Fonts** — Inter is **self-hosted** (`fonts/inter-latin-var.woff2`, one variable file, weights
  300–800, LATIN subset only). `@font-face` at the top of `styles.css` + `<link rel=preload …
  crossorigin>` in the head; NO Google Fonts (removed to kill render-blocking). The latin
  unicode-range covers Norwegian æ/ø/å; adding glyphs outside latin needs a different subset file.

## Conventions / gotchas

- **Cache-bust:** `styles.css?v=N` + `script.js?v=N` in `index.html` — bump on any functional
  CSS/JS change (currently **v=6 / v=4**). Image `data-shot`s carry `?v=1`; new image = new
  filename instead of bump.
- **UNVERSIONED files + Cloudflare cache:** assets are served `Cache-Control: immutable, 30d`
  and Cloudflare caches them at the edge; the HTML is `no-cache` (nginx `expires -1` in `location /`).
  Files WITHOUT a `?v` (`robots.txt`, `favicon.*`, `apple-touch-icon.png`, `og-card.jpg`, and any
  image reused under the same name) can serve **stale from the CF edge after a deploy** — the origin
  is correct but `cf-cache-status: HIT` serves the old copy. After changing/deleting any unversioned
  file, **Custom-Purge that URL in Cloudflare** (verify with `curl '…?cb=1'` which bypasses the edge).
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
  agentas-sites.
