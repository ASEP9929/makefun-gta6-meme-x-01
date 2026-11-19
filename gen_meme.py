#!/usr/bin/env python3
"""Draw the GTA 6 launch-week meme for gta6-meme-x-01, from scratch with PIL.

Scene: a Vice City synthwave sunset. Big caption "WAITED 13 YEARS FOR THIS
DAY". The make.fun ghost stands in the middle of the road holding its magenta
star coin up at the sun, a real character in the scene, not a sticker. A
bottom banner sells make.fun. Original art, no Rockstar assets, no downloads.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

random.seed(6)
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# --- sky gradient: deep purple -> magenta -> orange at the horizon ---
top = (43, 16, 85)
mid = (196, 33, 110)
bot = (255, 126, 61)
for y in range(0, 780):
    t = y / 780
    if t < 0.5:
        a, b, f = top, mid, t / 0.5
    else:
        a, b, f = mid, bot, (t - 0.5) / 0.5
    col = tuple(int(a[i] + (b[i] - a[i]) * f) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)

# --- stars in the upper sky ---
for _ in range(70):
    x = random.randint(0, W)
    y = random.randint(0, 260)
    r = random.randint(1, 3)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))

# --- synthwave sun with slats, upper right ---
sun_cx, sun_cy, sun_r = 760, 400, 165
for r in range(sun_r, 0, -6):
    t = 1 - r / sun_r
    col = (255, int(190 + 65 * t), int(60 + 120 * (1 - t)))
    d.ellipse([sun_cx - r, sun_cy - r, sun_cx + r, sun_cy + r], fill=col)
gap = 8
y = sun_cy + 10
while y < sun_cy + sun_r:
    d.rectangle([sun_cx - sun_r, y, sun_cx + sun_r, y + gap], fill=(224, 60, 110))
    y += gap + 16
    gap += 5

# --- skyline silhouette ---
d.rectangle([0, 640, W, 780], fill=(38, 12, 66))
x = 0
while x < W:
    bw = random.randint(50, 110)
    bh = random.randint(60, 150)
    d.rectangle([x, 700 - bh, x + bw, 780], fill=(26, 8, 48))
    for _ in range(bw * bh // 900):
        wx = random.randint(x + 6, x + bw - 8)
        wy = random.randint(700 - bh + 6, 770)
        d.rectangle([wx, wy, wx + 4, wy + 6], fill=(255, 214, 90))
    x += bw + random.randint(4, 18)

# --- ground / road ---
d.rectangle([0, 780, W, H], fill=(22, 10, 46))
d.line([(0, 780), (W, 780)], fill=(255, 45, 149), width=6)
# neon dashes on the road
for x in range(40, W, 160):
    d.rectangle([x, 880, x + 90, 894], fill=(255, 211, 25))

# --- palm trees, dark silhouettes ---
def palm(x, y, s, lean):
    top_x, top_y = x + lean, y - 210 * s
    d.line([(x, y), (top_x, top_y)], fill=(18, 6, 36), width=int(14 * s))
    for ang in (-150, -110, -70, -30, 10, 50):
        rad = math.radians(ang)
        pts = []
        for t in [i / 12 for i in range(13)]:
            px = top_x + math.cos(rad) * 130 * s * t
            py = top_y + math.sin(rad) * 60 * s * t + 90 * s * t * t
            pts.append((px, py))
        d.line(pts, fill=(18, 6, 36), width=int(10 * s))

palm(110, 800, 1.0, 40)
palm(990, 800, 1.1, -50)
palm(60, 790, 0.7, 30)
palm(1030, 790, 0.75, -35)

# --- make.fun ghost, large, centre of the road ---
def sparkle(cx, cy, r):
    k = 0.20
    pts = [(cx, cy - r), (cx + r * k, cy - r * k), (cx + r, cy),
           (cx + r * k, cy + r * k), (cx, cy + r), (cx - r * k, cy + r * k),
           (cx - r, cy), (cx - r * k, cy - r * k)]
    d.polygon(pts, fill=(0, 0, 0))

def star(cx, cy, r):
    pts = []
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
    d.polygon(pts, fill=(255, 255, 255))

gx, gy, gw, gh = 400, 470, 280, 330  # ghost bounding box
# ghost outline points: dome arc, sides, three wavy bumps at the bottom
pts = []
for a in range(180, -1, -6):
    rad = math.radians(a)
    pts.append((gx + gw / 2 + (gw / 2) * math.cos(rad),
                gy + gw / 2 - (gw / 2) * math.sin(rad)))
pts.append((gx + gw, gy + gh - 40))
bump_r = gw / 6
for b in range(3):
    bcx = gx + gw - bump_r - b * 2 * bump_r
    for a in range(0, 181, 10):
        rad = math.radians(a)
        pts.append((bcx + bump_r * math.cos(rad), gy + gh - 40 + bump_r * math.sin(rad)))
pts.append((gx, gy + gw / 2))
d.polygon(pts, fill=(255, 255, 255), outline=(0, 0, 0), width=10)
# sparkle eyes
sparkle(gx + 105, gy + 150, 26)
sparkle(gx + 175, gy + 150, 26)
# round little hand raised on the right, holding the magenta coin
d.ellipse([gx + 225, gy + 190, gx + 275, gy + 240], fill=(255, 255, 255),
          outline=(0, 0, 0), width=6)
coin_cx, coin_cy, coin_r = gx + 285, gy + 165, 52
d.ellipse([coin_cx - coin_r, coin_cy - coin_r, coin_cx + coin_r, coin_cy + coin_r],
          fill=(224, 0, 122), outline=(0, 0, 0), width=6)
star(coin_cx, coin_cy, 30)

# --- top caption ---
def text_center(y, s, font, fill, stroke=6):
    tw = d.textlength(s, font=font)
    d.text(((W - tw) / 2, y), s, font=font, fill=fill,
           stroke_width=stroke, stroke_fill=(0, 0, 0))

f_big = ImageFont.truetype(BOLD, 86)
f_med = ImageFont.truetype(BOLD, 76)
text_center(36, "WAITED 13 YEARS", f_big, (255, 255, 255))
text_center(158, "FOR THIS DAY", f_med, (255, 211, 25))

# --- bottom banner: the make.fun pitch, readable at 480 px ---
d.rectangle([0, 918, W, H], fill=(12, 4, 30))
d.line([(0, 918), (W, 918)], fill=(255, 45, 149), width=5)
f_b1 = ImageFont.truetype(BOLD, 56)
f_b2 = ImageFont.truetype(BOLD, 40)
text_center(934, "GTA VI IS FINALLY OUT", f_b1, (255, 255, 255), stroke=5)
text_center(1006, "now win real money on make.fun", f_b2, (255, 211, 25), stroke=4)

img.save("meme.png")
print("saved meme.png", img.size)
