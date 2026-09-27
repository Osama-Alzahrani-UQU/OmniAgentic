# Arabic Font Pairing & Game Typography Guide

This reference details the principles of artistic and typographic harmony when localizing games, ensuring that Arabic fonts match the visual weight, ornamentation, and thematic mood of the original English typography.

---

## 1. The Typographic Harmony Rule

A game's font is a core part of its visual identity and atmosphere. When localizing into Arabic:
- **Never substitute stylized display fonts with generic system fonts** (e.g. replacing a medieval gothic font with standard Tahoma).
- **Match 4 Core Attributes**:
  1. **Visual Weight**: Regular, Medium, Bold, ExtraBold, or Black.
  2. **Stylistic Theme**: Serif vs. Sans-Serif vs. Display vs. Pixel.
  3. **Ornamentation**: Sharp terminals, futuristic cutouts, calligraphic swashes, or distressed textures.
  4. **Proportional Height (x-Height)**: Arabic fonts often have different vertical proportions; adjust font scale factor (e.g. `0.85x` or `1.15x`) so text fits within UI frames.

---

## 2. Style Pairing Matrix for Game Genres

| Game Genre / Visual Mood | English Font Reference | Recommended Arabic Font | Visual Characteristics |
| :--- | :--- | :--- | :--- |
| **Fantasy / Medieval / RPG** (e.g. Skyrim, Witcher, Elden Ring) | Trajan, Friz Quadrata, Cinzel | **Amiri**, **Almarai Bold**, **Scheherazade New** | Elegant calligraphic Naskh, pronounced serifs, classic dignity. |
| **Sci-Fi / Cyberpunk / Tech** (e.g. Cyberpunk 2077, Mass Effect, Starfield) | Orbitron, Eurostyle, Rajdhani | **Cairo**, **Tajawal**, **Readex Pro**, **Changa** | Geometric, square proportions, sharp tech cutouts, ultra-modern. |
| **Horror / Dark / Gothic** (e.g. Resident Evil, Silent Hill, Bloodborne) | Old English, Blackletter, Resident | **Aref Ruqaa**, **Lalezar**, **Gulzar** | Heavy strokes, intense contrast, dramatic calligraphic angles. |
| **Pixel Art / Retro 8-bit / 16-bit** (e.g. Undertale, Celeste, Stardew Valley) | Press Start 2P, Minecraftia | **Beiruti Pixel**, **Arabic 8-Bit** | Strict bitmap grid alignment, crisp pixel rendering without anti-aliasing. |
| **Casual / Cartoon / Battle Royale** (e.g. Fortnite, Fall Guys, Brawl Stars) | Burbank, Luckiest Guy, Comic Sans | **Dinar One**, **Somar**, **Lemonada** | Rounded corners, friendly open loops, playful bouncy baseline. |
| **Military / Tactical Shooter** (e.g. Call of Duty, Battlefield, CS2) | DIN 1451, Agency FB, Impact | **Almarai**, **Bebas Neue Arabic**, **Kufam** | Condensed, tall verticality, high legibility under motion. |

---

## 3. Font Merging & Glyph Injection Technique

When a game executable or engine has hardcoded font pointers:
1. Extract the game's original `.ttf` / `.otf`.
2. Extract the matching Arabic font `.ttf`.
3. Use Python `fontTools` or `FontForge` script to merge glyphs:
   - Keep Latin ASCII glyphs from the original font.
   - Inject Arabic Unicode ranges (`0x0600â€“0x06FF`, `0xFB50â€“0xFDFF`, `0xFE70â€“0xFEFF`) from the Arabic font.
   - Save the patched font under the exact same filename and replace it in the game's asset directory.
