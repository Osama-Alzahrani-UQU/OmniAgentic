# Document & Game Asset Standards

Technical specifications, dimensions, color spaces, and format requirements across Web, Documents (PDF/Word), and Games/Mods.

---

## 1. Specifications Matrix by Medium

| Medium | Target Resolution | Recommended Format | DPI / Compression | Layout Invariant |
| :--- | :--- | :--- | :--- | :--- |
| **Web & App UI** | Responsive (1x, 2x) | WebP, PNG, SVG | 72â€“96 DPI, Lossy 85% | `object-fit: cover;`, CSS aspect ratio |
| **PDF (Print/Digital)** | 1200â€“2400px width | PNG, JPEG | 300 DPI (Print), 150 DPI (Web) | `break-inside: avoid;`, centered captions |
| **Word (`.docx`)** | Max 6.0 inches width | PNG, JPEG | 300 DPI | Centered paragraph, explicit Inches width |
| **Game Textures** | Power-of-Two (POT) | DDS (BC1/BC7), PNG | No DPI (GPU sampled) | Mipmaps generated, no non-POT scaling |
| **Game UI Sprites** | 64x64, 128x128, 256x256 | 32-bit RGBA PNG | Clean Alpha channel | Pre-multiplied or straight alpha |

---

## 2. Power-of-Two (POT) Rule for Game Engines

Modern graphics pipelines (DirectX, Vulkan, OpenGL, Metal) sample textures most efficiently when dimensions are powers of two:
- Valid sizes: `64x64`, `128x128`, `256x256`, `512x512`, `1024x1024`, `2048x2048`, `4096x4096`.
- Rectangular POT is also valid if needed: `1024x512`, `2048x1024`.
- **Why?** Mipmapping algorithms divide dimensions by 2 repeatedly until 1x1. Non-POT textures either fail to generate hardware mipmaps or consume extra VRAM due to runtime padding.

---

## 3. High-Quality PDF & Word Embedding Rules

1. **Do not upscale small images**: Never scale a 300px image to full page width. Generate at native resolution or keep the display width proportional.
2. **Always include descriptive captions**: Readers rely on captions for context. In HTML/PDF, use `<figure>` and `<figcaption>`.
3. **Control Page Breaks**: In PDF styling, ensure images never separate from their captions or break across two pages:
   ```css
   figure {
     page-break-inside: avoid;
     break-inside: avoid;
   }
   ```
