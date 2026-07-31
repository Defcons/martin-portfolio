# CODE-MAP — martin-portfolio (martindavidsen.cc)

_Last verified: 2026-07-31_

Single-page static personal portfolio. No build step. Structure: see README.md.

## Subsystems

- **Bilingual toggle** — `script.js` `setLanguage()`: swaps `textContent` from `data-en`/`data-no`
  attributes on every `[data-en][data-no]` element; persisted in `localStorage['cc-lang']`
  (legacy `cc-` key kept — renaming resets stored user prefs).
  **INVARIANT:** `el.textContent = …` destroys child nodes, so an element carrying
  `data-en`/`data-no` must contain plain text ONLY. Links with trailing arrows/icons must
  nest the translatable part in an inner `<span data-en data-no>` with the arrow outside
  (see `.timeline-links` / `.ai-card-cta` markup in `index.html`).
- **Project modal** — `script.js` `initModal()`: any `.ai-card--modal` opens a modal fed by
  card `data-*` attrs (`data-shot`/`data-shot2` images, `data-link`/`data-link-label`,
  `data-link2…`, `data-private`, `data-fit="contain"`). Card screenshots appear ONLY in the
  modal, not on the card face.
- **Email obfuscation** — `script.js` init: address base64-assembled at runtime into `#cc-email`
  (keeps plaintext out of the repo).

## Conventions / gotchas

- **Cache-bust:** `styles.css?v=N` + `script.js?v=N` in `index.html` — bump on any functional
  CSS/JS change. Image `data-shot`s carry `?v=1`; new image = new filename instead of bump.
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
