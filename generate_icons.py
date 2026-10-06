"""Genera los iconos PNG de la PWA (512, 192 y apple-touch-icon 180).

Requiere Pillow (ya incluida en el entorno). Ejecutar: python generate_icons.py
"""
import os
from PIL import Image, ImageDraw, ImageFilter

BLUE_TOP = (10, 132, 255)      # #0A84FF
BLUE_BOTTOM = (90, 200, 250)   # #5AC8FA
BLUE = (10, 132, 255)
HEADER_BLUE = (234, 244, 255)


def gradient(size, top, bottom):
    img = Image.new("RGB", (size, size))
    d = ImageDraw.Draw(img)
    for y in range(size):
        t = y / (size - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (size, y)], fill=c)
    return img


def make_icon(size):
    img = gradient(size, BLUE_TOP, BLUE_BOTTOM).convert("RGBA")
    mx = int(size * 0.13)
    cx0, cy0 = mx, int(size * 0.23)
    cx1, cy1 = size - mx, int(size * 0.79)
    r = int(size * 0.09)

    # Sombra suave
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    off = int(size * 0.02)
    sd.rounded_rectangle([cx0, cy0 + off, cx1, cy1 + off], radius=r, fill=(0, 0, 0, 80))
    shadow = shadow.filter(ImageFilter.GaussianBlur(size * 0.02))
    img = Image.alpha_composite(img, shadow)

    d = ImageDraw.Draw(img)

    # Tarjeta blanca
    d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=r, fill=(255, 255, 255, 255))

    # Banda superior (cabecera del calendario)
    hh = int(size * 0.15)
    d.rounded_rectangle([cx0, cy0, cx1, cy0 + hh], radius=r, fill=HEADER_BLUE + (255,))
    d.rectangle([cx0, cy0 + hh // 2, cx1, cy0 + hh], fill=HEADER_BLUE + (255,))

    # Anillas
    ring_r = max(2, int(size * 0.022))
    for xf in (0.30, 0.70):
        rx = cx0 + int((cx1 - cx0) * xf)
        ry = cy0 + hh // 2
        d.ellipse([rx - ring_r, ry - ring_r, rx + ring_r, ry + ring_r], fill=BLUE + (255,))

    # Check
    lw = max(4, int(size * 0.05))
    pts = [
        (int(size * 0.335), int(size * 0.51)),
        (int(size * 0.455), int(size * 0.63)),
        (int(size * 0.665), int(size * 0.375)),
    ]
    d.line(pts, fill=BLUE + (255,), width=lw, joint="curve")
    for p in pts:
        d.ellipse([p[0] - lw // 2, p[1] - lw // 2, p[0] + lw // 2, p[1] + lw // 2], fill=BLUE + (255,))

    return img.convert("RGB")


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
    os.makedirs(out_dir, exist_ok=True)
    base = make_icon(1024)
    for name, size in [
        ("icon-512.png", 512),
        ("icon-192.png", 192),
        ("apple-touch-icon.png", 180),
    ]:
        im = base.resize((size, size), Image.LANCZOS)
        im.save(os.path.join(out_dir, name), "PNG")
        print("guardado:", os.path.join(out_dir, name), f"({size}x{size})")


if __name__ == "__main__":
    main()
