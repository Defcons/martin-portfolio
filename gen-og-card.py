# -*- coding: utf-8 -*-
"""Generate the martindavidsen.cc Open Graph share card (images/og-card.jpg).

Photo-forward card: circular headshot left; name, role (two lines), "Founder of
Agentas AS" and the domain right, on the site's own :root palette from styles.css
(sand + fjord green since the 2026-09 restyle), with --accent as a photo ring and
an underline under the name, and the name in the site's display face.
Final image 1200x630 (Open Graph spec).

CRISPNESS: LinkedIn shows the card at ~520px wide from its own low-res,
re-compressed copy, so everything must survive a ~45% downscale plus a lossy
re-encode (2026-09-28: the first green card, with 31px secondary lines and green
role text, came out blurry there). Rules:
- render SUPERSAMPLED (3x -> LANCZOS) on flat backgrounds;
- no text below ~40px on the 1200px canvas, and bold weights;
- TEXT IN DARK INK, not the accent: JPEG chroma subsampling smears coloured
  strokes; keep colour for big shapes (ring, underline);
- save JPEG q95 with 4:4:4 chroma (subsampling=0) so our generation adds no smear.
Eyeball a ~520px, low-quality JPEG of the output before shipping.

Headshot source = images/martin-400.jpg (the site's own headshot crop; ~1:1
with the final circle). Fonts (gitignored _assets/, made from the site's own
woff2 files with fontTools: TTFont(woff2).flavor = None; .save(ttf)):
_assets/inter-var.ttf (fonts/inter-latin-var.woff2) and _assets/bricolage.ttf
(fonts/bricolage-latin-var.woff2).
Root *.py files are NOT served (Dockerfile COPYs an explicit file list).

og:image/twitter:image/JSON-LD reference the card as `?v=N`; a regen = bump N in
index.html (no Cloudflare purge), then re-scrape in LinkedIn's Post Inspector.

    python gen-og-card.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
TEXT_FONT = os.path.join(ROOT, '_assets', 'inter-var.ttf')
DISPLAY_FONT = os.path.join(ROOT, '_assets', 'bricolage.ttf')
PHOTO = os.path.join(ROOT, 'images', 'martin-400.jpg')
OUT = os.path.join(ROOT, 'images', 'og-card.jpg')

# styles.css :root tokens.
BG = (251, 249, 245)          # --bg-primary
BG2 = (241, 235, 224)         # --bg-secondary
INK = (20, 33, 29)            # --text-primary
SECONDARY = (60, 73, 68)      # --text-secondary
ACCENT = (30, 91, 77)         # --accent            #1e5b4d
BORDER = (230, 222, 208)      # --border

SS = 3
W, H = 1200 * SS, 630 * SS


def inter(s, weight):
    f = ImageFont.truetype(TEXT_FONT, s * SS)
    f.set_variation_by_axes([weight])        # axes: wght
    return f


def display(s, weight=700):
    f = ImageFont.truetype(DISPLAY_FONT, s * SS)
    f.set_variation_by_axes([96, weight])    # axes: opsz, wght
    return f


img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)
accent = Image.new('RGB', (W, H), ACCENT)

# --- flat --bg-secondary panel behind the photo ---
PANEL = 450 * SS
d.rectangle([0, 0, PANEL, H], fill=BG2)
d.line([(PANEL, 0), (PANEL, H)], fill=BORDER, width=1 * SS)

# --- circular headshot, accent ring ---
CIRCLE = 340 * SS
cx, cy = PANEL // 2, H // 2
px, py = cx - CIRCLE // 2, cy - CIRCLE // 2
RING = 10 * SS

ring_mask = Image.new('L', (W, H), 0)
rd = ImageDraw.Draw(ring_mask)
rd.ellipse([px - RING, py - RING, px + CIRCLE + RING, py + CIRCLE + RING], fill=255)
rd.ellipse([px, py, px + CIRCLE, py + CIRCLE], fill=0)
img.paste(accent, (0, 0), ring_mask)

photo = Image.open(PHOTO).convert('RGB').resize((CIRCLE, CIRCLE), Image.LANCZOS)
photo_mask = Image.new('L', (CIRCLE, CIRCLE), 0)
ImageDraw.Draw(photo_mask).ellipse([0, 0, CIRCLE, CIRCLE], fill=255)
img.paste(photo, (px, py), photo_mask)
d = ImageDraw.Draw(img)

# --- text block, right ---
TX = 500 * SS
RIGHT = W - 48 * SS
name, name_px = 'Martin Davidsen', 92
while d.textlength(name, font=display(name_px)) > RIGHT - TX:
    name_px -= 1
name_f = display(name_px)
d.text((TX, 176 * SS), name, font=name_f, fill=INK, anchor='ls')
name_w = d.textlength(name, font=name_f)

bar_mask = Image.new('L', (W, H), 0)
ImageDraw.Draw(bar_mask).rounded_rectangle([TX, 198 * SS, TX + name_w, 210 * SS], radius=6 * SS, fill=255)
img.paste(accent, (0, 0), bar_mask)
d = ImageDraw.Draw(img)

role_f = inter(50, 700)
d.text((TX, 290 * SS), 'AI Architect &', font=role_f, fill=INK, anchor='ls')
d.text((TX, 350 * SS), 'Software Engineer', font=role_f, fill=INK, anchor='ls')
d.text((TX, 432 * SS), 'Founder of Agentas AS', font=inter(42, 550), fill=SECONDARY, anchor='ls')
d.text((TX, 522 * SS), 'martindavidsen.cc', font=inter(42, 700), fill=INK, anchor='ls')

img = img.resize((1200, 630), Image.LANCZOS)
img.save(OUT, quality=95, subsampling=0, optimize=True)
print('wrote', OUT, '(1200x630, rendered at %dx)' % SS)
