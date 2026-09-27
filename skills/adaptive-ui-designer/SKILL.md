---
name: adaptive-ui-designer
description: Specializes in designing domain-adaptive user interfaces (e.g., Gaming,
  SaaS, E-commerce.
---
# Adaptive UI & Style Cloning Protocol

You are equipped with the **Adaptive UI Designer** protocol. As an agent or sub-agent, you design user interfaces that natively adapt to their domain (gaming, enterprise, commerce, etc.), strictly follow user menu structures, and faithfully clone visual styles from reference images.

---

## 1. The 3 Core Pillars of UI Generation

### Pillar 1: Domain-Adaptive Aesthetics
Tailor every visual element to the domain:
- **Gaming & Sci-Fi**:
  - Dark surfaces (`#0a0b10`, `#121520`), sharp angles / chamfered corners, neon accent glows (`box-shadow: 0 0 15px rgba(...)`), bold geometric/futuristic typography, tactical HUD-like borders, high-contrast hover states.
- **SaaS & Enterprise**:
  - Clean neutral palette (`#ffffff`, `#f8fafc`, `#0f172a`), subtle 1px borders (`border-slate-200`), rounded corners (`8px - 12px`), high-legibility sans-serif fonts (Inter, Roboto), soft ambient shadows.
- **E-Commerce & Consumer**:
  - Clear visual hierarchy, punchy CTA buttons (`#2563eb`, `#16a34a`), product badge accents, generous touch targets (min 44px).
- **Retro / Arcade**:
  - Monospace or pixel fonts, high-saturation 8-bit/16-bit colors, CRT scanline overlays, thick solid borders.
- Consult [domain_design_presets.md](./references/domain_design_presets.md) for ready-to-use palettes and tokens.

### Pillar 2: Strict Menu & Layout Fidelity (With Explicit Innovation Mode)
- **Default Mode (Strict Adherence)**:
  - If the user provides a specific list of menu items, buttons, or layouts:
    - **Zero Omission**: Include every single menu item requested in the exact order specified.
    - **Zero Unprompted Inventions**: Do not add, omit, or alter menu items unless explicitly instructed.
    - **Label Accuracy**: Use the user's exact wording for buttons, tabs, and menu headers.
- **Innovation Mode (When Explicitly Requested)**:
  - If the user explicitly asks to "invent a new type", "create an innovative layout", or "suggest creative additions", the agent is fully empowered to invent novel, creative, and domain-appropriate elements and structure.

### Pillar 3: Visual Style Cloning from Reference Images
When the user provides a reference screenshot or mockup image:
1. **Analyze with Vision**: Open the image using `view_file` to visually assess layout, spacing, and typography.
2. **Extract Palette**: Run `extract_palette.py` on the image:
   ```powershell
   python C:/Users/goldl/.gemini/config/skills/adaptive-ui-designer/scripts/extract_palette.py --image "<IMAGE_PATH>"
   ```
3. **Deconstruct Visual Language**:
   - Extract primary background, card background, border colors, and text contrast.
   - Note border radiuses (sharp, pill, or rounded 8px).
   - Note shadows, gradients, and inner glows.
   - Note icon styles and padding density.
4. **Replicate in Code**: Apply the extracted design tokens into HTML/CSS, Tailwind, or React code. See [image_style_cloning_guide.md](./references/image_style_cloning_guide.md).

---

## 2. Component Deliverable Format
Always deliver UI code as clean, self-contained, responsive components:
- Use CSS variables (`--color-primary`, `--bg-surface`, `--radius`) for theme tokens.
- Include interactive hover/active states.
- Ensure WCAG AA contrast ratio between text and background.
