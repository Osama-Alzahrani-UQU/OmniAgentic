# Hooking & Memory Manipulation Cheat Sheet

Quick reference snippets for Harmony (C#), MinHook (C++), and Memory Patching.

---

## 1. Harmony C# (Unity)

### Prefix (Override or Intercept)
```csharp
[HarmonyPatch(typeof(PlayerHealth), "TakeDamage")]
public static class TakeDamagePatch
{
    // Return false to skip the original method entirely (e.g. God Mode)
    [HarmonyPrefix]
    public static bool Prefix(ref float damage, PlayerHealth __instance)
    {
        if (GodModeEnabled)
        {
            damage = 0f;
            return false; // Skip original TakeDamage
        }
        return true; // Execute original TakeDamage
    }
}
```

### Postfix (Modify Return Value)
```csharp
[HarmonyPatch(typeof(Inventory), "GetItemCount")]
public static class InventoryPatch
{
    [HarmonyPostfix]
    public static void Postfix(ref int __result)
    {
        __result = 999; // Override returned item count
    }
}
```

---

## 2. MinHook C++ (Native Games)

```cpp
#include <MinHook.h>

typedef bool(__fastcall* tIsPlayerAlive)(void* pPlayer);
tIsPlayerAlive fpOriginalIsPlayerAlive = nullptr;

bool __fastcall DetourIsPlayerAlive(void* pPlayer)
{
    // Always return true or execute custom logic
    return true;
}

void InitializeHook(uintptr_t targetAddress)
{
    MH_Initialize();
    MH_CreateHook(reinterpret_cast<LPVOID>(targetAddress), 
                  &DetourIsPlayerAlive, 
                  reinterpret_cast<LPVOID*>(&fpOriginalIsPlayerAlive));
    MH_EnableHook(MH_ALL_HOOKS);
}
```

---

## 3. Dynamic Memory Patching (VirtualProtect)

```cpp
void PatchMemory(void* address, const unsigned char* bytes, size_t size)
{
    DWORD oldProtect;
    VirtualProtect(address, size, PAGE_EXECUTE_READWRITE, &oldProtect);
    memcpy(address, bytes, size);
    VirtualProtect(address, size, oldProtect, &oldProtect);
}

// Example: NOP out a 5-byte instruction (0x90)
unsigned char nops[5] = { 0x90, 0x90, 0x90, 0x90, 0x90 };
PatchMemory(reinterpret_cast<void*>(0x140123456), nops, sizeof(nops));
```
