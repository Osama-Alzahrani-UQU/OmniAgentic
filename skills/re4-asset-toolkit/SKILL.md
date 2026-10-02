---
name: re4-asset-toolkit
description: Capcom RE4 extraction and asset pipeline
---
# Resident Evil 4 Asset Extraction & Engine Toolkit

This skill provides comprehensive workflows, tool chains, format specifications, and extraction methodologies for Capcom's Resident Evil 4 Classic and Ultimate HD (UHD) game engine formats.

---

## 1. Engine Archive & Container Architecture

Resident Evil 4 structures its UI, animations, audio, and stage data into specialized container formats:

| Format / Extension | Purpose | Internal Structure | Primary Extraction Tool |
| :--- | :--- | :--- | :--- |
| **`.lfs` / `.yz2.lfs`** | Capcom LFS compressed container | High-compression header wrapping `.dat` or `.pack` | `re4lfs.exe` / `RE4_UHD_DAT_Tool` |
| **`.dat`** | Multi-asset bundle (e.g., `title.dat`) | Packs EFF, UWF, TPL, and script tables | `RE4_UHD_DAT_Tool.exe` |
| **`.pack` / `.yz2`** | Texture image packs (e.g., `3e000001.pack`) | Contains raw TGA/DDS textures mapped to IDs | `JADERLINK_RE4_UHD_BIN_TOOL.exe` |
| **`.EFF`** | Effect & UI composition | Bundles 2D UI meshes, textures (`.tpl`), and tables | `RE4UHD_EFF_Tool.exe` |
| **`.UWF`** | Capcom UI Animation & Layout | Defines 2D screen coords, vertex tints, and timers | Custom binary parser / RE4UWFTool |
| **`.TPL`** | Texture Palette Library | Raw GC/Wii/PC texture format | `JADERLINK_RE4_UHD_BIN_TOOL.exe` |

---

## 2. Key ImagePack Catalog

- **`3e000001`**: Authentic Main Title Screen UI (Resident Evil 4 Logo, NEW GAME, LOAD GAME, EXTRAS, OPTIONS, QUIT, Village Pueblo panoramas `0082`-`0084`).
- **`34000001`**: Game Over & Reset Screen ("You Are Dead", retry prompts).
- **`3a000001`**: Map, Merchant, and HUD UI elements.
- **`07000000`**: Global particle effects, laser sight, film grain, and HUD prompts.

---

## 3. Step-by-Step Extraction Workflow

1. **Decompress LFS**:
   ```powershell
   re4lfs.exe -d "BIO4\SS\eng\title.dat.lfs" "title_eng.dat"
   ```
2. **Unpack DAT Archive**:
   ```powershell
   RE4_UHD_DAT_Tool.exe "title_eng.dat"
   ```
   Generates `title_00.EFF` through `title_24.UWF`.
3. **Unpack EFF Effects & Textures**:
   ```powershell
   RE4UHD_EFF_Tool.exe "title_00.EFF"
   ```
   Extracts `.tpl` textures and references matching ImagePack `3E000001`.
4. **Extract Textures to TGA/PNG**:
   ```powershell
   JADERLINK_RE4_UHD_BIN_TOOL.exe unpack "3e000001.pack"
   ```
5. **Reconstruct & Composite**:
   - Alpha-mask font contours.
   - Symmetrically composite multi-part titles (e.g. `0037.tga` + `0035.tga` for Title Logo).
   - Wire vertex color tinting (`Color3.fromRGB(225, 45, 35)` when selected, `Color3.fromRGB(180, 180, 180)` idle).
