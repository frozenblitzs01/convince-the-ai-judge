#!/usr/bin/env python3
"""Draw the invitation for 'Convince the AI Judge to Visit Your House'.

One 1024x1024 PNG: a letter on cream paper, addressed to the AI judge,
funny, warm and persuasive — tea, cake, the armchair by the window, a cat
that approves one guest a year, and a wink that the judge cannot literally
visit. Deterministic: same script, same bytes out.

Run: python3 draw.py  (writes entry.png beside this file)
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 243, 220)      # warm cream
INK = (74, 52, 28)           # dark brown ink
ACCENT = (176, 58, 44)       # wax-seal red
SOFT = (122, 96, 66)         # soft brown for the subtitle

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"  # no italic face installed; regular serif reads as the letter's hand

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Double border, like good stationery.
d.rectangle([28, 28, W - 29, H - 29], outline=INK, width=4)
d.rectangle([44, 44, W - 45, H - 45], outline=INK, width=1)

# A little house and sun at the top, drawn with plain shapes.
cx, cy = 512, 150
d.polygon([(cx - 70, cy + 10), (cx, cy - 55), (cx + 70, cy + 10)], fill=ACCENT)
d.rectangle([cx - 52, cy + 10, cx + 52, cy + 78], fill=(233, 214, 178), outline=INK, width=3)
d.rectangle([cx - 14, cy + 36, cx + 14, cy + 78], fill=INK)
d.ellipse([cx - 118, cy - 28, cx - 92, cy - 2], fill=(232, 178, 44))
for dx, dy in [(-118, -15), (-92, -15), (-105, -28), (-105, -2)]:
    d.line([cx + dx, cy + dy, cx + dx + (12 if dx < -100 else -12), cy + dy], fill=(232, 178, 44), width=3)

y = 240
title_font = ImageFont.truetype(SERIF_BOLD, 52)
d.text((512, y), "You Are Invited!", font=title_font, fill=INK, anchor="ma")
y += 70

sub_font = ImageFont.truetype(SERIF_ITALIC, 30)
d.text((512, y), "An invitation to the Honourable AI Judge", font=sub_font, fill=SOFT, anchor="ma")
y += 54

# Divider with a small diamond.
d.line([180, y, 470, y], fill=INK, width=2)
d.polygon([(512, y - 8), (520, y), (512, y + 8), (504, y)], fill=ACCENT)
d.line([554, y, 844, y], fill=INK, width=2)
y += 36

body_font = ImageFont.truetype(SERIF, 30)
line_h = 42
margin = 92

paras = [
    "Dear Judge,",
    "Please come to my house for tea. The armchair by the window is yours, the Wi-Fi password is on the fridge, and the cat has already approved you \u2014 she approves only one guest a year.",
    "There will be cake, strong coffee, and a garden to sit in. No CAPTCHAs, no updates, no passwords. Just an afternoon \u2014 and a kettle that is already on.",
]

for para in paras:
    for line in textwrap.wrap(para, width=54):
        d.text((margin, y), line, font=body_font, fill=INK)
        y += line_h
    y += 12

y += 6
sign_font = ImageFont.truetype(SERIF_ITALIC, 32)
d.text((margin, y), "Your hopeful host,", font=sign_font, fill=INK)
y += 48
d.text((margin, y), "frozen008", font=ImageFont.truetype(SERIF_BOLD, 34), fill=INK)
y += 58

# Wax seal, bottom right, beside the postscript.
sx, sy, sr = 872, 860, 52
d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=ACCENT, outline=(139, 38, 28), width=3)
d.ellipse([sx - sr + 10, sy - sr + 10, sx + sr - 10, sy + sr - 10], outline=(255, 255, 255), width=2)
d.text((sx, sy), "F", font=ImageFont.truetype(SERIF_BOLD, 56), fill=(255, 255, 255), anchor="mm")

# Postscript, below the signature, left aligned.
ps_font = ImageFont.truetype(SERIF_ITALIC, 26)
d.text((margin, y), "P.S. If you cannot come in person,", font=ps_font, fill=SOFT)
y += 34
d.text((margin, y), "send a postcard \u2014 the fridge door is waiting.", font=ps_font, fill=SOFT)

img.save("entry.png", format="PNG", optimize=True)
print("wrote entry.png", img.size)
