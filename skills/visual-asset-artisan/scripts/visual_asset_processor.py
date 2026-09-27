"""
Visual Asset Processor & Integration Code Generator.
Optimizes images for:
1. Games & Mods (Power-of-Two dimensions: 256, 512, 1024, 2048).
2. Documents & Publications (PDF/Word 300 DPI metadata).
3. Software & Web UI (Responsive aspect ratio & compression).
Generates ready-to-use embedding code snippets.
"""
import argparse
import json
import os
import sys

def get_nearest_pot(val):
    pots = [64, 128, 256, 512, 1024, 2048, 4096]
    return min(pots, key=lambda x: abs(x - val))

def generate_snippets(output_path, width, height, mode):
    filename = os.path.basename(output_path)
    abs_path = os.path.abspath(output_path).replace("\\", "/")

    html_snippet = f"""<figure style="margin: 20px auto; text-align: center; break-inside: avoid; max-width: {width}px;">
  <img src="{abs_path}" alt="{filename}" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
  <figcaption style="margin-top: 8px; font-size: 12px; color: #64748b; font-style: italic;">{filename}</figcaption>
</figure>"""

    docx_snippet = f"""from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run()
run.add_picture(r"{abs_path}", width=Inches({min(width / 96.0, 6.0):.2f}))"""

    unity_csharp_snippet = f"""// Unity C# Runtime Sprite / Texture Loader
using System.IO;
using UnityEngine;

public static Sprite LoadModSprite(string filePath)
{{
    if (!File.Exists(filePath)) return null;
    byte[] fileData = File.ReadAllBytes(filePath);
    Texture2D texture = new Texture2D({width}, {height}, TextureFormat.RGBA32, false);
    if (texture.LoadImage(fileData))
    {{
        return Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), new Vector2(0.5f, 0.5f));
    }}
    return null;
}}"""

    return {
        "html_css": html_snippet,
        "docx_python": docx_snippet,
        "unity_csharp": unity_csharp_snippet
    }

def process_image(input_path, output_path, mode="web-ui", target_size=None, target_dpi=300):
    if not os.path.exists(input_path):
        return {"status": "ERROR", "message": f"Input file not found: {input_path}"}

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    try:
        from PIL import Image
        has_pil = True
    except ImportError:
        has_pil = False

    if not has_pil:
        # Fallback: copy file and report basic dimensions if PIL not present
        import shutil
        shutil.copy2(input_path, output_path)
        snippets = generate_snippets(output_path, 800, 600, mode)
        return {
            "status": "COPIED_NO_PIL",
            "message": "Pillow not installed; copied file directly without resizing.",
            "output_file": output_path,
            "snippets": snippets
        }

    with Image.open(input_path) as img:
        orig_w, orig_h = img.size

        if mode == "game-pot":
            if target_size:
                new_w = target_size
                new_h = target_size
            else:
                new_w = get_nearest_pot(orig_w)
                new_h = get_nearest_pot(orig_h)
            processed_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        elif mode == "icon":
            sz = target_size or 256
            processed_img = img.resize((sz, sz), Image.Resampling.LANCZOS)
            new_w, new_h = sz, sz
        elif mode == "document":
            if target_size:
                ratio = target_size / float(orig_w)
                new_w = target_size
                new_h = int(orig_h * ratio)
                processed_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            else:
                processed_img = img
                new_w, new_h = orig_w, orig_h
        else:  # web-ui
            if target_size and orig_w > target_size:
                ratio = target_size / float(orig_w)
                new_w = target_size
                new_h = int(orig_h * ratio)
                processed_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            else:
                processed_img = img
                new_w, new_h = orig_w, orig_h

        # Save with DPI metadata
        dpi_tuple = (target_dpi, target_dpi)
        processed_img.save(output_path, dpi=dpi_tuple, quality=95, optimize=True)

    snippets = generate_snippets(output_path, new_w, new_h, mode)

    return {
        "status": "SUCCESS",
        "input_file": input_path,
        "output_file": output_path,
        "original_dimensions": [orig_w, orig_h],
        "processed_dimensions": [new_w, new_h],
        "dpi": target_dpi,
        "mode": mode,
        "snippets": snippets
    }

def main():
    parser = argparse.ArgumentParser(description="Process visual assets and generate integration snippets.")
    parser.add_argument("--input", "-i", required=True, help="Path to input image")
    parser.add_argument("--output", "-o", required=True, help="Path to output image")
    parser.add_argument("--mode", choices=["game-pot", "document", "web-ui", "icon"], default="web-ui")
    parser.add_argument("--size", type=int, default=None, help="Target width or square size")
    parser.add_argument("--dpi", type=int, default=300, help="Target DPI for print/document")

    args = parser.parse_args()

    res = process_image(args.input, args.output, mode=args.mode, target_size=args.size, target_dpi=args.dpi)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
