---
name: game-arabic-localizer
description: 'Equips agents and sub-agents with comprehensive game localization and
  Arabic translation expertise: text.'
---
# Game Arabic Localizer: Translation & Typography Protocol

This skill equips agents and sub-agents with the complete engineering and artistic methodology to localize (Arabize) games across any engine, solve complex Arabic RTL/letter-shaping rendering challenges, and preserve the original game's visual identity by matching Arabic typography to the original English font style and ornamentation.

---

## 1. The Core Engineering Challenges of Game Arabization

### 1. The RTL & Letter-Shaping Invariant (ط§ظ„طھط´ظƒظٹظ„ ظˆط¹ظƒط³ ط§ظ„ط§طھط¬ط§ظ‡)
- **The Problem**: Western game engines often treat strings as arrays of isolated LTR glyphs. Without complex text layout (CTL), Arabic renders disconnected and backwards (e.g. `ظ… ط± ط­ ط¨ ط§` instead of `ظ…ط±ط­ط¨ط§`).
- **Engine-Level Solutions**:
  - **Modern Engines (Unity TextMeshPro, Unreal Engine 5)**: Use native RTL support or enable HarfBuzz/ICU shaping modules.
  - **Engines without native RTL (Older Unity, Native C++, Custom Engines)**:
    - Pre-process strings through an Arabic Reshaper (joining letters into initial/medial/final glyph forms from Unicode Presentation Forms-B: `U+FE70 - U+FEFF`).
    - Reverse bidirectional character order using FriBidi / Python `bidi.algorithm` prior to injecting strings into game files.

### 2. Typographic Harmony & Style Matching (ظ…ط·ط§ط¨ظ‚ط© ط§ظ„ط®ط· ظˆط§ظ„ط²ط®ط±ظپط©)
- **Never use generic fonts**: Replacing a stylized gothic or sci-fi font with a bland system font ruins the player's immersion.
- **Style Pairing Matrix**:
  - **Fantasy / Medieval / Souls-like**: Calligraphic Naskh / Diwani with sharp serifs (e.g. *Amiri*, *Almarai Bold*, *Kawkab*).
  - **Sci-Fi / Cyberpunk / Clean UI**: Geometric, angular Sans-Serif with futuristic cutouts (e.g. *Cairo*, *Tajawal*, *Readex Pro*, *Changa*).
  - **Pixel Art / Retro 8-bit / 16-bit**: Grid-aligned Arabic bitmap fonts (e.g. *Beiruti Pixel*, *Arabic Pixel 12px*).
  - **Gothic / Dark / Horror**: Heavy, stylized display fonts with sharp terminals (e.g. *Aref Ruqaa*, *Gulzar*, *Lalezar*).
  - **Casual / Comic / Cartoonish**: Rounded, informal display typefaces (e.g. *Dinar One*, *Somar*, *Lemonada*).

### 3. Font Glyph Injection & SDF Generation
- If a game uses a single baked font file (TTF/OTF or Unity TextMeshPro SDF texture):
  - **Glyph Injection**: Inject Arabic Unicode ranges (`U+0600 - U+06FF`, `U+0750 - U+077F`, `U+FE70 - U+FEFF`) into the game's font using `fonttools`.
  - **SDF Atlas Expansion**: Generate or expand the Signed Distance Field (SDF) font asset in Unity/Unreal so the font engine can render Arabic characters at runtime.

---

## 2. Text Extraction & Injection Pipelines

| Engine | Primary Text Storage | Extraction Tool | Injection / Translation Method |
| :--- | :--- | :--- | :--- |
| **Unity (Mono)** | `Assembly-CSharp.dll`, TextMeshPro assets, JSON/XML tables | dnSpy, AssetStudio, UABEA | Edit strings in dnSpy or replace localization tables in `Resources.assets`. |
| **Unity (IL2CPP)** | `global-metadata.dat` | Il2CppDumper | Dump strings to `stringliteral.json`, edit and repack with metadata patchers. |
| **Unreal Engine** | `<Game>/Content/Localization/Game/*.locres` | `ue4-locres`, UnrealPak | Unpack `.locres` to JSON/PO, translate, and recompile. |
| **Ren'Py** | `game/tl/None/*.rpy` | Native Ren'Py `Generate Translations` | Create `game/tl/arabic/`, set `style.default.font = "fonts/arabic.ttf"`. |
| **RPG Maker** | `data/System.json`, `data/Map*.json` | Text editor / Python script | Batch translate JSON files; override font in `js/plugins.js`. |

---

## 3. Game Localization Toolkit

Use `game_localization_toolkit.py` to inspect fonts, shape Arabic text, and manage translation tables:

```powershell
# Pre-shape and reverse Arabic text for games without native RTL engines
python "C:\Users\goldl\.gemini\config\skills\game-arabic-localizer\scripts\game_localization_toolkit.py" --action shape --text "ظ…ط±ط­ط¨ط§ظ‹ ط¨ظƒ ظپظٹ ط§ظ„ظ„ط¹ط¨ط©"

# Inspect TTF/OTF font for Arabic glyph coverage and typographic style
python "C:\Users\goldl\.gemini\config\skills\game-arabic-localizer\scripts\game_localization_toolkit.py" --action inspect-font --font "path\to\game_font.ttf"

# Convert and export translation table (JSON / CSV)
python "C:\Users\goldl\.gemini\config\skills\game-arabic-localizer\scripts\game_localization_toolkit.py" --action export-table --input "strings.json" --output "strings_ar.json"
```

---

## 4. References

- [Arabic Font Pairing & Typography Guide](file:///C:/Users/goldl/.gemini/config/skills/game-arabic-localizer/references/arabic_font_pairing_and_typography.md): Matching English game font aesthetics to Arabic typography.
- [Engine Localization Cheat Sheet](file:///C:/Users/goldl/.gemini/config/skills/game-arabic-localizer/references/engine_localization_cheat_sheet.md): Concrete extraction and injection workflows for Unity, Unreal, Ren'Py, and Native engines.
