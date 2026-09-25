"""Preview-only hero variants for martindavidsen.cc, rendered by DOM injection into the
local site. Nothing here touches the site files.
Usage: from the repo root, `python -m http.server 8765 --bind 127.0.0.1`, then
       `python drafts/hero-variants.py <outdir>` (outdir outside the repo)."""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
URL = "http://127.0.0.1:8765/"
PORTRAIT = r"C:\Dev\career\cv\martin@2x.jpg"
COMPOSITE = r"C:\Dev\agentas\agentas-sites\apex\images\hero-products.webp"

TEXT = """
<div class="hv-text">
  <p class="hv-eyebrow"><span data-en="Stavanger, Norway" data-no="Stavanger, Norge">Stavanger, Norway</span> · <span data-en="Founder of Agentas AS" data-no="Gründer av Agentas AS">Founder of Agentas AS</span></p>
  <h1 class="hv-name">Martin Davidsen</h1>
  <p class="hv-role" data-en="Software &amp; AI Engineer" data-no="Programvare- og AI-ingeniør">Software &amp; AI Engineer</p>
  <p class="hv-sub">From electrician, to offshore technology for oil production, to critical infrastructure projects onshore, to AI-driven applications — fifteen years turning hands-on curiosity into systems people depend on.</p>
  <div class="hv-actions">
    <a href="#work" class="btn btn-primary">See My Work</a>
    <a href="#contact" class="btn btn-outline">Get in Touch</a>
  </div>
  <div class="hv-stats">
    <div class="hv-stat"><b>15+</b><span>years in tech</span></div>
    <div class="hv-stat"><b>9+</b><span>years engineering</span></div>
    <div class="hv-stat"><b>20+</b><span>projects shipped</span></div>
  </div>
</div>"""

VISUAL = {
 "A": """<figure class="hv-portrait"><img src="/__mock/portrait.jpg" alt="Martin Davidsen"></figure>""",
 "B": """<figure class="hv-work">
   <img class="hv-composite" src="/__mock/composite.webp" alt="Agentas Consult and Aurly">
   <img class="hv-avatar" src="/__mock/portrait.jpg" alt="">
   <figcaption>Agentas Consult and Aurly — products I build and run. Demo data shown.</figcaption>
 </figure>""",
 "C": """<figure class="hv-collage">
   <img class="hv-c-portrait" src="/__mock/portrait.jpg" alt="Martin Davidsen">
   <img class="hv-c-shot hv-c-shot1" src="images/agentas-consult.webp?v=1" alt="">
   <img class="hv-c-shot hv-c-shot2" src="images/aurly.webp?v=1" alt="">
 </figure>""",
}

CSS = """
#hero.hv { min-height: auto; display: block; padding: 136px 0 88px; overflow: hidden; }
#hero.hv::before, #hero.hv .hero-bg-grid, #hero.hv .hero-scroll { display: none; }
.hv-grid { max-width: var(--max-width); margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: 1.08fr 0.92fr; gap: 72px; align-items: center; }
.hv-grid > * { min-width: 0; }
.hv-eyebrow { font-size: 0.95rem; font-weight: 500; color: var(--text-muted); margin-bottom: 18px; }
.hv-name { font-size: clamp(2.6rem, 5.4vw, 4.4rem); font-weight: 800; letter-spacing: -0.035em; line-height: 1.04; margin-bottom: 12px; text-wrap: balance; }
.hv-role { font-size: clamp(1.25rem, 2.2vw, 1.6rem); font-weight: 600; color: var(--accent); letter-spacing: -0.01em; margin-bottom: 22px; }
.hv-sub { font-size: 1.08rem; line-height: 1.75; color: var(--text-secondary); max-width: 540px; margin-bottom: 34px; }
.hv-actions { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 44px; }
.hv-stats { display: flex; gap: 44px; padding-top: 24px; border-top: 1px solid var(--border); max-width: 540px; }
.hv-stat b { display: block; font-size: 1.8rem; font-weight: 800; letter-spacing: -0.02em; line-height: 1.1; color: var(--text-primary); }
.hv-stat span { font-size: 0.88rem; color: var(--text-muted); }
figure { margin: 0; }
/* A: portrait split */
.hv-portrait { position: relative; justify-self: end; width: 100%; max-width: 430px; }
.hv-portrait::before { content: ''; position: absolute; inset: 28px -28px -28px 28px; border-radius: 24px; background: var(--bg-secondary); border: 1px solid var(--border); z-index: -1; }
.hv-portrait img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: 50% 18%; border-radius: 20px; box-shadow: 0 30px 60px -24px rgba(15, 23, 42, 0.35); }
/* B: work-forward composite + avatar */
.hv-work { position: relative; }
.hv-composite { width: 100%; filter: drop-shadow(0 24px 40px rgba(15, 23, 42, 0.14)); }
.hv-avatar { position: absolute; left: -18px; bottom: 44px; width: 104px; height: 104px; border-radius: 50%; object-fit: cover; object-position: 50% 20%; border: 4px solid #fff; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.25); }
.hv-work figcaption { margin-top: 10px; padding-left: 104px; font-size: 0.85rem; color: var(--text-muted); }
/* C: portrait + work collage */
.hv-collage { position: relative; justify-self: end; width: 100%; max-width: 480px; padding: 44px 36px 64px 64px; }
.hv-c-portrait { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: 50% 18%; border-radius: 20px; box-shadow: 0 30px 60px -24px rgba(15, 23, 42, 0.35); }
.hv-c-shot { position: absolute; border-radius: 10px; border: 1px solid var(--border); background: #fff; box-shadow: 0 18px 40px -12px rgba(15, 23, 42, 0.35); }
.hv-c-shot1 { width: 52%; top: 96px; left: 0; }
.hv-c-shot2 { width: 64%; right: 0; bottom: 0; }
@media (max-width: 900px) {
  #hero.hv { padding: 104px 0 56px; }
  .hv-grid { grid-template-columns: 1fr; gap: 44px; }
  .hv-portrait, .hv-collage { justify-self: start; max-width: 340px; }
  .hv-portrait::before { inset: 16px -16px -16px 16px; }
  .hv-collage { padding: 28px 20px 44px 40px; }
  .hv-c-shot1 { top: 64px; }
  .hv-stats { gap: 28px; }
  .hv-avatar { width: 76px; height: 76px; left: -6px; bottom: 36px; }
  .hv-work figcaption { padding-left: 80px; }
}
"""

INJECT = """([css, html]) => {
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);
  const h = document.getElementById('hero'); h.classList.add('hv');
  h.innerHTML = '<div class="hv-grid">' + html + '</div>';
}"""

def route(page):
    page.route("**/__mock/portrait.jpg", lambda r: r.fulfill(path=PORTRAIT, content_type="image/jpeg"))
    page.route("**/__mock/composite.webp", lambda r: r.fulfill(path=COMPOSITE, content_type="image/webp"))

shots = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for vw, vh, tag in [(1280, 820, "desktop"), (375, 812, "mobile")]:
        pg = b.new_page(viewport={"width": vw, "height": vh}, device_scale_factor=1)
        route(pg)
        pg.goto(URL); pg.wait_for_timeout(500)
        f = out / f"hero-current-{tag}.png"
        pg.screenshot(path=f, full_page=False)
        shots.append(("Current", tag, f))
        for key, vis in VISUAL.items():
            pg.goto(URL); pg.wait_for_timeout(300)
            pg.evaluate(INJECT, [CSS, TEXT + vis])
            pg.wait_for_timeout(700)
            box = pg.eval_on_selector("#hero", "e => { const r = e.getBoundingClientRect(); return [r.height, document.documentElement.scrollWidth]; }")
            f = out / f"hero-{key}-{tag}.png"
            clip_h = min(int(box[0]), 1500 if tag == "mobile" else vh)
            pg.screenshot(path=f, clip={"x": 0, "y": 0, "width": vw, "height": clip_h}, full_page=True)
            print(tag, key, "hero height", int(box[0]), "scrollWidth", box[1])
            shots.append((key, tag, f))
        pg.close()
    b.close()

# contact sheet of the desktop shots (current + A/B/C), 2x2
font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
desk = [s for s in shots if s[1] == "desktop"]
ims = [Image.open(s[2]).convert("RGB") for s in desk]
w, h = ims[0].size
pad, lab = 24, 50
sheet = Image.new("RGB", (2 * w + 3 * pad, 2 * (h + lab) + 3 * pad), "#e2e8f0")
names = {"Current": "Current (live)", "A": "A — Portrait split", "B": "B — Work-forward (products + avatar)", "C": "C — Portrait + work collage"}
for i, (s, im) in enumerate(zip(desk, ims)):
    x = pad + (i % 2) * (w + pad); y = pad + (i // 2) * (h + lab + pad)
    ImageDraw.Draw(sheet).text((x, y + 6), names[s[0]], fill="#0f172a", font=font)
    sheet.paste(im.resize((w, h)), (x, y + lab))
sheet = sheet.resize((sheet.width // 2 * 2 // 2, sheet.height // 2 * 2 // 2))
sheet.save(out / "hero-variants-desktop.png")
mob = [Image.open(s[2]).convert("RGB") for s in shots if s[1] == "mobile"]
mh = max(m.height for m in mob)
ms = Image.new("RGB", (len(mob) * (375 + pad) + pad, mh + lab + 2 * pad), "#e2e8f0")
for i, (s, m) in enumerate(zip([s for s in shots if s[1] == "mobile"], mob)):
    x = pad + i * (375 + pad)
    ImageDraw.Draw(ms).text((x, pad), s[0], fill="#0f172a", font=font)
    ms.paste(m, (x, pad + lab))
ms.save(out / "hero-variants-mobile.png")
print("sheets written")
