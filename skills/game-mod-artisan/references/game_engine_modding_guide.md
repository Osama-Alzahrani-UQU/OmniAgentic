# Game Engine Modding Guide (Unity, Unreal, Native C++)

A comprehensive architectural guide for creating robust, maintainable game mods across major commercial and custom engines.

---

## 1. Unity Engine Modding

### Mono vs. IL2CPP
- **Mono**: The game executes managed C# bytecode inside `.NET Mono`. Assemblies reside in `<Game>_Data/Managed/Assembly-CSharp.dll`.
  - **Tooling**: dnSpy (decompilation and direct IL editing), BepInEx 5.x, Harmony.
- **IL2CPP**: C# code is compiled directly to native C++ machine code (`GameAssembly.dll`).
  - **Tooling**: Il2CppDumper (restores metadata and dummy DLLs), BepInEx 6.x Bleeding Edge or MelonLoader with Il2CppInterop.

### Harmony Runtime Patching Workflow
1. Locate target class and method using dnSpy or ILSpy.
2. Create a patch method with matching arguments:
   - `__instance`: The calling object instance.
   - `__result`: Reference to the return value (modifiable in postfix).
   - `___privateField`: Access private fields via triple underscore.
3. Apply patch using `Harmony.PatchAll()`.

---

## 2. Unreal Engine (UE4 / UE5) Modding

### Unreal Pak System
- Game content is stored in compressed `.pak` archives (`<Game>/Content/Paks/`).
- Engine loads loose paks in alphabetical order: files ending with `_P.pak` (Patch) override base files.
- **Tools**: UnrealPak, UAssetGUI (editing serialized binary assets without editor).

### UE4SS (Unreal Engine Scripting System)
- Injects a Lua and C++ scripting runtime into Unreal Engine games.
- Allows reading and writing UProperties, calling UFunctions, and intercepting engine events.

---

## 3. Native C++ & Hooking

### Direct Memory & API Hooking
- When a game doesn't use managed engines, hooks must be applied to native x86/x64 assembly:
- **MinHook**: Creates a 5-byte/14-byte jump detour at the target function prologue, preserving overwritten instructions in a trampoline.
- **VTable Hooking**: Modifies the virtual method table pointer of a class instance to redirect calls.
- **Signature Scanning (AOB)**: Locates function addresses dynamically across game updates using unique byte patterns with wildcards (`48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC 20`).
