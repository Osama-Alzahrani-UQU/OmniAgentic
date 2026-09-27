---
name: game-mod-artisan
description: 'Equips agents and sub-agents with advanced game and software modding
  expertise: Unity (BepInEx/Harmony C#).'
---
# Game Mod Artisan: Engineering & Modding Protocol

This skill enables agents and sub-agents to design, engineer, and build high-quality game mods, gameplay modifications, asset replacements, and engine extensions across diverse architectures and game engines.

---

## 1. Engine Detection & Architecture Matrix

Before writing any mod, identify the target game engine and runtime architecture:

| Game Engine / Runtime | Key Indicators | Preferred Modding Approach | Key Tools |
| :--- | :--- | :--- | :--- |
| **Unity (Mono)** | `UnityPlayer.dll`, `<Game>_Data/Managed/Assembly-CSharp.dll` | C# Plugin via **BepInEx 5/6** + **Harmony** runtime patching | dnSpy, ILSpy, BepInEx |
| **Unity (IL2CPP)** | `GameAssembly.dll`, `<Game>_Data/il2cpp_data` | BepInEx Bleeding Edge / MelonLoader (Il2CppInterop) or C++ hook | Il2CppDumper, Cpp2IL |
| **Unreal Engine (UE4/5)** | `<Game>/Content/Paks/`, `UnrealVersion.h` | **UE4SS** (Lua/C++ modding) or `.pak` archive asset override | UE4SS, UnrealPak, UAssetGUI |
| **Native C / C++** | Custom executable, DirectX/Vulkan/OpenGL DLLs | Native C++ DLL injection + **MinHook** / **Detours** | Visual Studio, x64dbg, Cheat Engine |
| **Script-Driven** | `.lua`, `.py`, `.js`, loose JSON/XML configs | Script hooks, runtime overrides, or data table editing | VS Code, LuaJIT |

---

## 2. Core Modding Protocols

### Protocol 1: The Non-Destructive Modding Invariant (ط­ظ…ط§ظٹط© ظ…ظ„ظپط§طھ ط§ظ„ظ„ط¹ط¨ط© ط§ظ„ط£طµظ„ظٹط©)
- **Zero Permanent Overwrites**: Never directly overwrite vanilla game executables or core archives without creating a timestamped `.vanilla.bak` backup.
- **Prefer Mod Loaders**: Always use standard community mod loaders (BepInEx, MelonLoader, UE4SS, Vortex-compatible folders) so users can install/uninstall cleanly by deleting a single folder.

### Protocol 2: Hooking & Patching Best Practices
- **Unity Harmony**:
  - Use `[HarmonyPrefix]` to inspect or intercept method execution before it runs. Return `false` to skip the original method when overriding logic entirely.
  - Use `[HarmonyPostfix]` to modify return values (`ref __result`) or trigger secondary actions.
  - Use `[HarmonyTranspiler]` for surgical IL bytecode alterations.
- **Native C++ MinHook**:
  - Always verify target address before calling `MH_CreateHook`.
  - Always store the original function pointer `fpOriginal` to call through safely.
  - Call `MH_EnableHook(MH_ALL_HOOKS)` only after all targets are registered.
- **Unreal Engine UE4SS**:
  - Register hooks via `RegisterHook("/Script/Engine.Actor:ReceiveBeginPlay", callback)`.
  - Use `StaticFindObject` to inspect in-memory UObjects and UFunctions.

### Protocol 3: Asset Packaging & Distribution
- Group mod files into standard distribution structures:
  - BepInEx: `BepInEx/plugins/<ModName>/<ModName>.dll`
  - UE4SS: `UE4SS/Mods/<ModName>/scripts/main.lua`
  - Loose Pak: `<Game>/Content/Paks/~mods/<ModName>_P.pak`
- Include a clear `README.md` with:
  1. Installation instructions.
  2. Compatibility / prerequisite mod loaders.
  3. Config options explanation.

---

## 3. Mod Scaffolder Helper Script

Use `mod_scaffolder.py` to generate complete, ready-to-compile mod project structures:

```powershell
python "C:\Users\goldl\.gemini\config\skills\game-mod-artisan\scripts\mod_scaffolder.py" --engine unity-bepinex --name "InfiniteStaminaMod" --game "MyGame" --out "C:\path\to\mods"
```

Supported engines:
- `unity-bepinex`: Generates C# BepInEx plugin project with Harmony patch and `.csproj`.
- `unreal-ue4ss`: Generates UE4SS Lua mod folder with `main.lua` and `enabled.txt`.
- `native-dll`: Generates C++ MinHook DLL project with `dllmain.cpp`.
- `lua-script`: Generates standalone game Lua override script.

---

## 4. References

- [Game Engine Modding Guide](file:///C:/Users/goldl/.gemini/config/skills/game-mod-artisan/references/game_engine_modding_guide.md): Complete architecture breakdown and walkthroughs.
- [Hooking and Memory Cheat Sheet](file:///C:/Users/goldl/.gemini/config/skills/game-mod-artisan/references/hooking_and_memory_cheat_sheet.md): Code snippets for Harmony, MinHook, VTable, and AOB scanning.
