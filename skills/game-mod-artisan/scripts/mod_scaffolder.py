"""
Game Mod Scaffolder & Project Generator.
Scaffolds complete, production-ready mod projects for:
1. Unity (BepInEx C# Plugin + Harmony Patches)
2. Unreal Engine (UE4SS Lua Mod)
3. Native C++ (MinHook DLL Injection)
4. Standalone Lua Scripts
"""
import argparse
import json
import os
import sys

def scaffold_unity_bepinex(mod_name, game_name, out_dir):
    mod_dir = os.path.join(out_dir, mod_name)
    os.makedirs(mod_dir, exist_ok=True)

    plugin_cs = f"""using BepInEx;
using BepInEx.Configuration;
using BepInEx.Logging;
using HarmonyLib;

namespace {mod_name}
{{
    [BepInPlugin(PluginGuid, PluginName, PluginVersion)]
    public class {mod_name}Plugin : BaseUnityPlugin
    {{
        public const string PluginGuid = "com.user.{mod_name.lower()}";
        public const string PluginName = "{mod_name}";
        public const string PluginVersion = "1.0.0";

        public static new ManualLogSource Logger {{ get; private set; }}
        public static ConfigEntry<bool> EnableMod {{ get; private set; }}

        private Harmony _harmony;

        private void Awake()
        {{
            Logger = base.Logger;

            // Bind configuration options
            EnableMod = Config.Bind("General", "EnableMod", true, "Enable or disable the {mod_name} mod.");

            if (!EnableMod.Value)
            {{
                Logger.LogInfo($"{mod_name} is disabled via configuration.");
                return;
            }}

            // Apply Harmony runtime patches
            _harmony = new Harmony(PluginGuid);
            _harmony.PatchAll();

            Logger.LogInfo($"{mod_name} v{{PluginVersion}} loaded successfully for {game_name}!");
        }}

        private void OnDestroy()

        {{
            _harmony?.UnpatchSelf();
        }}
    }}

    // Sample Harmony Patch: Target class and method in {game_name}
    [HarmonyPatch]
    public static class ExampleGameplayPatch
    {{
        // Replace 'PlayerController' and 'Update' with target class and method
        [HarmonyPatch(typeof(UnityEngine.Component), "Awake")]
        [HarmonyPrefix]
        public static void PrefixExample(UnityEngine.Component __instance)
        {{
            if (!{mod_name}Plugin.EnableMod.Value) return;
            // Intercept or modify game logic safely here
        }}
    }}
}}
"""

    csproj = f"""<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <AssemblyName>{mod_name}</AssemblyName>
    <Description>{mod_name} for {game_name}</Description>
    <Version>1.0.0</Version>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
    <LangVersion>latest</LangVersion>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="BepInEx.Core" Version="5.4.21" />
    <PackageReference Include="HarmonyX" Version="2.10.1" />
    <PackageReference Include="UnityEngine.Modules" Version="2021.3.0" IncludeAssets="compile" />
  </ItemGroup>
</Project>
"""

    readme = f"""# {mod_name} for {game_name}

## Installation:
1. Ensure **BepInEx 5** is installed in your {game_name} directory.
2. Place `{mod_name}.dll` into your `<GameDirectory>/BepInEx/plugins/` folder.
3. Launch the game. Configuration will generate in `BepInEx/config/com.user.{mod_name.lower()}.cfg`.
"""

    files = [
        (os.path.join(mod_dir, "Plugin.cs"), plugin_cs),
        (os.path.join(mod_dir, f"{mod_name}.csproj"), csproj),
        (os.path.join(mod_dir, "README.md"), readme)
    ]

    for path, content in files:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    return [p for p, _ in files]

def scaffold_unreal_ue4ss(mod_name, game_name, out_dir):
    mod_dir = os.path.join(out_dir, mod_name)
    scripts_dir = os.path.join(mod_dir, "scripts")
    os.makedirs(scripts_dir, exist_ok=True)

    main_lua = f"""-- {mod_name} for {game_name} (Unreal Engine UE4SS Mod)
print("[{mod_name}] Initializing mod for {game_name}...")

local isModActive = true

-- Example: Hook a function on player character or game mode
-- Replace '/Script/Engine.Actor:ReceiveBeginPlay' with the target UFunction
RegisterHook("/Script/Engine.Actor:ReceiveBeginPlay", function(self)
    if not isModActive then return end

    local actorName = self:get():GetFullName()
    -- print(string.format("[{mod_name}] Actor spawned: %s", actorName))
end)

print("[{mod_name}] Mod initialized successfully!")
"""

    enabled_txt = ""

    readme = f"""# {mod_name} for {game_name} (UE4SS Mod)

## Installation:
1. Ensure **UE4SS** (Unreal Engine 4/5 Scripting System) is installed in:
   `<GameFolder>/Binaries/Win64/ue4ss/`
2. Copy the `{mod_name}` folder into `<GameFolder>/Binaries/Win64/ue4ss/Mods/`.
3. Launch the game.
"""

    files = [
        (os.path.join(scripts_dir, "main.lua"), main_lua),
        (os.path.join(mod_dir, "enabled.txt"), enabled_txt),
        (os.path.join(mod_dir, "README.md"), readme)
    ]

    for path, content in files:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    return [p for p, _ in files]

def scaffold_native_dll(mod_name, game_name, out_dir):
    mod_dir = os.path.join(out_dir, mod_name)
    os.makedirs(mod_dir, exist_ok=True)

    dllmain_cpp = f"""// {mod_name} - Native C++ Hook DLL for {game_name}
#include <windows.h>
#include <iostream>

// Include MinHook header (or Detours)
// #include <MinHook.h>

// Example target function pointer signature
typedef void(*TargetFunction_t)(void* pThis, float value);
TargetFunction_t fpOriginalTarget = nullptr;

// Detour / Hook replacement function
void DetourTargetFunction(void* pThis, float value)
{{
    // Custom mod logic: modify value or trigger features
    float modifiedValue = value * 2.0f;

    // Call original function
    if (fpOriginalTarget)
    {{
        fpOriginalTarget(pThis, modifiedValue);
    }}
}}

DWORD WINAPI ModMainThread(LPVOID lpParam)
{{
    // Initialize hooking library
    // MH_Initialize();
    // MH_CreateHook(reinterpret_cast<LPVOID>(0x140001000), &DetourTargetFunction, reinterpret_cast<LPVOID*>(&fpOriginalTarget));
    // MH_EnableHook(MH_ALL_HOOKS);

    return 0;
}}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{{
    switch (ul_reason_for_call)
    {{
    case DLL_PROCESS_ATTACH:
        DisableThreadLibraryCalls(hModule);
        CreateThread(nullptr, 0, ModMainThread, hModule, 0, nullptr);
        break;
    case DLL_PROCESS_DETACH:
        // MH_DisableHook(MH_ALL_HOOKS);
        // MH_Uninitialize();
        break;
    }}
    return TRUE;
}}
"""

    readme = f"""# {mod_name} for {game_name} (Native C++ DLL)

## Compilation:
1. Open the source in Visual Studio (C++ / x64).
2. Link against `MinHook.lib` or Microsoft Detours.
3. Build as Release x64 DLL (`{mod_name}.dll`).

## Injection:
- Inject into `{game_name}.exe` using any standard DLL injector (or sidecar proxy DLL like `version.dll` / `dxgi.dll`).
"""

    files = [
        (os.path.join(mod_dir, "dllmain.cpp"), dllmain_cpp),
        (os.path.join(mod_dir, "README.md"), readme)
    ]

    for path, content in files:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    return [p for p, _ in files]

def main():
    parser = argparse.ArgumentParser(description="Scaffold Game Mod Projects")
    parser.add_argument("--engine", choices=["unity-bepinex", "unreal-ue4ss", "native-dll"], required=True)
    parser.add_argument("--name", required=True, help="Mod project name (e.g. InfiniteStaminaMod)")
    parser.add_argument("--game", default="GenericGame", help="Target game name")
    parser.add_argument("--out", required=True, help="Output directory")

    args = parser.parse_args()

    if args.engine == "unity-bepinex":
        created = scaffold_unity_bepinex(args.name, args.game, args.out)
    elif args.engine == "unreal-ue4ss":
        created = scaffold_unreal_ue4ss(args.name, args.game, args.out)
    else:
        created = scaffold_native_dll(args.name, args.game, args.out)

    result = {
        "status": "SUCCESS",
        "engine": args.engine,
        "mod_name": args.name,
        "game": args.game,
        "created_files": created
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
