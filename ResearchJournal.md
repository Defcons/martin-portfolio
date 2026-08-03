# martin-portfolio — Research Journal

_Append-only chronological history: what shipped when. The distilled current
truth lives in [`KnowledgeBase.md`](KnowledgeBase.md); the code index in
[`OrientationMap.md`](OrientationMap.md)._

_The triad: **OrientationMap = the machine · KnowledgeBase = the model ·
ResearchJournal = the history.**_

_Last verified: 2026-08-03 (three-cards commit, master) — appended the
Watcher/Oslo-Scout/WebOps entry._

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

## Note
The domain evolved `martin.defc0n.no` → **martindavidsen.cc** — the permanent
personal brand, kept deliberately distinct from the agentas.net company sites.
