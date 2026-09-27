---
name: visual-asset-artisan
description: Specializes in high-fidelity AI image generation, asset optimization.
---
# Visual Asset Artisan: Generation & Aesthetic Integration Protocol

This skill empowers agents and sub-agents to generate publication-grade visual assets using AI, optimize them for target platforms, and seamlessly integrate them with high aesthetic fidelity into software applications, PDF and Word documents, and game/mod projects.

---

## 1. Domain-Specific Generation & Integration Workflows

### 1. Software & Web Applications (UI / UX)
- **Generation Strategy**: Generate clean, modern UI components, icons, and hero illustrations. Avoid physical device frames (no laptops, phones) unless specifically asked.
- **Aspect Ratios**:
  - `16:9`: Hero banners, background splash art.
  - `1:1`: Profile avatars, app icons, square feature cards.
- **CSS / HTML Integration**:
  - Use responsive containers: `max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);`.
  - Use `object-fit: cover` or `contain` to prevent distortion.
  - Implement modern formats (WebP/PNG) with lazy loading (`loading="lazy"`).

### 2. Publication Documents (PDF & Word)
- **Generation Strategy**: Clean, editorial-quality illustrations, infographics, and technical diagrams with high contrast and legible details.
- **Aspect Ratios**: `4:3`, `3:2`, or `16:9` for document headers; `1:1` for side figures.
- **PDF Integration (HTML to PDF via `pdf-artisan`)**:
  - Set print resolution (300 DPI metadata).
  - Wrap in figure cards with `page-break-inside: avoid;` and `break-inside: avoid;` to prevent awkward splitting across page boundaries.
  - Add centered, styled captions beneath images (`font-size: 11px; color: #64748b; font-style: italic;`).
- **Word (`.docx`) Integration (via `python-docx`)**:
  - Insert images using explicit dimensions: `document.add_picture('image.png', width=Inches(5.5))`.
  - Center paragraph alignment: `p.alignment = WD_ALIGN_PARAGRAPH.CENTER`.

### 3. Games & Modding (Unity, Unreal, Native)
- **Generation Strategy**: Seamless textures, isometric sprites, character portraits, item icons, and HUD elements.
- **Power of Two (POT) Invariant**:
  - GPU texture samplers require textures with dimensions of $2^n$ (e.g. `256x256`, `512x512`, `1024x1024`, `2048x2048`).
  - Always resize generated textures to power-of-two dimensions before packing into game archives.
- **Format Requirements**:
  - UI Sprites & Icons: 32-bit RGBA PNG with clean alpha channel.
  - 3D Textures / Materials: Convert to DDS (DirectDraw Surface) with mipmaps (BC1 for diffuse without alpha, BC3/BC7 for alpha/normal maps).

---

## 2. Visual Asset Processor Script

Use `visual_asset_processor.py` to prepare, resize, and generate embed code for any image:

```powershell
# Optimize for Game Texture (Power-of-Two 1024x1024)
python "C:\Users\goldl\.gemini\config\skills\visual-asset-artisan\scripts\visual_asset_processor.py" --input "path\to\image.png" --mode game-pot --size 1024 --output "path\to\texture_1024.png"

# Optimize for Document / Print (300 DPI)
python "C:\Users\goldl\.gemini\config\skills\visual-asset-artisan\scripts\visual_asset_processor.py" --input "path\to\image.png" --mode document --dpi 300 --output "path\to\doc_hero.png"
```

Outputs:
- Resized, formatted image.
- Ready-to-use HTML/CSS snippet, `python-docx` snippet, and Unity C# sprite loading snippet.

---

## 3. References

- [Image Prompt Crafting Guide](file:///C:/Users/goldl/.gemini/config/skills/visual-asset-artisan/references/image_prompt_crafting_guide.md): Tested prompt templates for UI, game assets, textures, and documents.
- [Document and Game Asset Standards](file:///C:/Users/goldl/.gemini/config/skills/visual-asset-artisan/references/document_and_game_asset_standards.md): Standards for dimensions, DPI, formats, and alpha channels across target mediums.
