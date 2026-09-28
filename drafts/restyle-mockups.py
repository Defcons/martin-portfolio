"""Preview-only restyle mockups for martindavidsen.cc: theme CSS + small hero DOM swaps injected
into the real local page. Nothing here touches the site files.
Usage: from the repo root run `python -m http.server 8765 --bind 127.0.0.1`, then
       `python drafts/restyle-mockups.py <outdir outside the repo> [v1 v2 v3 v4]`   (screenshots)
   or  `python drafts/restyle-mockups.py --html`   (open-in-a-browser files in drafts/mockups/, gitignored)."""
import sys, pathlib, re, base64, shutil
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

REPO = pathlib.Path(__file__).resolve().parent.parent
URL = "http://127.0.0.1:8765/"
PORTRAIT = r"C:\Dev\career\cv\martin@2x.jpg"
GF = "https://fonts.googleapis.com/css2?"

# ---------------------------------------------------------------- shared: no chips / pills / bubbles
COMMON = """
html.mk .service-tags { display: block; margin-top: 16px; font-size: .78rem; line-height: 1.6; color: var(--text-muted); }
html.mk .service-tags span { display: inline; padding: 0; background: none; border: 0; border-radius: 0; font-size: inherit; font-weight: 500; color: inherit; }
html.mk .service-tags span + span::before { content: " \\00b7  "; }
html.mk .ai-badge { position: static; display: block; padding: 0; background: none; border: 0; border-radius: 0; margin: 0 0 12px; font-size: .7rem; }
html.mk .ai-cat-count { background: none; padding: 0; min-width: 0; font-weight: 500; color: var(--text-muted); }
html.mk .ai-cat-count::before { content: "("; } html.mk .ai-cat-count::after { content: ")"; }
html.mk .lang-toggle { border: 0; background: none; }
html.mk .hero-visual figcaption { padding-left: 0; }
html.mk main { counter-reset: sec; }
html.mk main > section:not(#hero) { counter-increment: sec; }
html.mk .service-card::before { display: none; }
"""

V = {}

# ---------------------------------------------------------------- 1. Field Notes (editorial)
V["v1"] = dict(
 short="1  Field Notes — editorial",
 name="1 \u2014 Field Notes (editorial: paper, serif, copper, hairlines)",
 fonts="family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700",
 hero="""<img class="mk-portrait" src="/__mock/portrait.jpg" alt="Martin Davidsen">
<figcaption>Fig. 1 \u2014 Martin Davidsen, Stavanger</figcaption>""",
 css="""
html.mk-v1 { --bg-primary:#f6f2ea; --bg-secondary:#f6f2ea; --bg-card:transparent; --bg-card-hover:transparent;
  --border:#d8d0c0; --border-light:#bfb5a2; --text-primary:#1d1b17; --text-secondary:#3e3a32; --text-muted:#716a5d;
  --accent:#a8431f; --accent-hover:#86341a; --accent-glow:rgba(168,67,31,.07); --accent-secondary:#a8431f;
  --gradient-accent:linear-gradient(#1d1b17,#1d1b17); --shadow-sm:none; --shadow-md:none;
  --radius:0px; --radius-sm:0px; --radius-lg:0px; --serif:'Fraunces', Georgia, serif; }
html.mk-v1 body { background: var(--bg-primary); }
html.mk-v1 #navbar, html.mk-v1 #navbar.scrolled { background: rgba(246,242,234,.95); box-shadow: none; border-bottom: 1px solid var(--border); }
html.mk-v1 .logo-monogram { display: none; }
html.mk-v1 .logo-text { font-family: var(--serif); font-weight: 600; font-size: 1.3rem; letter-spacing: -.01em; }
html.mk-v1 .hero-name, html.mk-v1 .section-title, html.mk-v1 .about-text h2, html.mk-v1 .ai-card h3, html.mk-v1 .service-card h3,
html.mk-v1 .timeline-head h3, html.mk-v1 .beyond-card h3, html.mk-v1 .ai-cat-name, html.mk-v1 .contact-single h2, html.mk-v1 .service-feature-content h3 { font-family: var(--serif); }
html.mk-v1 main > section:not(#hero) { padding: 96px 0; }
html.mk-v1 main > section:not(#hero) > .container { border-top: 1px solid var(--text-primary); padding-top: 26px; }
html.mk-v1 .section-label { font-family: var(--serif); font-style: italic; text-transform: none; letter-spacing: 0; font-size: 1.05rem; font-weight: 400; color: var(--accent); }
html.mk-v1 .section-label::before { content: counter(sec, decimal-leading-zero) "\\2003"; color: var(--text-muted); font-style: normal; }
html.mk-v1 .contact-single h2 { font-weight: 400; font-size: clamp(2.2rem, 4.4vw, 3.4rem); letter-spacing: -.025em; }
html.mk-v1 .section-title { font-weight: 400; font-size: clamp(2.2rem, 4.4vw, 3.4rem); letter-spacing: -.025em; line-height: 1.08; max-width: 820px; font-variation-settings: "opsz" 144; }
html.mk-v1 .service-card, html.mk-v1 .ai-card, html.mk-v1 .timeline-content, html.mk-v1 .skill-group, html.mk-v1 .beyond-card,
html.mk-v1 .contact-card, html.mk-v1 .service-card--feature { background: transparent; border: 0; border-top: 1px solid var(--text-primary);
  border-radius: 0; box-shadow: none; padding: 20px 0 0; transform: none !important; }
html.mk-v1 .ai-card-icon, html.mk-v1 .beyond-icon, html.mk-v1 .service-feature-icon { display: none; }
html.mk-v1 .service-num { font-family: var(--serif); font-style: italic; font-size: 1rem; letter-spacing: 0; font-weight: 400; }
html.mk-v1 .ai-card h3, html.mk-v1 .service-card h3, html.mk-v1 .beyond-card h3 { font-size: 1.4rem; font-weight: 500; line-height: 1.22; }
html.mk-v1 .ai-card:hover h3 { text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 5px; }
html.mk-v1 .ai-grid, html.mk-v1 .services-grid, html.mk-v1 .skills-grid, html.mk-v1 .beyond-grid { column-gap: 44px; row-gap: 40px; }
html.mk-v1 .ai-badge { font-family: var(--serif); font-style: italic; font-size: .9rem; color: var(--text-muted); }
html.mk-v1 .ai-sections { gap: 0; }
html.mk-v1 .ai-section { border: 0; border-top: 1px solid var(--text-primary); border-radius: 0; background: transparent; box-shadow: none; }
html.mk-v1 .ai-section:last-child { border-bottom: 1px solid var(--text-primary); }
html.mk-v1 .ai-cat { padding: 18px 0; color: var(--text-primary); }
html.mk-v1 .ai-cat:hover, html.mk-v1 .ai-cat:focus-visible { background: transparent; color: var(--accent); }
html.mk-v1 .ai-cat-name { font-size: 1.75rem; font-weight: 400; text-transform: none; letter-spacing: -.01em; }
html.mk-v1 .ai-cat-count { font-family: var(--serif); font-style: italic; font-size: 1rem; }
html.mk-v1 .ai-cat-chevron { color: currentColor; }
html.mk-v1 .ai-section-inner .ai-grid { padding: 8px 0 36px; }
html.mk-v1 .timeline { padding-left: 0; max-width: none; }
html.mk-v1 .timeline::before, html.mk-v1 .timeline-marker { display: none; }
html.mk-v1 .timeline-org { font-family: var(--serif); font-style: italic; font-weight: 400; font-size: 1.05rem; color: var(--accent); }
html.mk-v1 .timeline-head h3 { font-size: 1.45rem; font-weight: 500; }
html.mk-v1 .client-item { background: transparent; border: 0; }
html.mk-v1 .about-photo { display: none; }
html.mk-v1 .btn { border-radius: 0; }
html.mk-v1 .btn-primary { background: var(--text-primary); color: #f6f2ea; box-shadow: none; }
html.mk-v1 .btn-primary:hover { transform: none; background: var(--accent); box-shadow: none; }
html.mk-v1 .btn-outline { border-color: var(--text-primary); }
html.mk-v1 #hero { padding-top: 150px; }
html.mk-v1 .hero-eyebrow { font-family: var(--serif); font-style: italic; font-size: 1.1rem; }
html.mk-v1 .hero-name { font-weight: 400; font-size: clamp(3rem, 7vw, 6.2rem); letter-spacing: -.035em; line-height: .98; font-variation-settings: "opsz" 144; margin-bottom: 18px; }
html.mk-v1 .hero-role { font-family: var(--serif); font-style: italic; font-weight: 400; color: var(--accent); font-size: clamp(1.4rem, 2.4vw, 1.9rem); }
html.mk-v1 .hero-stats { border-top-color: var(--text-primary); }
html.mk-v1 .hero-stat-num { font-family: var(--serif); font-weight: 400; font-size: 2.5rem; }
html.mk-v1 .hero-visual { justify-self: end; width: 100%; max-width: 410px; }
html.mk-v1 .mk-portrait { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: 50% 16%; filter: saturate(.85); }
html.mk-v1 .hero-visual figcaption { font-family: var(--serif); font-style: italic; font-size: .92rem; margin-top: 10px; padding-top: 10px; border-top: 1px solid var(--border); }
@media (max-width: 900px) { html.mk-v1 .hero-visual { justify-self: start; max-width: 340px; } }
""")

# ---------------------------------------------------------------- 2. Control Room (dark industrial)
V["v2"] = dict(
 short="2  Control Room — dark industrial",
 name="2 \u2014 Control Room (dark industrial: graphite, amber, mono)",
 fonts="family=Space+Grotesk:wght@400..700&family=JetBrains+Mono:wght@400..700",
 hero="""<div class="mk-panel">
  <div class="mk-bar"><span>MARTIN DAVIDSEN</span><span>STAVANGER \u00b7 NO</span></div>
  <img class="mk-portrait" src="/__mock/portrait.jpg" alt="Martin Davidsen">
  <ol class="mk-trace">
    <li><b>01</b>Electrician</li><li><b>02</b>Offshore</li><li><b>03</b>Critical infrastructure</li><li class="now"><b>04</b>AI engineering</li>
  </ol>
</div>""",
 css="""
html.mk-v2 { --bg-primary:#0c0e11; --bg-secondary:#101318; --bg-card:#13171c; --bg-card-hover:#171c22; --border:#242b34; --border-light:#333c48;
  --text-primary:#e9edf2; --text-secondary:#b1bac6; --text-muted:#7c8795; --accent:#f2a93b; --accent-hover:#ffbe5c;
  --accent-glow:rgba(242,169,59,.10); --accent-secondary:#f2a93b; --gradient-accent:linear-gradient(#f2a93b,#f2a93b);
  --shadow-sm:none; --shadow-md:none; --radius:4px; --radius-sm:3px; --radius-lg:6px;
  --mono:'JetBrains Mono', ui-monospace, monospace; --display:'Space Grotesk', 'Inter', sans-serif; color-scheme: dark; }
html.mk-v2 body { background: var(--bg-primary); color: var(--text-primary); }
html.mk-v2 #navbar, html.mk-v2 #navbar.scrolled { background: rgba(12,14,17,.92); box-shadow: none; border-bottom: 1px solid var(--border); }
html.mk-v2 .logo-monogram { background: transparent; border: 1px solid var(--accent); color: var(--accent); font-family: var(--mono); border-radius: 3px; }
html.mk-v2 .logo-text { font-family: var(--display); }
html.mk-v2 .nav-links a, html.mk-v2 .lang-toggle { font-family: var(--mono); font-size: .76rem; text-transform: uppercase; letter-spacing: .06em; }
html.mk-v2 .hero-name, html.mk-v2 .section-title, html.mk-v2 .about-text h2, html.mk-v2 .ai-card h3, html.mk-v2 .service-card h3,
html.mk-v2 .timeline-head h3, html.mk-v2 .beyond-card h3, html.mk-v2 .service-feature-content h3, html.mk-v2 .contact-single h2 { font-family: var(--display); }
html.mk-v2 .section-label { font-family: var(--mono); font-weight: 500; letter-spacing: .08em; }
html.mk-v2 .section-label::before { content: "// " counter(sec, decimal-leading-zero) "  "; color: var(--text-muted); }
html.mk-v2 .section-title { font-weight: 600; letter-spacing: -.02em; }
html.mk-v2 .service-card, html.mk-v2 .ai-card, html.mk-v2 .timeline-content, html.mk-v2 .skill-group, html.mk-v2 .beyond-card,
html.mk-v2 .contact-card, html.mk-v2 .service-card--feature { background: var(--bg-card); border: 1px solid var(--border); border-radius: 4px;
  box-shadow: none; transform: none !important; position: relative; }
html.mk-v2 .service-card::after, html.mk-v2 .ai-card::after, html.mk-v2 .timeline-content::after, html.mk-v2 .skill-group::after,
html.mk-v2 .beyond-card::after { content: ''; position: absolute; top: -1px; left: -1px; width: 18px; height: 2px; background: var(--accent); }
html.mk-v2 .ai-card:hover, html.mk-v2 .service-card:hover { border-color: var(--border-light); background: var(--bg-card-hover); }
html.mk-v2 .ai-card-icon, html.mk-v2 .beyond-icon, html.mk-v2 .service-feature-icon { background: transparent; border: 1px solid var(--border-light); border-radius: 3px; width: 40px; height: 40px; }
html.mk-v2 .ai-card-icon svg, html.mk-v2 .beyond-icon svg { color: var(--accent); width: 20px; height: 20px; }
html.mk-v2 .service-num { font-family: var(--mono); }
html.mk-v2 .ai-badge { font-family: var(--mono); color: var(--text-muted); letter-spacing: .06em; font-weight: 500; }
html.mk-v2 .ai-badge::before { content: "\\25cf  "; }
html.mk-v2 .ai-badge--live { color: #5ee08f; } html.mk-v2 .ai-badge--dev { color: var(--accent); }
html.mk-v2 .service-tags { font-family: var(--mono); font-size: .72rem; text-transform: lowercase; }
html.mk-v2 .service-tags span + span::before { content: " / "; }
html.mk-v2 .ai-section { background: var(--bg-card); border: 1px solid var(--border); border-radius: 4px; box-shadow: none; }
html.mk-v2 .ai-cat { color: var(--text-primary); }
html.mk-v2 .ai-cat:hover, html.mk-v2 .ai-cat:focus-visible { background: var(--bg-card-hover); }
html.mk-v2 .ai-cat-name { font-family: var(--mono); font-weight: 500; letter-spacing: .08em; }
html.mk-v2 .ai-cat-count { font-family: var(--mono); color: var(--accent); }
html.mk-v2 .ai-cat-count::before { content: "["; } html.mk-v2 .ai-cat-count::after { content: "]"; }
html.mk-v2 .ai-section-inner .ai-card { background: var(--bg-secondary); }
html.mk-v2 .timeline::before { background: var(--border-light); width: 1px; }
html.mk-v2 .timeline-marker { border-radius: 0; width: 9px; height: 9px; left: -26px; box-shadow: none; }
html.mk-v2 .timeline-org { font-family: var(--mono); font-size: .76rem; text-transform: uppercase; letter-spacing: .06em; }
html.mk-v2 .client-item { background: transparent; }
html.mk-v2 .client-logo { filter: brightness(0) invert(1) opacity(.55); }
html.mk-v2 .about-photo { filter: grayscale(1) contrast(1.05); border-radius: 4px; }
html.mk-v2 .btn { border-radius: 3px; font-family: var(--mono); text-transform: uppercase; letter-spacing: .06em; font-size: .78rem; }
html.mk-v2 .btn-primary { background: var(--accent); color: #111; box-shadow: none; }
html.mk-v2 .btn-primary:hover { background: var(--accent-hover); box-shadow: none; }
html.mk-v2 .btn-outline { color: var(--text-primary); border-color: var(--border-light); }
html.mk-v2 .hero-eyebrow { font-family: var(--mono); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }
html.mk-v2 .hero-name { font-family: var(--display); font-weight: 600; font-size: clamp(2.8rem, 6vw, 5rem); letter-spacing: -.03em; }
html.mk-v2 .hero-role { font-family: var(--mono); font-weight: 500; font-size: 1.15rem; }
html.mk-v2 .hero-role::before { content: "> "; color: var(--text-muted); }
html.mk-v2 .hero-stat-num { font-family: var(--mono); font-weight: 600; }
html.mk-v2 .hero-stat-label { font-family: var(--mono); font-size: .72rem; text-transform: uppercase; letter-spacing: .06em; }
html.mk-v2 .hero-visual { justify-self: end; width: 100%; max-width: 440px; }
html.mk-v2 .mk-panel { border: 1px solid var(--border-light); background: var(--bg-card); border-radius: 4px; position: relative; }
html.mk-v2 .mk-panel::after { content: ''; position: absolute; top: -1px; left: -1px; width: 28px; height: 2px; background: var(--accent); }
html.mk-v2 .mk-bar { display: flex; justify-content: space-between; font-family: var(--mono); font-size: .7rem; letter-spacing: .08em; color: var(--text-muted); padding: 10px 14px; border-bottom: 1px solid var(--border); }
html.mk-v2 .mk-portrait { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; object-position: 50% 22%; filter: grayscale(1) contrast(1.08) brightness(.92); }
html.mk-v2 .mk-trace { list-style: none; margin: 0; padding: 14px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; border-top: 1px solid var(--border); position: relative; }
html.mk-v2 .mk-trace li { font-family: var(--mono); font-size: .66rem; line-height: 1.35; color: var(--text-muted); text-transform: uppercase; letter-spacing: .04em; border-top: 2px solid var(--border-light); padding-top: 8px; }
html.mk-v2 .mk-trace li b { display: block; color: var(--text-secondary); font-weight: 600; margin-bottom: 2px; }
html.mk-v2 .mk-trace li.now { border-top-color: var(--accent); color: var(--text-primary); }
html.mk-v2 .mk-trace li.now b { color: var(--accent); }
@media (max-width: 900px) { html.mk-v2 .hero-visual { justify-self: start; max-width: 360px; } }
""")

# ---------------------------------------------------------------- 3. Nordic (calm, warm, photo-forward)
V["v3"] = dict(
 short="3  Nordic — sand + fjord green",
 name="3 \u2014 Nordic (sand + fjord green, soft, photo-forward)",
 fonts="family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800",
 hero="""<img class="mk-portrait" src="/__mock/portrait.jpg" alt="Martin Davidsen">
<a class="mk-now" href="#work"><span>Now building</span><b>Agentas Consult \u00b7 Aurly \u2192</b></a>""",
 css="""
html.mk-v3 { --bg-primary:#fbf9f5; --bg-secondary:#f1ebe0; --bg-card:#fffdf9; --bg-card-hover:#ffffff; --border:#e6ded0; --border-light:#d6cbb8;
  --text-primary:#14211d; --text-secondary:#3c4944; --text-muted:#66736d; --accent:#1e5b4d; --accent-hover:#15463b;
  --accent-glow:rgba(30,91,77,.08); --accent-secondary:#1e5b4d; --gradient-accent:linear-gradient(#1e5b4d,#1e5b4d);
  --shadow-sm:0 1px 2px rgba(60,45,20,.05), 0 6px 18px rgba(60,45,20,.05); --shadow-md:0 14px 34px rgba(60,45,20,.09);
  --radius:18px; --radius-sm:12px; --radius-lg:28px; --display:'Bricolage Grotesque', 'Inter', sans-serif; }
html.mk-v3 body { background: var(--bg-primary); }
html.mk-v3 #navbar, html.mk-v3 #navbar.scrolled { background: rgba(251,249,245,.92); box-shadow: none; }
html.mk-v3 .logo-monogram { border-radius: 50%; }
html.mk-v3 .logo-text, html.mk-v3 .hero-name, html.mk-v3 .section-title, html.mk-v3 .about-text h2, html.mk-v3 .ai-card h3, html.mk-v3 .service-card h3,
html.mk-v3 .timeline-head h3, html.mk-v3 .beyond-card h3, html.mk-v3 .ai-cat-name, html.mk-v3 .hero-stat-num, html.mk-v3 .service-feature-content h3, html.mk-v3 .contact-single h2 { font-family: var(--display); }
html.mk-v3 .section-label { text-transform: none; letter-spacing: 0; font-size: .98rem; font-weight: 600; display: flex; align-items: center; gap: 12px; }
html.mk-v3 .section-label::before { content: ''; width: 28px; height: 2px; background: var(--accent); }
html.mk-v3 .section-title { font-weight: 700; letter-spacing: -.03em; font-size: clamp(2rem, 4vw, 3rem); max-width: 760px; }
html.mk-v3 .service-card, html.mk-v3 .ai-card, html.mk-v3 .timeline-content, html.mk-v3 .skill-group, html.mk-v3 .beyond-card,
html.mk-v3 .contact-card, html.mk-v3 .service-card--feature { border: 0; background: var(--bg-card); border-radius: 18px; box-shadow: var(--shadow-sm); }
html.mk-v3 .ai-card-icon, html.mk-v3 .beyond-icon, html.mk-v3 .service-feature-icon { background: var(--accent-glow); border-radius: 50%; }
html.mk-v3 .ai-card-icon svg, html.mk-v3 .beyond-icon svg { color: var(--accent); }
html.mk-v3 .service-num { font-family: var(--display); font-size: .95rem; letter-spacing: 0; }
html.mk-v3 .ai-badge { text-transform: none; letter-spacing: 0; font-size: .8rem; font-weight: 600; color: var(--text-muted); }
html.mk-v3 .ai-badge--live { color: var(--accent); } html.mk-v3 .ai-badge--dev { color: #b3601b; }
html.mk-v3 .ai-section { border: 0; border-radius: 18px; background: var(--bg-card); box-shadow: var(--shadow-sm); }
html.mk-v3 .ai-cat { color: var(--text-primary); padding: 22px 26px; }
html.mk-v3 .ai-cat-name { text-transform: none; letter-spacing: -.01em; font-size: 1.3rem; font-weight: 600; }
html.mk-v3 .ai-cat-chevron { color: var(--accent); }
html.mk-v3 .ai-section-inner .ai-card { background: var(--bg-primary); box-shadow: none; }
html.mk-v3 .timeline::before { background: var(--border-light); }
html.mk-v3 .timeline-marker { box-shadow: 0 0 0 4px var(--bg-primary), 0 0 0 5px var(--accent); }
html.mk-v3 .client-item { background: var(--bg-card); border: 0; border-radius: 999px; }
html.mk-v3 .about-photo { display: none; }
html.mk-v3 .btn { border-radius: 999px; }
html.mk-v3 .btn-primary { background: var(--accent); box-shadow: none; }
html.mk-v3 .btn-primary:hover { background: var(--accent-hover); box-shadow: none; }
html.mk-v3 .btn-outline { border-color: var(--border-light); background: var(--bg-card); }
html.mk-v3 #hero { background: linear-gradient(90deg, var(--bg-primary) 0 60%, var(--bg-secondary) 60% 100%); padding-bottom: 96px; }
html.mk-v3 .hero-eyebrow { color: var(--accent); font-weight: 600; }
html.mk-v3 .hero-name { font-weight: 700; letter-spacing: -.04em; font-size: clamp(2.8rem, 6.2vw, 5.4rem); }
html.mk-v3 .hero-role { color: var(--text-primary); font-weight: 500; }
html.mk-v3 .hero-stat-num { color: var(--accent); font-weight: 700; }
html.mk-v3 .hero-visual { justify-self: end; width: 100%; max-width: 440px; position: relative; }
html.mk-v3 .mk-portrait { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: 50% 16%; border-radius: 28px; box-shadow: var(--shadow-md); }
html.mk-v3 .mk-now { position: absolute; left: -44px; bottom: 36px; background: var(--bg-card); border-radius: 16px; padding: 14px 18px; box-shadow: var(--shadow-md); display: flex; flex-direction: column; gap: 2px; }
html.mk-v3 .mk-now span { font-size: .75rem; color: var(--text-muted); }
html.mk-v3 .mk-now b { font-size: .95rem; color: var(--accent); font-weight: 600; }
@media (max-width: 900px) { html.mk-v3 #hero { background: var(--bg-primary); } html.mk-v3 .hero-visual { justify-self: start; max-width: 340px; } html.mk-v3 .mk-now { left: 12px; } }
""")

# ---------------------------------------------------------------- 4. Swiss (bold type, black/white, safety orange)
V["v4"] = dict(
 short="4  Swiss — bold type",
 name="4 \u2014 Swiss (giant type, black + white, safety orange)",
 fonts="family=Archivo:wdth,wght@62..125,400..900",
 hero="""<img class="mk-portrait" src="/__mock/portrait.jpg" alt="Martin Davidsen">""",
 css="""
html.mk-v4 { --bg-primary:#ffffff; --bg-secondary:#f3f3f1; --bg-card:transparent; --bg-card-hover:transparent; --border:#d4d4d4; --border-light:#0a0a0a;
  --text-primary:#0a0a0a; --text-secondary:#2b2b2b; --text-muted:#666; --accent:#ff4d12; --accent-hover:#e03e05;
  --accent-glow:rgba(255,77,18,.08); --accent-secondary:#ff4d12; --gradient-accent:linear-gradient(#0a0a0a,#0a0a0a);
  --shadow-sm:none; --shadow-md:none; --radius:0px; --radius-sm:0px; --radius-lg:0px; --font:'Archivo', 'Inter', sans-serif; }
html.mk-v4 body { font-family: var(--font); }
html.mk-v4 #navbar, html.mk-v4 #navbar.scrolled { background: #fff; box-shadow: none; border-bottom: 2px solid #0a0a0a; }
html.mk-v4 .logo-monogram { background: var(--accent); border-radius: 0; }
html.mk-v4 .nav-links a { text-transform: uppercase; font-weight: 600; font-size: .78rem; letter-spacing: .04em; color: #0a0a0a; }
html.mk-v4 .section-label { color: #0a0a0a; font-weight: 700; letter-spacing: .06em; border-top: 2px solid #0a0a0a; padding-top: 12px; display: flex; justify-content: space-between; }
html.mk-v4 .section-label::before { content: counter(sec, decimal-leading-zero); color: var(--accent); order: 2; }
html.mk-v4 .contact-single h2 { font-weight: 800; font-size: clamp(2.4rem, 5.4vw, 4.4rem); letter-spacing: -.04em; }
html.mk-v4 .section-title { font-weight: 800; font-size: clamp(2.4rem, 5.4vw, 4.4rem); line-height: .95; letter-spacing: -.04em; max-width: 980px; }
html.mk-v4 .service-card, html.mk-v4 .ai-card, html.mk-v4 .timeline-content, html.mk-v4 .skill-group, html.mk-v4 .beyond-card,
html.mk-v4 .contact-card, html.mk-v4 .service-card--feature { background: transparent; border: 0; border-top: 2px solid #0a0a0a; border-radius: 0;
  box-shadow: none; padding: 16px 0 0; transform: none !important; }
html.mk-v4 .ai-card-icon, html.mk-v4 .beyond-icon, html.mk-v4 .service-feature-icon { display: none; }
html.mk-v4 .service-num { font-family: var(--font); font-size: 2.4rem; font-weight: 800; letter-spacing: -.03em; line-height: 1; }
html.mk-v4 .ai-card h3, html.mk-v4 .service-card h3, html.mk-v4 .timeline-head h3, html.mk-v4 .beyond-card h3 { font-weight: 800; font-size: 1.3rem; letter-spacing: -.02em; line-height: 1.15; }
html.mk-v4 .ai-card:hover h3 { color: var(--accent); }
html.mk-v4 .ai-badge { text-transform: uppercase; font-weight: 700; letter-spacing: .06em; color: #666; }
html.mk-v4 .ai-badge--live { color: #0a0a0a; } html.mk-v4 .ai-badge--live::before { content: "\\25a0  "; color: var(--accent); }
html.mk-v4 .service-tags { text-transform: uppercase; font-size: .68rem; letter-spacing: .06em; font-weight: 600; }
html.mk-v4 .ai-sections { gap: 0; }
html.mk-v4 .ai-section { border: 0; border-top: 2px solid #0a0a0a; border-radius: 0; background: transparent; box-shadow: none; }
html.mk-v4 .ai-section:last-child { border-bottom: 2px solid #0a0a0a; }
html.mk-v4 .ai-cat { padding: 16px 0; color: #0a0a0a; }
html.mk-v4 .ai-cat:hover, html.mk-v4 .ai-cat:focus-visible { background: transparent; color: var(--accent); }
html.mk-v4 .ai-cat-name { font-size: 1.9rem; font-weight: 800; letter-spacing: -.02em; }
html.mk-v4 .ai-cat-count { color: var(--accent); font-weight: 700; font-size: .9rem; align-self: flex-start; }
html.mk-v4 .ai-cat-count::before, html.mk-v4 .ai-cat-count::after { content: ""; }
html.mk-v4 .ai-cat-chevron { color: currentColor; width: 26px; height: 26px; }
html.mk-v4 .ai-section-inner .ai-grid { padding: 6px 0 32px; }
html.mk-v4 .timeline { padding-left: 0; max-width: none; }
html.mk-v4 .timeline::before, html.mk-v4 .timeline-marker { display: none; }
html.mk-v4 .timeline-org { color: var(--accent); text-transform: uppercase; font-weight: 700; letter-spacing: .04em; font-size: .78rem; }
html.mk-v4 .skill-group h3 { color: #0a0a0a; }
html.mk-v4 .client-item { background: transparent; border: 0; }
html.mk-v4 .about-photo { display: none; }
html.mk-v4 .btn { border-radius: 0; text-transform: uppercase; letter-spacing: .04em; font-size: .82rem; }
html.mk-v4 .btn-primary { background: #0a0a0a; box-shadow: none; }
html.mk-v4 .btn-primary:hover { background: var(--accent); box-shadow: none; transform: none; }
html.mk-v4 .btn-outline { border: 2px solid #0a0a0a; }
html.mk-v4 #hero { padding-top: 120px; }
html.mk-v4 .hero-grid { grid-template-columns: repeat(12, 1fr); column-gap: 24px; row-gap: 0; align-items: start; }
html.mk-v4 .hero-text { display: contents; }
html.mk-v4 .hero-eyebrow { grid-column: 1 / -1; grid-row: 1; color: #0a0a0a; text-transform: uppercase; font-weight: 700; font-size: .8rem; letter-spacing: .06em; border-bottom: 2px solid #0a0a0a; padding-bottom: 12px; margin-bottom: 22px; }
html.mk-v4 .hero-name { grid-column: 1 / -1; grid-row: 2; font-size: clamp(3.2rem, 11.2vw, 10.2rem); line-height: .86; font-weight: 800; font-stretch: 112%; text-transform: uppercase; letter-spacing: -.045em; margin-bottom: 30px; }
html.mk-v4 .hero-role { grid-column: 1 / 5; grid-row: 3; font-size: 1.55rem; font-weight: 800; color: var(--accent); line-height: 1.15; letter-spacing: -.02em; }
html.mk-v4 .hero-sub { grid-column: 5 / 9; grid-row: 3; font-size: 1rem; margin: 0; }
html.mk-v4 .hero-actions { grid-column: 5 / 9; grid-row: 4; margin: 24px 0 0; }
html.mk-v4 .hero-stats { grid-column: 1 / 5; grid-row: 4; border-top: 2px solid #0a0a0a; margin-top: 24px; gap: 28px; }
html.mk-v4 .hero-stat-num { font-size: 2.2rem; }
html.mk-v4 .hero-visual { grid-column: 10 / 13; grid-row: 3 / 5; position: relative; z-index: 0; }
html.mk-v4 .hero-visual::before { content: ''; position: absolute; inset: 14px -14px -14px 14px; background: var(--accent); z-index: -1; }
html.mk-v4 .mk-portrait { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; object-position: 50% 20%; filter: grayscale(1) contrast(1.12); }
@media (max-width: 900px) {
  html.mk-v4 .hero-grid { grid-template-columns: 1fr; row-gap: 0; }
  html.mk-v4 .hero-eyebrow, html.mk-v4 .hero-name, html.mk-v4 .hero-role, html.mk-v4 .hero-sub, html.mk-v4 .hero-actions,
  html.mk-v4 .hero-stats, html.mk-v4 .hero-visual { grid-column: 1; grid-row: auto; }
  html.mk-v4 .hero-sub { margin-top: 16px; }
  html.mk-v4 .hero-visual { max-width: 240px; margin-top: 36px; }
}
""")

INJECT = """([cls, css, fontsUrl, heroHtml]) => {
  if (fontsUrl) { const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = fontsUrl; document.head.appendChild(l); }
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);
  document.documentElement.classList.add('mk', cls);
  if (heroHtml) document.querySelector('.hero-visual').innerHTML = heroHtml;
}"""
PREP = """async () => {
  document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager');
  document.querySelectorAll('.fade-in').forEach(e => e.classList.add('visible'));
  const b = document.querySelector('[aria-controls=aisec-products]'); if (b && b.getAttribute('aria-expanded') !== 'true') b.click();
  for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
  await document.fonts.ready;
  await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
  window.scrollTo(0, 0);
}"""

def label(img, text, h=46):
    f = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    c = Image.new("RGB", (img.width, img.height + h), "#e2e8f0")
    ImageDraw.Draw(c).text((6, 8), text, fill="#0f172a", font=f); c.paste(img, (0, h)); return c

def grid(cells, cols, pad=20, bg="#cbd5e1"):
    w = max(c.width for c in cells); h = max(c.height for c in cells); rows = (len(cells) + cols - 1) // cols
    s = Image.new("RGB", (cols * w + (cols + 1) * pad, rows * h + (rows + 1) * pad), bg)
    for i, c in enumerate(cells):
        s.paste(c, (pad + (i % cols) * (w + pad), pad + (i // cols) * (h + pad)))
    return s

def run(out, ONLY):
    heroes, mobiles = [], []
    with sync_playwright() as p:
        br = p.chromium.launch()
        def page(w, h):
            ctx = br.new_context(viewport={"width": w, "height": h}, reduced_motion="reduce")
            pg = ctx.new_page()
            pg.route("**/__mock/portrait.jpg", lambda r: r.fulfill(path=PORTRAIT, content_type="image/jpeg"))
            return pg
        # baseline: current site (local = what's live)
        for key in ["current"] + [k for k in V if not ONLY or k in ONLY]:
            v = V.get(key)
            for (w, h, tag) in [(1280, 820, "desk"), (375, 812, "mob")]:
                pg = page(w, h); pg.goto(URL); pg.wait_for_timeout(400)
                if v: pg.evaluate(INJECT, [f"mk-{key}", COMMON + v["css"], GF + v["fonts"] + "&display=swap", v["hero"]])
                pg.evaluate(PREP); pg.wait_for_timeout(900)
                sw = pg.evaluate("document.documentElement.scrollWidth")
                pg.screenshot(path=out / f"{key}-{tag}-hero.png")
                if tag == "desk":
                    pg.screenshot(path=out / f"{key}-desk-full.png", full_page=True)
                print(key, tag, "scrollWidth", sw)
                pg.context.close()
            name = v["short"] if v else "Current portfolio (live)"
            heroes.append(label(Image.open(out / f"{key}-desk-hero.png").convert("RGB").resize((640, 410)), name))
            mobiles.append(label(Image.open(out / f"{key}-mob-hero.png").convert("RGB"), key if not v else v["short"].split(" —")[0], 40))
            if v:  # full page, halved, folded into two columns
                full = Image.open(out / f"{key}-desk-full.png").convert("RGB"); full = full.resize((full.width // 2, full.height // 2))
                half = (full.height + 1) // 2
                a, b = full.crop((0, 0, full.width, half)), full.crop((0, half, full.width, 2 * half))
                sheet = grid([a, b], 2)
                label(sheet, v["name"]).save(out / f"{key}-page.png")
        br.close()
    apex = pathlib.Path("cmp/apex-full.png")
    if apex.exists():
        heroes.insert(0, label(Image.open(apex).convert("RGB").crop((0, 0, 1280, 820)).resize((640, 410)), "agentas.net (apex, live)"))
    grid(heroes, 2).save(out / "overview-heroes.png")
    grid(mobiles, len(mobiles)).save(out / "overview-mobile.png")
    print("done")

FILES = {"v1": "1-field-notes.html", "v2": "2-control-room.html", "v3": "3-nordic.html", "v4": "4-swiss.html"}
SWITCH_CSS = """
.mk-switch { position: fixed; left: 12px; bottom: 12px; z-index: 3000; display: flex; flex-wrap: wrap; align-items: center; gap: 2px;
  padding: 6px; background: rgba(17,17,17,.9); border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,.3); font: 600 12px/1.2 system-ui, sans-serif; }
.mk-switch a { color: #fff; padding: 6px 9px; border-radius: 5px; text-decoration: none; }
.mk-switch a:hover { background: rgba(255,255,255,.15); }
.mk-switch a[aria-current] { background: #fff; color: #111; }
"""

def build_html(dest):
    """Standalone mockup pages that open straight from disk (file://): the real index.html + the theme CSS,
    with site assets referenced from the repo root and Inter embedded (Firefox blocks file:// fonts
    loaded from a parent folder)."""
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy(PORTRAIT, dest / "portrait.jpg")
    src = (REPO / "index.html").read_text(encoding="utf-8")
    src = re.sub(r'<link rel="preload" as="font"[^>]*>\s*', "", src)
    src = re.sub(r'(?<=["\s,])(images/|fonts/|styles\.css|script\.js|favicon|apple-touch-icon)', r"../../\1", src)
    inter = base64.b64encode((REPO / "fonts" / "inter-latin-var.woff2").read_bytes()).decode()
    face = ("@font-face { font-family: 'Inter'; font-style: normal; font-weight: 300 800; font-display: swap;"
            f" src: url(data:font/woff2;base64,{inter}) format('woff2'); }}")
    for key, v in V.items():
        links = "".join(f'<a href="{f}"{" aria-current=\"page\"" if k == key else ""}>{V[k]["short"].split(" —")[0]}</a>'
                        for k, f in FILES.items())
        switch = f'<nav class="mk-switch" aria-label="Mockups"><a href="index.html">All</a>{links}</nav>\n'
        page = src.replace('<html lang="en">', f'<html lang="en" class="mk mk-{key}">', 1)
        page = re.sub(r"<title>", f"<title>Mockup {v['short'].split(' —')[0].strip()} · ", page, count=1)
        page = page.replace("</head>", f'<link rel="stylesheet" href="{GF}{v["fonts"]}&display=swap">\n'
                                       f"<style>\n{face}\n{COMMON}{v['css']}{SWITCH_CSS}</style>\n</head>", 1)
        page = re.sub(r'(<figure class="hero-visual">).*?(</figure>)',
                      lambda m: m.group(1) + v["hero"].replace("/__mock/portrait.jpg", "portrait.jpg") + m.group(2),
                      page, count=1, flags=re.S)
        page = page.replace("</body>", switch + "</body>", 1)
        (dest / FILES[key]).write_text(page, encoding="utf-8", newline="\n")
    cards = "".join(
        f'<a class="card" href="{FILES[k]}"><img src="hero-{k}.png" alt=""><b>{v["short"]}</b></a>'
        for k, v in V.items())
    (dest / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Portfolio restyle mockups</title>
<style>
:root {{ --bg: #f4f5f7; --fg: #111827; --muted: #5b6270; --card: #fff; --line: #e3e6eb; }}
body {{ margin: 0; font: 16px/1.5 system-ui, sans-serif; background: var(--bg); color: var(--fg); }}
main {{ max-width: 1120px; margin: 0 auto; padding: 40px 16px; }}
h1 {{ margin: 0 0 6px; font-size: 1.6rem; }} p {{ margin: 0 0 28px; color: var(--muted); }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
.card {{ display: block; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; color: inherit; text-decoration: none; }}
.card:hover {{ border-color: #9aa3b2; }} .card img {{ display: block; width: 100%; height: auto; border-bottom: 1px solid var(--line); }}
.card b {{ display: block; padding: 12px 14px; }}
a {{ color: #1d4ed8; }}
</style></head><body><main>
<h1>Portfolio restyle mockups</h1>
<p>Same page, same wording, four looks. Open one, then use the switcher bottom-left to jump between them.
Compare with the <a href="https://martindavidsen.cc">live portfolio</a> and <a href="https://agentas.net">agentas.net</a>.</p>
<div class="grid">{cards}</div>
</main></body></html>
""", encoding="utf-8", newline="\n")
    print("wrote", sorted(p.name for p in dest.iterdir()))

if __name__ == "__main__":
    if sys.argv[1:2] == ["--html"]:
        build_html(REPO / "drafts" / "mockups")
    else:
        o = pathlib.Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
        run(o, sys.argv[2:])
