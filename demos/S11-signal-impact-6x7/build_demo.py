from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
W, H = 1080, 1260

FIELD = "#111319"
CREAM = "#FFF7E8"
INK = "#111319"
LIME = "#FFF07A"
COBALT = "#1559FF"
CORAL = "#FF5A19"
MUTED = "#A6ADBA"
CHECK = "#65E36B"

FONT_CN = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_CN_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_LATIN = "/System/Library/Fonts/Supplemental/Arial Black.ttf"


def font(path, size):
    return ImageFont.truetype(path, size=size)


def cover_resize(image, size, focus=(0.5, 0.5)):
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = round((resized.width - target_w) * focus[0])
    top = round((resized.height - target_h) * focus[1])
    return resized.crop((left, top, left + target_w, top + target_h))


def fit_height(image, height):
    width = round(image.width * height / image.height)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def remove_checkerboard(image):
    """Remove the rendered checkerboard while retaining the generated subject."""
    image = image.convert("RGB")
    px = image.load()
    alpha = Image.new("L", image.size, 255)
    apx = alpha.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = px[x, y]
            # The image tool rendered transparency as two near-neutral light
            # checker colors. The supplied shirt remains darker and cooler.
            if min(r, g, b) > 226 and max(r, g, b) - min(r, g, b) < 12:
                apx[x, y] = 0
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.7))
    result = image.convert("RGBA")
    result.putalpha(alpha)
    box = alpha.getbbox()
    if box:
        result = result.crop(box)
    return result


def rounded(image, radius, border=0, border_color=CREAM):
    image = image.convert("RGBA")
    if border:
        outer = Image.new("RGBA", (image.width + border * 2, image.height + border * 2), (0, 0, 0, 0))
        outer_mask = Image.new("L", outer.size, 0)
        ImageDraw.Draw(outer_mask).rounded_rectangle((0, 0, outer.width - 1, outer.height - 1), radius + border, fill=255)
        outer.paste(Image.new("RGBA", outer.size, border_color), (0, 0), outer_mask)
        inner_mask = Image.new("L", image.size, 0)
        ImageDraw.Draw(inner_mask).rounded_rectangle((0, 0, image.width - 1, image.height - 1), radius, fill=255)
        outer.paste(image, (border, border), inner_mask)
        return outer
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, image.width - 1, image.height - 1), radius, fill=255)
    out = Image.new("RGBA", image.size, (0, 0, 0, 0))
    out.paste(image, (0, 0), mask)
    return out


def add_shadow(canvas, layer, xy, offset=(9, 12), opacity=125, blur=14):
    alpha = layer.getchannel("A")
    shadow_alpha = alpha.point(lambda a: a * opacity // 255).filter(ImageFilter.GaussianBlur(blur))
    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    shadow.putalpha(shadow_alpha)
    canvas.alpha_composite(shadow, (xy[0] + offset[0], xy[1] + offset[1]))
    canvas.alpha_composite(layer, xy)


def subject_with_signature_contour(subject, target_height=735):
    subject = fit_height(subject, target_height)
    pad = 38
    base = Image.new("RGBA", (subject.width + pad * 2, subject.height + pad * 2), (0, 0, 0, 0))
    base.alpha_composite(subject, (pad, pad))
    alpha = base.getchannel("A")

    # Signature: thin cream inner border plus one asymmetric cobalt offset contour.
    cream_mask = alpha.filter(ImageFilter.MaxFilter(19))
    offset_mask = alpha.filter(ImageFilter.MaxFilter(27))
    offset_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    offset_layer.putalpha(offset_mask)
    offset_color = Image.new("RGBA", base.size, COBALT)
    offset_color.putalpha(offset_mask)

    result = Image.new("RGBA", (base.width + 22, base.height + 26), (0, 0, 0, 0))
    result.alpha_composite(offset_color, (18, 20))
    cream_color = Image.new("RGBA", base.size, CREAM)
    cream_color.putalpha(cream_mask)
    result.alpha_composite(cream_color, (0, 0))
    result.alpha_composite(base, (0, 0))
    return result


def background():
    # Reference-led construction: the real topic material becomes the scene.
    # It is enlarged, softened and darkened like an interface wall—not replaced
    # by an unrelated illustration or generated poster background.
    source = Image.open(ROOT / "input/benchmark-source.png").convert("RGB")
    scene = cover_resize(source, (W, H), focus=(0.5, 0.38))
    scene = ImageEnhance.Contrast(scene).enhance(1.18)
    scene = scene.filter(ImageFilter.GaussianBlur(7))
    canvas = scene.convert("RGBA")
    canvas.alpha_composite(Image.new("RGBA", (W, H), (8, 10, 20, 202)))
    draw = ImageDraw.Draw(canvas)

    # Interface-like depth panels sampled from the supplied benchmark.
    draw.rounded_rectangle((610, 70, 1035, 355), radius=28, fill=(24, 28, 48, 205), outline=(255, 240, 122, 90), width=3)
    for i, label in enumerate(("SCIENCE", "CODING", "REASONING", "WORKFLOW")):
        y = 105 + i * 58
        draw.rounded_rectangle((650, y, 995, y + 42), radius=10, fill=(40, 44, 69, 220))
        draw.rounded_rectangle((668, y + 11, 686, y + 29), radius=4, fill=COBALT if i % 2 == 0 else CHECK)
        draw.text((706, y + 8), label, font=font(FONT_LATIN, 17), fill=(255, 247, 232, 170))

    # Dark edge planes keep the composition dense and protect small-screen type.
    draw.polygon([(0, 0), (535, 0), (492, 45), (0, 62)], fill=(8, 10, 18, 245))
    draw.polygon([(0, 1115), (320, 1092), (535, 1125), (1080, 1082), (1080, 1260), (0, 1260)], fill=(8, 10, 18, 245))

    random.seed(17)
    for _ in range(90):
        x = random.randrange(0, W)
        y = random.randrange(0, H)
        shade = random.choice([(255, 247, 232, 8), (83, 119, 255, 10)])
        draw.point((x, y), fill=shade)
    return canvas


def draw_signal_bars(draw, x, y):
    widths = (116, 82, 48)
    colors = (LIME, COBALT, CORAL)
    for i, (bar_w, color) in enumerate(zip(widths, colors)):
        yy = y + i * 18
        draw.rounded_rectangle((x, yy, x + bar_w, yy + 8), radius=4, fill=color)


def hook_text(canvas):
    draw = ImageDraw.Draw(canvas)

    # Small context label.
    logo = Image.open(ROOT / "input/anthropic-mark.png").convert("RGB")
    logo = rounded(cover_resize(logo, (72, 72)), 16, border=4, border_color=CREAM)
    canvas.alpha_composite(logo, (58, 42))
    draw.rounded_rectangle((142, 53, 474, 103), radius=18, fill=INK)
    draw.text((164, 63), "ANTHROPIC · 新模型", font=font(FONT_CN, 24), fill=CREAM)
    draw.rounded_rectangle((490, 53, 590, 103), radius=18, fill=CORAL, outline=CREAM, width=3)
    draw.text((510, 64), "实测", font=font(FONT_CN, 23), fill=CREAM)

    # Accent echo behind the hook.
    f_latin = font(FONT_LATIN, 126)
    draw.text((68, 154), "Fable 5.1", font=f_latin, fill=CREAM, stroke_width=14, stroke_fill=INK)
    draw.text((61, 146), "Fable 5.1", font=f_latin, fill=LIME, stroke_width=7, stroke_fill=CREAM)

    f_cn = font(FONT_CN, 112)
    draw.text((70, 292), "真能打吗？", font=f_cn, fill=CREAM, stroke_width=15, stroke_fill=INK)
    draw.text((66, 286), "真能打吗？", font=f_cn, fill=CREAM, stroke_width=4, stroke_fill=CREAM)

    draw.rounded_rectangle((76, 432, 498, 492), radius=17, fill=CREAM, outline=INK, width=5)
    draw.text((99, 444), "Mythos 5.1 同场对打", font=font(FONT_CN, 27), fill=INK)
    draw.text((79, 508), "不只看发布会跑分", font=font(FONT_CN, 25), fill=INK, stroke_width=3, stroke_fill=CREAM)

    # Short-video cover language: proof becomes three instantly scannable claims.
    checklist = [
        ("7 项能力横评", "#1559FF"),
        ("科研能力 52.6%", INK),
        ("Agent 编码 60.9%", INK),
    ]
    for i, (label, bg) in enumerate(checklist):
        y = 558 + i * 61
        draw.rounded_rectangle((76, y, 382, y + 49), radius=13, fill=bg, outline=CREAM, width=3)
        draw.rounded_rectangle((88, y + 10, 118, y + 39), radius=6, fill=CHECK)
        draw.line((96, y + 25, 103, y + 32, 113, y + 17), fill=INK, width=4)
        draw.text((132, y + 9), label, font=font(FONT_CN, 23), fill=CREAM)

    # Hand-drawn emphasis marks that point toward the human reaction.
    draw.arc((399, 560, 610, 735), 205, 335, fill=CREAM, width=9)
    draw.polygon([(574, 696), (616, 714), (586, 742)], fill=CREAM)
    draw.text((424, 615), "真实上手", font=font(FONT_CN, 24), fill=INK, stroke_width=4, stroke_fill=LIME)


def evidence_card():
    source = Image.open(ROOT / "input/benchmark-source.png").convert("RGB")
    crop = source.crop((20, 124, 745, 535))
    crop = cover_resize(crop, (475, 286), focus=(0.42, 0.45))
    crop = ImageEnhance.Contrast(crop).enhance(1.04)

    card = Image.new("RGBA", (515, 350), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((0, 0, 514, 349), radius=24, fill=CREAM, outline=INK, width=7)
    draw.rounded_rectangle((14, 58, 500, 332), radius=16, fill="#D7DDCC")
    card.alpha_composite(rounded(crop.resize((465, 252), Image.Resampling.LANCZOS), 12), (25, 68))

    draw.rounded_rectangle((24, 18, 144, 57), radius=10, fill=LIME)
    draw.text((39, 25), "实测 01", font=font(FONT_CN, 24), fill=INK)
    draw.text((164, 24), "真实榜单截图", font=font(FONT_CN, 23), fill=INK)

    # One factual emphasis, copied from the supplied benchmark.
    draw.rounded_rectangle((312, 296, 494, 338), radius=11, fill=COBALT)
    draw.text((329, 303), "60.9% 编码", font=font(FONT_CN, 22), fill=CREAM)
    return card.rotate(-2.2, resample=Image.Resampling.BICUBIC, expand=True)


def portrait_frame():
    """Use the supplied photo pixels directly inside an intentional editorial frame."""
    source = Image.open(ROOT / "input/portrait-source.png").convert("RGB")
    photo = cover_resize(source, (420, 585), focus=(0.5, 0.46))
    photo = rounded(photo, 28)

    frame = Image.new("RGBA", (474, 650), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    # Asymmetric cobalt contour + cream inner border: the style signature is
    # carried by the frame, while the supplied face remains untouched.
    draw.rounded_rectangle((30, 26, 473, 649), radius=38, fill=COBALT)
    draw.rounded_rectangle((0, 0, 449, 622), radius=36, fill=CREAM)
    frame.alpha_composite(photo, (15, 15))
    draw.rounded_rectangle((14, 14, 435, 600), radius=29, outline=INK, width=5)
    draw.rounded_rectangle((248, 572, 438, 618), radius=12, fill=LIME)
    draw.text((270, 582), "真人实测", font=font(FONT_CN, 25), fill=INK)
    return frame.rotate(1.6, resample=Image.Resampling.BICUBIC, expand=True)


def build():
    canvas = background()
    hook_text(canvas)

    card = evidence_card()
    add_shadow(canvas, card, (42, 760), offset=(10, 14), opacity=150, blur=10)

    checker = Image.open(ROOT / "input/portrait-cutout-checker.png")
    subject = remove_checkerboard(checker)
    subject = subject_with_signature_contour(subject, target_height=735)
    add_shadow(canvas, subject, (470, 475), offset=(12, 16), opacity=175, blur=12)

    draw = ImageDraw.Draw(canvas)
    # Bottom conclusion rail closes the composition without inventing a verdict.
    draw.rounded_rectangle((44, 1159, 1034, 1226), radius=18, fill=CREAM, outline=INK, width=6)
    draw.text((76, 1174), "不只看榜单｜真实体验到底怎么样？", font=font(FONT_CN, 31), fill=INK)

    out = ROOT / "preview.png"
    canvas.convert("RGB").save(out, quality=96)
    canvas.convert("RGB").resize((270, 315), Image.Resampling.LANCZOS).save(ROOT / "preview-small.png", quality=96)
    return out


if __name__ == "__main__":
    print(build())
