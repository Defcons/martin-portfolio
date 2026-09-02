# -*- coding: utf-8 -*-
"""Generate the martindavidsen.cc Open Graph share card (images/og-card.jpg).

Photo-forward refresh of the original hand-made card: same layout (circular
headshot left, name/role/location right) rebuilt on the site's own :root palette
from styles.css, with the --gradient-accent (#2563eb -> #06b6d4) as a photo ring
+ an underline under the name. Final image 1200x630 (Open Graph spec).

CRISPNESS (learned on the agentas card, 2026-09-02): LinkedIn downscales the
card to ~500px + re-encodes, so render SUPERSAMPLED (3x -> LANCZOS), keep the
background flat, use bold high-contrast type. Eyeball a ~523x274 JPEG of the
output before shipping - that's what platforms actually show.

Headshot source = images/martin-400.jpg (the site's own headshot crop; ~1:1
with the final circle so the supersample roundtrip is lossless). Font =
_assets/inter.ttf (gitignored; copy of the agentas-sites ogcard-gen font).
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
PHOTO = os.path.join(ROOT, 'images', 'martin-400.jpg')
OUT = os.path.join(ROOT, 'images', 'og-card.jpg')

# styles.css :root tokens.
BG = (255, 255, 255)          # --bg-primary
BG2 = (243, 246, 252)         # --bg-secondary
INK = (15, 23, 42)            # --text-primary
SECONDARY = (58, 66, 86)      # --text-secondary
MUTED = (92, 103, 128)        # --text-muted
ACCENT = (37, 99, 235)        # --accent            #2563eb
GRAD_START = (37, 99, 235)    # --gradient-accent start
GRAD_END = (6, 182, 212)      # --gradient-accent end #06b6d4
BORDER = (229, 233, 242)      # --border

SS = 3
W, H = 1200 * SS, 630 * SS
inter = lambda s: ImageFont.truetype(FONT, s * SS)


def diag_gradient(c1, c2):
    """Full-canvas 135deg linear gradient c1->c2 (--gradient-accent direction)."""
    g = Image.new('RGB', (W, H), c1)
    gd = ImageDraw.Draw(g)
    diag = W + H
    for i in range(0, diag, SS):
        t = i / diag
        gd.line([(0, i), (i, 0)], fill=tuple(int(c1[k] + (c2[k] - c1[k]) * t) for k in range(3)), width=SS)
    return g


img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)
grad = diag_gradient(GRAD_START, GRAD_END)

# --- soft --bg-secondary wash on the photo half (flat, no fine texture) ---
d.rectangle([0, 0, 500 * SS, H], fill=BG2)
d.line([(500 * SS, 0), (500 * SS, H)], fill=BORDER, width=1 * SS)

# --- circular headshot, gradient ring ---
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
name_f = inter(74)
d.text((TX, 232 * SS), 'Martin Davidsen', font=name_f, fill=INK, anchor='ls', stroke_width=2 * SS)
name_w = d.textlength('Martin Davidsen', font=name_f)

# gradient underline under the name (site's --gradient-accent motif)
uy = 254 * SS
bar_mask = Image.new('L', (W, H), 0)
ImageDraw.Draw(bar_mask).rounded_rectangle([TX, uy, TX + name_w, uy + 9 * SS], radius=4 * SS, fill=255)
img.paste(grad, (0, 0), bar_mask)
d = ImageDraw.Draw(img)

d.text((TX, 336 * SS), 'Software & AI Engineer', font=inter(44), fill=ACCENT, anchor='ls', stroke_width=1 * SS)
d.text((TX, 404 * SS), 'Founder of Agentas AS', font=inter(31), fill=SECONDARY, anchor='ls')
d.text((TX, 458 * SS), 'Stavanger, Norway', font=inter(31), fill=MUTED, anchor='ls')
d.text((TX, 540 * SS), 'martindavidsen.cc', font=inter(30), fill=INK, anchor='ls', stroke_width=1 * SS)

img = img.resize((1200, 630), Image.LANCZOS)
img.save(OUT, quality=92, optimize=True)
print('wrote', OUT, '(1200x630, rendered at %dx)' % SS)
