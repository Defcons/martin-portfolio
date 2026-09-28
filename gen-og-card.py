# -*- coding: utf-8 -*-
"""Generate the martindavidsen.cc Open Graph share card (images/og-card.jpg).

Photo-forward card: circular headshot left, name/role/location right, on the
site's own :root palette from styles.css (sand + fjord green since the 2026-09
restyle), with --accent as a photo ring + an underline under the name and the
name set in the site's display face. Final image 1200x630 (Open Graph spec).

CRISPNESS (learned on the agentas card, 2026-09-02): LinkedIn downscales the
card to ~500px + re-encodes, so render SUPERSAMPLED (3x -> LANCZOS), keep the
background flat, use bold high-contrast type. Eyeball a ~523x274 JPEG of the
output before shipping - that's what platforms actually show.

Headshot source = images/martin-400.jpg (the site's own headshot crop; ~1:1
with the final circle so the supersample roundtrip is lossless). Fonts =
_assets/inter.ttf (gitignored; copy of the agentas-sites ogcard-gen font) and
_assets/bricolage.ttf (gitignored; fonts/bricolage-latin-var.woff2 decompressed
with fontTools: TTFont(woff2).flavor = None; .save(ttf)).
Root *.py files are NOT served (Dockerfile COPYs an explicit file list).

og-card.jpg is UNVERSIONED in the head by default and CF-edge-cached - this
refresh switched the og:image/twitter:image/JSON-LD refs to `?v=N` so a regen
just bumps N (no Cloudflare purge). Overwrite = bump N in index.html.

    python gen-og-card.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(ROOT, '_assets', 'inter.ttf')
DISPLAY_FONT = os.path.join(ROOT, '_assets', 'bricolage.ttf')
PHOTO = os.path.join(ROOT, 'images', 'martin-400.jpg')
OUT = os.path.join(ROOT, 'images', 'og-card.jpg')

# styles.css :root tokens.
BG = (251, 249, 245)          # --bg-primary
BG2 = (241, 235, 224)         # --bg-secondary
INK = (20, 33, 29)            # --text-primary
SECONDARY = (60, 73, 68)      # --text-secondary
MUTED = (102, 115, 109)       # --text-muted
ACCENT = (30, 91, 77)         # --accent            #1e5b4d
BORDER = (230, 222, 208)      # --border

SS = 3
W, H = 1200 * SS, 630 * SS
inter = lambda s: ImageFont.truetype(FONT, s * SS)


def display(s, weight=700):
    f = ImageFont.truetype(DISPLAY_FONT, s * SS)
    f.set_variation_by_axes([96, weight])   # axes: opsz, wght
    return f


img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)
grad = Image.new('RGB', (W, H), ACCENT)

# --- soft --bg-secondary wash on the photo half (flat, no fine texture) ---
d.rectangle([0, 0, 500 * SS, H], fill=BG2)
d.line([(500 * SS, 0), (500 * SS, H)], fill=BORDER, width=1 * SS)

# --- circular headshot, accent ring ---
CIRCLE = 380 * SS
cx, cy = 250 * SS, H // 2                      # circle center
px, py = cx - CIRCLE // 2, cy - CIRCLE // 2    # photo top-left
RING = 7 * SS

ring_mask = Image.new('L', (W, H), 0)
rd = ImageDraw.Draw(ring_mask)
rd.ellipse([px - RING, py - RING, px + CIRCLE + RING, py + CIRCLE + RING], fill=255)
rd.ellipse([px, py, px + CIRCLE, py + CIRCLE], fill=0)
img.paste(grad, (0, 0), ring_mask)

photo = Image.open(PHOTO).convert('RGB').resize((CIRCLE, CIRCLE), Image.LANCZOS)
photo_mask = Image.new('L', (CIRCLE, CIRCLE), 0)
ImageDraw.Draw(photo_mask).ellipse([0, 0, CIRCLE, CIRCLE], fill=255)
img.paste(photo, (px, py), photo_mask)
d = ImageDraw.Draw(img)

# --- text block, right ---
TX = 566 * SS
name_f = display(78)
d.text((TX, 232 * SS), 'Martin Davidsen', font=name_f, fill=INK, anchor='ls')
name_w = d.textlength('Martin Davidsen', font=name_f)

# accent underline under the name
uy = 254 * SS
bar_mask = Image.new('L', (W, H), 0)
ImageDraw.Draw(bar_mask).rounded_rectangle([TX, uy, TX + name_w, uy + 9 * SS], radius=4 * SS, fill=255)
img.paste(grad, (0, 0), bar_mask)
d = ImageDraw.Draw(img)

role = 'AI Architect & Software Engineer'
role_px = 44
while d.textlength(role, font=inter(role_px)) > W - TX - 56 * SS:  # shrink to fit the right panel
    role_px -= 1
d.text((TX, 336 * SS), role, font=inter(role_px), fill=ACCENT, anchor='ls', stroke_width=1 * SS)
d.text((TX, 404 * SS), 'Founder of Agentas AS', font=inter(31), fill=SECONDARY, anchor='ls')
d.text((TX, 458 * SS), 'Stavanger, Norway', font=inter(31), fill=MUTED, anchor='ls')
d.text((TX, 540 * SS), 'martindavidsen.cc', font=inter(30), fill=INK, anchor='ls', stroke_width=1 * SS)

img = img.resize((1200, 630), Image.LANCZOS)
img.save(OUT, quality=92, optimize=True)
print('wrote', OUT, '(1200x630, rendered at %dx)' % SS)
