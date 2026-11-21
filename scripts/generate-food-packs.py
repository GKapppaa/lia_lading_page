"""Generate original, unbranded reference packshots for the Lía app preview."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "packs"
OUT.mkdir(parents=True, exist_ok=True)
DOG_PHOTO = ROOT / "public" / "v2" / "american-eskimo-dog-portrait-above.jpg"

W, H = 320, 420
FONT = ImageFont.load_default(size=24)
SMALL = ImageFont.load_default(size=15)
TINY = ImageFont.load_default(size=12)

variants = [
    ("esencial", "ESENCIAL", "#c9dfe0", "#123c48", "#eff6f5"),
    ("equilibrado", "EQUILIBRADO", "#2b7f86", "#ffffff", "#78d2c8"),
    ("premium", "PREMIUM", "#0b3d4a", "#ffffff", "#f47c2c"),
]

for slug, label, color, foreground, accent in variants:
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((48, 40, 278, 395), radius=35, fill=(4, 31, 38, 105))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    canvas.alpha_composite(shadow, (0, 4))

    bag = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bag)
    draw.rounded_rectangle((42, 24, 272, 382), radius=28, fill=color)
    draw.rounded_rectangle((48, 28, 266, 62), radius=14, fill=accent)
    draw.line((58, 51, 256, 51), fill=foreground, width=2)
    draw.rounded_rectangle((58, 82, 256, 111), radius=8, fill=accent)
    draw.text((129, 31), "LIA", font=FONT, fill=foreground)
    draw.text((91, 89), "NUTRICIÓN DIARIA", font=TINY, fill=foreground)

    dog = Image.open(DOG_PHOTO).convert("RGB")
    dog = dog.crop((60, 650, 1320, 1910)).resize((174, 174), Image.Resampling.LANCZOS)
    mask = Image.new("L", dog.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 173, 173), fill=255)
    bag.paste(dog, (70, 126), mask)
    draw.ellipse((70, 126, 244, 300), outline=accent, width=5)

    bbox = draw.textbbox((0, 0), label, font=SMALL)
    draw.text(((W - (bbox[2] - bbox[0])) / 2, 318), label, font=SMALL, fill=foreground)
    draw.text((119, 348), "PERRO ADULTO", font=TINY, fill=foreground)
    draw.text((132, 366), "12,5 kg", font=TINY, fill=foreground)
    canvas.alpha_composite(bag)
    canvas.save(OUT / f"{slug}.png", optimize=True)
    print(OUT / f"{slug}.png")
