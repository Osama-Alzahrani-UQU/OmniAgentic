"""
UI Color Palette Extractor.
Extracts dominant colors and HEX values from a reference UI screenshot/image,
categorizes them into Background, Surface, Primary, and Accent tokens.
"""
import argparse
import json
import os
import sys
from PIL import Image

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_luminance(rgb):
    """Calculates perceived luminance of an RGB color (0.0 to 1.0)."""
    r, g, b = [x / 255.0 for x in rgb]
    return 0.299 * r + 0.587 * g + 0.114 * b

def extract_palette(image_path, num_colors=6):
    if not os.path.exists(image_path):
        return {"status": "error", "message": f"Image not found: {image_path}"}

    image = Image.open(image_path).convert("RGB")
    # Resize for fast processing
    image.thumbnail((200, 200))

    # Quantize to find dominant colors
    quantized = image.quantize(colors=num_colors, method=Image.Quantize.MEDIANCUT)
    palette_data = quantized.getpalette()[:num_colors * 3]

    colors = []
    for i in range(0, len(palette_data), 3):
        rgb = tuple(palette_data[i:i+3])
        hex_code = rgb_to_hex(rgb)
        lum = get_luminance(rgb)
        colors.append({
            "hex": hex_code,
            "rgb": list(rgb),
            "luminance": round(lum, 3)
        })

    # Sort colors by luminance (darkest to lightest)
    colors.sort(key=lambda c: c["luminance"])

    # Basic role heuristic:
    # If darkest color has low luminance (< 0.15), it is likely a dark theme background
    is_dark_theme = colors[0]["luminance"] < 0.25

    if is_dark_theme:
        suggested_roles = {
            "background": colors[0]["hex"],
            "surface": colors[1]["hex"],
            "border": colors[2]["hex"],
            "accent": colors[3]["hex"],
            "text_muted": colors[-2]["hex"],
            "text_primary": colors[-1]["hex"]
        }
    else:
        suggested_roles = {
            "background": colors[-1]["hex"],
            "surface": colors[-2]["hex"],
            "border": colors[-3]["hex"],
            "accent": colors[2]["hex"],
            "text_muted": colors[1]["hex"],
            "text_primary": colors[0]["hex"]
        }

    return {
        "status": "success",
        "image": os.path.abspath(image_path).replace("\\", "/"),
        "theme_type": "dark" if is_dark_theme else "light",
        "dominant_colors": colors,
        "suggested_design_tokens": suggested_roles
    }

def main():
    parser = argparse.ArgumentParser(description="Extract color palette from UI screenshot")
    parser.add_argument("--image", type=str, required=True, help="Path to reference screenshot")
    parser.add_argument("--colors", type=int, default=6, help="Number of dominant colors to extract")
    args = parser.parse_args()

    result = extract_palette(args.image, num_colors=args.colors)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
