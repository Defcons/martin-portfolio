# martin-portfolio — Research Journal

_Append-only chronological history: what shipped when. The distilled current
truth lives in [`KnowledgeBase.md`](KnowledgeBase.md); the code index in
[`OrientationMap.md`](OrientationMap.md)._

_The bible set: **OrientationMap = the machine · KnowledgeBase = the model ·
ResearchJournal = the history · ToDo = deferrals · Testing = pending verification.**_

_Last verified: 2026-08-20 @ ac64bfc (master) — bible-freshening pass (see
Timeline entry below)._

## Timeline

### 2026-09-15 — Footer "Built by Agentas" credit
Added an explicit followable footer credit under the copyright line in the existing
`<footer>` (`.footer-bottom.footer-single`): a single `<a href="https://agentas.net"
target="_blank" rel="noopener">` carrying `data-en="Built by Agentas"` /
`data-no="Laget av Agentas"` — text-only inside the anchor so the language toggle's
`textContent` swap is safe. Normal followable link, NO `rel="nofollow"` (deliberate SEO
backlink to Martin's own company). agentas.net was already linked from the About section
and JSON-LD `sameAs`; this is an additional understated credit. New `.footer-credit` CSS
(muted text, hover to primary). Cache-bust styles `?v=11→v=12` (script unchanged at v=6).

### 2026-06-30 — Born
Personal portfolio site created as `martin.defc0n.no`; host port set to 3040
(3030 was already taken by epoch-sim).

### 2026-07-02 — Person-first identity
Switched to a light theme + person-focused content; logo-visibility tweaks; hero
stat 10+ → 9+ Years Engineering.

### 2026-07-08 — Work showcase
Added project screenshots + click-to-expand modals + new projects; added
web.codecrafts.cc as a "Website Studio" work card (title later trimmed to drop
the URL prefix).

### 2026-07-30/31 — Rebrand + polish
`workflow_dispatch` added to the deploy workflow; **Rebrand Codecraft → Agentas**
across the portfolio; **Polish pass** — perf, a11y, responsive, contrast, EN/NO
parity — with the resulting invariants recorded in CODE-MAP.

### 2026-08-01 — Trim
Removed the contact form; copy fixes; image cleanup.

### 2026-08-03 — Triad standardization
CODE-MAP.md → CodeMap.md (`~/.claude/CLAUDE.md` §5); this KnowledgeBase + Journal
seeded the same day (docs-only pass).

### 2026-08-03 — Baby Suite card (10th work card)
Added the family baby apps (Defcons/baby: contraction timer + baby tracker +
pelvic trainer) as one "Selected Work" card after NoBS. Firsts: the site's first
**public-repo link** and the first real use of the modal's `data-link2` (repo +
live landing). Screenshots (`images/babysuite*.jpg`) were staged from patched
local copies — worker URL pointed at an unreachable port, synthetic demo data
seeded via injected localStorage script, **light theme** per David — so no real
family data or production KV was ever involved. HTML-only change + new image
filenames → no cache-bust, no CF purge needed.

### 2026-08-03 — Three more work cards: Watcher, Oslo-Scout, WebOps
Selected Work grew 10 → 13 cards, all Private-badged, same day as the Baby
Suite. Screenshots staged with synthetic data only: **watcher** + **oslo-scout**
via node stubs serving each app's REAL dashboard html with fabricated `/api`
responses (fictional GPU watchlists; fictional Oslo Børs issuers — no real
tickers); **WebOps** by booting the real app in Fiken-mock mode against a
seeded scratchpad DB (`DB_PATH` override — production data/tokens untouched).
These apps are dark-only, so the light-theme screenshot rule didn't apply
(CodeMap rule wording clarified accordingly). Placement: Oslo-Scout after the
Go simulator, Watcher after vehicle telemetry, WebOps directly before Website
Studio (internal platform → productised service).

### 2026-08-03 — Norwegian title pass
David flagged that several NO card titles were calques of English tech phrasing.
Seven titles rewritten to idiomatic Norwegian from picked options (e.g.
"Automatisering av kjøretøytelemetri" → "Automatisk kjørebok og timeføring",
"Tre lokal-først PWA-er" → "Tre apper for babytiden"). Standing rule captured
in global memory: translate the outcome, not the English compound; offer
variants for NO copy.

### 2026-08-19 — Private & On-Prem AI pillar
`#focus` retitled "Four things I'm good at" → "What I'm good at" and gained a
full-width `.service-card--feature` pillar below the four cards — the local/
on-prem AI capability David wants to foreground. Personal-voice copy, kept
honest: "I run open-weight LLMs on my own machines and homelab" (true — David
confirmed hands-on local models + a self-hosted inference box), and "bring the
cloud RAG/agent patterns on-premise" framed as capability, not a shipped client
deployment. Local LLMs + Ollama added to the Skills "AI & LLMs" group. New CSS
`.service-card--feature` (+ ≤768 stack); `styles.css v7→v8`. Mirrors the apex
`#services` pillar (agentas-sites RJ, same day). HTML+CSS change → cache-bust
bumped; held for David's copy review before push.

### 2026-08-20 — Bible-freshening pass
Estate-wide docs maintenance (CLAUDE.md §5). Spot-checked OM's subsystem
pointers/symbols against code — all resolved. Found and fixed a stale
cache-bust figure (OM + KB said "v=7/v=5"; code has been v=9/v=5 since the
08-19 pillar work). Normalized the "triad" self-description in KB/RJ headers
to the current six-doc bible (ToDo.md + Testing.md existed but weren't
listed). Added OM's missing bible-docs pointer list. Normalized the
Testing.md stub into a clean honest-empty ledger. No site behavior changed.

### 2026-09-02 — Category restructure + new cards + fritid (career-alignment)
Part of the cross-surface career alignment (canon in `C:\Dev\career\`). The `#work`
grid was reorganized from a flat card list into **9 labeled category groups** (new
`.ai-cat` CSS spanning the grid): Analytics Platform · Apps · Cyber Security ·
Economy · Tools · Automation · Business Automation · Games · Websites & Client Sites.
**Four new modal cards** — Automated Trading Platform, Table-Scout, AssistKey
(GitHub link), Consulting Lead Engine (describe-only) — added without `data-shot`
(modal hides the media area when no shot). The old "Oslo-Scout — Market Falsification
Rig" card was **reframed to "AI-Assisted Market Analysis"** (dropped the internal
name, "Oslo Børs", and the paper-vs-live framing) per the career KnowledgeBase §4.12
public-safety rule. Siemens Energy timeline entry: **Symra → first oil** (resolved the
long-standing conflict vs agentas.net, which was already correct) + a **well-builder
tool** line. Beyond/fritid gained a 4th personal card **"Life outside the screen"**
(nature/boat/training/family/home). `styles.css v9→v10`. The heavy grid reorder was
done by a subagent under verbatim-preservation rules; render verified via a local
static server (category labels, new cards, fritid card all correct) before push.

### 2026-09-02b — Collapsible category accordions + reorder + merge
Follow-up to the same-day category restructure, per Martin. Three changes:
1. **Merged "Business Automation" into "Automation"** — Agentas WebOps + Consulting Lead Engine
   now sit alongside Vehicle Telemetry ("Automatisk kjørebok") under Automasjon. Grid dropped from
   9 → 8 categories.
2. **Reordered sections** to Martin's spec: Automation · Economy · Tools · Cyber Security ·
   Analytics Platform · Apps · (then Games · Websites & Client Sites).
3. **Made each category a default-collapsed accordion** — clickable `.ai-cat` `<button>` header
   (accent label + count pill + rotating chevron) expands a `.ai-section-panel` via the animatable
   `grid-template-rows: 0fr→1fr` trick (`.ai-section-inner` clips with `overflow:hidden; min-height:0`).
   New JS `initAccordions()` toggles `.open`/`aria-expanded`, injects the per-section card count, and
   reveals a section's cards on open. Reduced-motion disables the row + chevron transitions.

The HTML reorder/merge was done by a **deterministic Python script** (scratchpad) that splits the
grid at `.ai-cat` boundaries and reassembles it — cards preserved byte-for-byte (verified: 17 cards
in, 17 out; clean diff). Verified in real Chrome (localhost:8899): 8 collapsed bars in the right order,
counts 3·2·3·2·2·2·2·1, Automation expands to its 3 cards, NO toggle swaps labels
(Automasjon/Økonomi/Verktøy/…) with counts persisting, modal still opens. `styles.css v=10→v=11`,
`script.js v=5→v6`. **Gotcha reconfirmed:** the in-app (`Claude_Browser`) MCP renders this page BLANK
in screenshots (scroll-reveal + capture quirk) — verify visually in real Chrome, but DOM/CSS assertions
via its `javascript_tool` are reliable.

### 2026-09-02c — OG share card refreshed + made generator-owned
Spun out of the agentas-sites OG/LinkedIn session the same day (see that repo's
ResearchJournal 2026-09-02: the "couldn't generate a preview" was LinkedIn's
negative cache, and its first light apex card came back blurry — LinkedIn
downscales cards to ~500px, killing fine detail). Martin chose "refresh, keep
photo" over a text card for the portfolio (a face beats a logo for a personal
brand). New root `gen-og-card.py` renders `images/og-card.jpg` as a faithful
refresh of the hand-made original — same layout (circular `martin-400.jpg`
headshot left / name-role-location right), rebuilt on the site's `:root` palette
with a `--gradient-accent` photo ring + underline, SUPERSAMPLED 3×→LANCZOS on
flat backgrounds, validated against a simulated LinkedIn downscale (~523×274
JPEG) before shipping. Head: og:image/twitter:image/JSON-LD `image` → `?v=1`
(og-card leaves the unversioned-CF-purge list), + `og:image:type`/`og:image:alt`
+ `twitter:image`. Committed surgically around an in-flight working-tree edit
from the parallel career session (project-card changes left uncommitted, only
the head hunk of index.html staged). Facts promoted → KnowledgeBase §3.

### 2026-09-02d — Full screenshot pass: every card has a shot + games/clouddrive fixes
Martin's polish list, executed in one batch:
1. **Games**: Dreadmark moved before Frostwake; badges swapped (Dreadmark → Live,
   Frostwake → In dev) — done by a deterministic split/reassemble script, cards byte-identical.
2. **Self-Hosted File Platform → open source**: "Open source" badge (live-green), public
   `github.com/Defcons/clouddrive` link, `data-private` dropped; better screenshot (`?v=2`).
3. **NoBS**: replaced both shots with ONE image — the landing page's "The whole app, no
   clutter" 4-phone showcase, captured from nobs.agentas.net via headless Chrome
   (puppeteer-core driving system Chrome, deviceScaleFactor 2, element-screenshot of the
   `section.band`) → 1600px JPG. `data-shot2` removed; orphaned `images/nobs-2.jpg` deleted.
4. **Four new screenshots wired** (Martin supplied via `Downloads\port pics`): consulting.jpg
   (`data-fit=contain`), trading.jpg, tablescout.jpg, assistkey.jpg → the four cards that had
   no `data-shot`. **Every one of the 17 cards now has a working screenshot** (verified by
   loading all `data-shot`s in-browser — no 404s).
5. **Publish-safety redactions (PIL pixelation) before wiring**: consulting.jpg showed real
   prospect companies, real person names (from scraped ads), and the `tech.agentas.net`
   hostname → all pixelated (8 company bands, 4 contact bands, activity entry, outbox
   sender, smtp footer); tablescout.jpg leaked the home address in "distances from …" →
   pixelated (career-KB §1 never-public rule). Trading/assistkey/clouddrive were clean.
   Redactions verified by re-reading the output images.

HTML + images only — no CSS/JS change → cache-bust stays v=11/v=6 (image URLs got their own
`?v` bumps: nobs `?v=2`, clouddrive `?v=2`, four new `?v=1`). Still pending: a NEW vehicle
telemetry image (not in the batch) → ToDo.

### 2026-09-02e — Vehicle Telemetry screenshot (last missing card image)
Martin delivered `vehicle.jpg` (the Kjørebok dashboard — trip tracking, monthly
reimbursement breakdown, recent-trips table). REDACTED before publish (PIL pixelation,
same pipeline as consulting/tablescout): the From/To columns exposed REAL movement
addresses (incl. the home area) and "Work: OneCo" client-site naming; Purpose labels also
covered. Stats/km/dates/types stay legible. Wired as `images/vehicle.jpg?v=1` (new
filename per convention); orphaned `vehicle.webp` deleted. The same redacted image also
replaced the apex copy (`agentas-sites` `images/projects/vehicle.jpg` → `?v=3`).
Every card image on both surfaces is now current.

## Note
The domain evolved `martin.defc0n.no` → **martindavidsen.cc** — the permanent
personal brand, kept deliberately distinct from the agentas.net company sites.

## 2026-09-15 — footer credit retargeted to agentas.net/web
Per David, the footer "Built by Agentas" credit now points to `https://agentas.net/web/`
(the web-services storefront, matching the client-sites convention) instead of the apex.
The About-section link and JSON-LD `sameAs` stay on the apex `https://agentas.net` (identity/
structured-data — a subpath would be wrong there). Note `/web` 301s to `/web/`, so the trailing
slash is used to skip the redirect.

## 2026-09-25 — apex-sync pass (Products category + publish-safety mirror)
Trigger (David): the apex got a big 09-25 pass (agentas-sites `49bac06`: hero, "Products"
category, 18 `/projects/<slug>/` showcases, §4 safety fixes) and the portfolio should reflect it.
Audit found the portfolio still serving BYTE-IDENTICAL copies (sha1-matched) of the 4 card
images apex git-rm'd that day for leaking internal names / trading venue / paper trading /
infra topology: `trading.jpg`, `watcher.jpg`, `homelab.jpg`, `osloscout.jpg`. Replaced with
apex's vetted files under new names (`trading-platform.webp`, `watcher.webp`,
`private-cloud.webp` = diagrams; `market-analysis.jpg` = redacted shot); old files git-rm'd.
Same drift in copy: Dreadmark card said TypeScript/Three.js (it is Unity 6 — the Frostwake
stack), Watcher named "marketplaces… job boards" (grey-zone + job-hunt angle, career KB §4.8),
Analytics said "four isolated containers" (stale since coalogs came down 09-09) → all three
now carry apex's 09-25 wording (NO text uses "AI", not apex's SEO "KI", for page consistency).
Added: **Products** as the first `#work` category — Agentas Consult + Aurly, copy + screenshots
from apex (demo data), no badge/tags per the standing no-badges rule. Retired: Consulting Lead
Engine card (Consult is the productised successor; apex retired it the same day) +
`consulting.jpg`. Every card now links its apex showcase (all 17 URLs curl-verified 200).
Baby Suite GitHub/Pages links dropped (apex dropped them: the repo may go private) → showcase
link instead. Website Studio link `web.agentas.net` → `agentas.net/web/`. Skills: + C#,
Next.js, PostGIS. Agentas timeline entry names the two products. Verified with Playwright
(EN/NO, 1280 + 375 px: no console errors, no horizontal scroll, all 24 card images 200).

### 2026-09-25b — hero redesign (mockup B)
Why: the hero carried the same tells David called "AI-made" on apex (pill badge, gradient
text, grid bg + radial glow, bouncing scroll mouse, centred stack). Three variants were mocked
by DOM injection (A portrait split / B work-forward / C portrait collage); **David picked B.**
Now: two-column `.hero-grid` — eyebrow "Stavanger, Norway · Founder of Agentas AS", name H1,
solid-accent role line, the unchanged sub-copy + CTAs, stats as plain dark numbers over a
hairline; right side `images/hero-products.webp` (apex's framed Consult + Aurly composite, demo
data) with a round avatar (reuses `martin-200/400.jpg`) + caption. No longer 100vh. Collapses
to one column ≤900px with the visual capped at 560px (at full tablet width it swamped the
screen). Removed the orphaned CSS (`.hero-bg-grid/-badge/-highlight/-scroll`,
`.scroll-indicator` + keyframes, old `.stat*`, old ≤768/≤480 hero rules, the later
`.hero-name/.hero-role` overrides, reduced-motion/print hero bits). `styles.css?v=13`.
Verified with Playwright at 1440/1280/1024/900/768/375/320 (EN + NO): no horizontal scroll,
both images load, no console errors.

### 2026-09-25c — deployed + live-verified
Pushed `162dbdb..f929af6` (David: "you push it") → "Deploy to Production" run 36193325900
green. Live: HTML carries `styles.css?v=13`, `hero-products.webp?v=1`, `#aisec-products`;
all 8 new images 200; headless-Chrome render of martindavidsen.cc matches the approved B hero
(no console errors, no horizontal scroll, 2 Products cards). The 5 removed images
(`trading/watcher/homelab/osloscout/consulting.jpg`, with and without `?v=1`) return 404 with
`cf-cache-status: MISS` — nothing was held at the Cloudflare edge, so NO Custom-Purge needed.

- **2026-09-25c** — Personal title changed "Software & AI Engineer" → **"AI Architect & Software Engineer"** (NO "KI-arkitekt og programvareingeniør") at the user's request, as part of an AI-architecture positioning push shared with agentas.net (new `/software-for/ai-architecture/` service page there). Keyword note: in English "AI architect" is mostly a job-title search, which is exactly why it belongs in the personal title. Updated hero-role, about-role, <title>, meta/OG/og:image:alt, JSON-LD jobTitle; regenerated the OG card (role line now auto-fits) → `?v=2`. CV + LinkedIn follow in the career session.

### 2026-09-28 — "doesn't look like a copy of apex": audit + four restyle mockups
Side-by-side full-page renders of the live apex and portfolio showed the portfolio is apex
re-skinned: identical tokens (Inter, `#2563eb`, blue→cyan gradient, radius 12/8/20, 1200px),
the same hero layout with the SAME product composite (adopted 09-25b as hero option B), the same
accordion with the same Products cards, the same small-caps-label + bold-title section heads,
tag pills and blue icon tiles. Four whole-page directions mocked on the real content by
`drafts/restyle-mockups.py` (theme CSS + hero-visual swap, copy untouched): Field Notes,
Control Room, Nordic, Swiss — heroes, full pages (1280) and phone heroes (375), no horizontal
overflow at either width. Mockup-only gotcha: lazy logos need a scroll-walk before a full-page
capture or they render as empty boxes. Pick pending (ToDo).
Same day: `restyle-mockups.py --html` wrote open-from-disk copies to `drafts/mockups/`
(gitignored). The export embeds Inter as a data: URI because browsers may block file:// fonts
from a parent folder (Firefox's strict file-origin policy; not tested here) — in Chrome the
embedded face is the one in use, the stylesheet's own Inter face stays `unloaded`. Styles,
script and images load fine from the parent folder.

### 2026-09-28b — Nordic restyle shipped (user picked mockup 3)
Moved mockup 3 into the real source, rule by rule rather than as an override layer:
- `:root` → sand `#fbf9f5`/`#f1ebe0`, fjord green `#1e5b4d`, warm shadows, radius 18/12/28,
  `--font-display`, `--status-dev`; `--gradient-accent` removed (all six uses were plain
  `background:`, now `var(--accent)`).
- Bricolage Grotesque self-hosted (`fonts/bricolage-latin-var.woff2`, Google Fonts' latin file
  for `opsz,wght`, 77 KB) on name, section titles, card/accordion titles, stats, modal title.
- Borderless soft cards, pill buttons/links, sentence-case section labels with a short rule,
  accordion names in the display face; status/tags/counts as plain text in cards AND the modal.
- Hero: portrait (`images/martin-hero.jpg`, 880×1100, a 4:5 crop of the CV headshot) + a "Now
  building / Bygger nå" link to `#work`; the apex composite, the round avatar and the About photo
  are gone (`hero-products.webp`, `martin-200.jpg` deleted; `martin-400.jpg` stays — the OG
  generator's input). Fixed one mockup flaw: the Private & On-Prem AI icon was white on pale
  green, now green.
- OG card regenerated on the new palette with the name in Bricolage (`?v=3`); favicons redrawn
  as the green "MD" circle and versioned `?v=2` in the head so no Cloudflare purge is needed.
Verified locally with Playwright at 1440/1280/1024/900/768/375/320: both fonts load, no
horizontal overflow, no console errors, badges/tags computed with no background or border, modal
opens with a plain status line, EN/NO swap incl. "Bygger nå"; the 1280 hero matches the mockup
side by side. Left alone (pre-existing unused CSS): `.founder-photo`, `.project-featured`,
`#ai::before`, `.logo-icon` still carry old blue values.
Deployed `cd38c8c` (run 36380780205 green) and live-verified: all new assets 200 (`styles.css?v=14`,
both fonts, `martin-hero.jpg`, `og-card.jpg?v=3`, the four `?v=2` icons); headless Chrome on
martindavidsen.cc at 1280 and 375 loads Inter + Bricolage, `--accent` = `#1e5b4d`, no console
errors, no horizontal overflow.

### 2026-09-28c — sharper OG card, portrait-first phones, Gmail stays
- **OG card blurry on LinkedIn** (user screenshot of the Post Inspector, `?v=3`): the card was
  the new one, but the 31px secondary lines and the green role line were mush. A plain
  523px LANCZOS + q70 local downscale had looked fine, so LinkedIn degrades harder than that.
  Re-laid-out in `gen-og-card.py`: name auto-fit up to 92px, role on two lines at 50px bold in
  dark ink, "Founder of Agentas AS" 42px, domain 42px bold, "Stavanger, Norway" dropped, ring
  10px, photo panel 450px; fonts now weight-controlled via `_assets/inter-var.ttf` (the site's
  variable Inter; the old `_assets/inter.ttf` was a static Medium); saved q95 4:4:4 → `?v=4`.
  Harsh local stand-in (400px copy, q60, shown at 520px): new card legible, old one not.
  Pending the user's re-scrape (Testing.md).
- **Phone hero** — user: "as you recommend" → portrait first on ≤900px (`order: -1`, 260px wide),
  "Now building" note hangs 18px off the photo's bottom edge. Name still on the first screen at
  375×812 and 320×640 (checked), 26px clear above the eyebrow at 375. `styles.css?v=15`.
- **Contact email** — user: keep `davidsen908@gmail.com` on the portfolio (recorded in the KB and
  in the career KB §1 as the deliberate exception).
- **Desktop hero background** (user: hard sand block vs rounded photo looks odd) — three options
  mocked (`hero_panel.py` → screenshots + `drafts/mockups/hero-*.html`), pick pending (ToDo).

### 2026-09-28d — hero background option A shipped
User: "looks good" (taken as A, the recommended option; flagged in chat). Hero loses the 60/40
split gradient (plain `--bg-primary`, so it ends cleanly before the sand About section); a
rounded 40px sand panel sits behind the portrait as `.hero-visual::before`, 40px above/below,
48px right, 84px left. Real-source check caught what the mockup screenshots (1280/1440 only)
did not: at 1024px the panel painted over the end of the intro paragraph — once the photo fills
its grid column (≤~1160px) an 84px reach exceeds the 72px column gap. Fixed with a ≤1160px
override to 44px; a 901–1920px sweep (10px steps) then measured ≥28px between the panel and
every hero text line, no overflow, no console errors. Hidden ≤900px (phone/tablet layout keeps
the portrait-first stack). `styles.css?v=16`.

### 2026-09-28e — style carry-overs shipped (user: "do those style tweaks")
The three leftovers from the apex 09-25 pass: `section` padding 120→80px (and 80→56px ≤768,
apex's pairing), `h1, h2, h3 { text-wrap: balance }` sitewide (replaces the hero name's own
rule), and the `#focus` cards' 01–04 numbers dropped (markup + the now-unused `.service-num`
rule). Page height 8768→8166px at 1280 and 13905→13401px at 375; heading line counts unchanged,
multi-line headings now split evenly; no overflow or console errors. `styles.css?v=17`.
