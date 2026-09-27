# Game Engine Localization & Text Injection Cheat Sheet

Step-by-step procedures for extracting and injecting translated Arabic text across Unity, Unreal Engine, Ren'Py, and Native game engines.

---

## 1. Unity Engine Localization

### Unity TextMeshPro (TMP)
1. **Extracting Text Assets**:
   - Open `<Game>_Data/resources.assets` or `sharedassets*.assets` in **UABEA** (Unity Asset Bundle Extractor).
   - Export `MonoBehaviour` or `TextAsset` containing string tables.
2. **Replacing Font with Arabic SDF Font Asset**:
   - In Unity Editor, import target Arabic TTF (e.g. Cairo).
   - Create TMP Font Asset: `Window > TextMeshPro > Font Asset Creator`.
   - Set Character Set to `Custom Range`: `0600-06FF,FB50-FDFF,FE70-FEFF`.
   - Export `.asset` file and import into game's asset bundle via UABEA.
3. **Automated Runtime Patching (BepInEx + Harmony)**:
   - Hook `TMP_Text.text` setter:
     ```csharp
     [HarmonyPatch(typeof(TMPro.TMP_Text), "set_text")]
     public static class ArabicTMPPatch
     {
         public static void Prefix(ref string value)
         {
             if (!string.IsNullOrEmpty(value))
             {
                 value = ArabicFixer.Fix(value); // Pre-shape and reverse RTL
             }
         }
     }
     ```

---

## 2. Unreal Engine 4 / 5 Localization

### Unreal `.locres` Files
- Path: `<Game>/Content/Localization/Game/<Culture>/Game.locres`
- **Workflow**:
  1. Extract `.locres` to JSON using `ue4-locres` CLI tool:
     ```cmd
     ue4-locres export Game.locres strings.json
     ```
  2. Translate strings in `strings.json`.
  3. Recompile back to `.locres`:
     ```cmd
     ue4-locres import strings_ar.json Game_ar.locres
     ```
  4. Place in `<Game>/Content/Localization/Game/ar/Game.locres`.
  5. Package into patch pak: `~mods/ArabicLocalization_P.pak`.

---

## 3. Ren'Py (Visual Novels)

1. Generate translation files from Ren'Py launcher: creates `game/tl/arabic/`.
2. Open `game/tl/arabic/screens.rpy` and define Arabic font:
   ```renpy
   init python:
       gui.text_font = "fonts/cairo.ttf"
       gui.name_text_font = "fonts/cairo_bold.ttf"
       gui.interface_text_font = "fonts/cairo.ttf"
   ```
3. Enable RTL if needed: `style.default.layout = "tex"` or use reshaped text.
