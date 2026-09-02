# martin-portfolio — Research Journal

_Append-only chronological history: what shipped when. The distilled current
truth lives in [`KnowledgeBase.md`](KnowledgeBase.md); the code index in
[`OrientationMap.md`](OrientationMap.md)._

_The bible set: **OrientationMap = the machine · KnowledgeBase = the model ·
ResearchJournal = the history · ToDo = deferrals · Testing = pending verification.**_

_Last verified: 2026-08-20 @ ac64bfc (master) — bible-freshening pass (see
Timeline entry below)._

## Timeline

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

## Note
The domain evolved `martin.defc0n.no` → **martindavidsen.cc** — the permanent
personal brand, kept deliberately distinct from the agentas.net company sites.
