"""
Installation verification script for Windows.
Verifies whether a program is installed by querying:
1. System PATH (via shutil.which)
2. Windows Registry (HKLM & HKCU Uninstall keys)
"""
import argparse
import json
import os
import shutil
import sys
import winreg

def check_path(binary_name):
    """Checks if the binary is executable in the current PATH."""
    loc = shutil.which(binary_name)
    if loc:
        return {"found": True, "path": os.path.abspath(loc).replace("\\", "/")}
    # Also try common extensions if omitted
    for ext in [".exe", ".cmd", ".bat"]:
        loc = shutil.which(binary_name + ext)
        if loc:
            return {"found": True, "path": os.path.abspath(loc).replace("\\", "/")}
    return {"found": False}

def search_registry(app_name):
    """Searches Windows Uninstall registry keys for matching application names."""
    results = []
    registry_paths = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
    ]

    query = app_name.lower()

    for root_key, subkey_path in registry_paths:
        try:
            with winreg.OpenKey(root_key, subkey_path) as key:
                num_subkeys = winreg.QueryInfoKey(key)[0]
                for i in range(num_subkeys):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            display_name = ""
                            display_version = ""
                            install_loc = ""
                            publisher = ""
                            try:
                                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            except OSError:
                                pass

                            if display_name and query in display_name.lower():
                                try:
                                    display_version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                                except OSError:
                                    pass
                                try:
                                    install_loc = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                                except OSError:
                                    pass
                                try:
                                    publisher = winreg.QueryValueEx(subkey, "Publisher")[0]
                                except OSError:
                                    pass

                                results.append({
                                    "display_name": display_name,
                                    "display_version": display_version,
                                    "install_location": install_loc,
                                    "publisher": publisher,
                                    "registry_path": f"{subkey_path}\\{subkey_name}"
                                })
                    except OSError:
                        continue
        except OSError:
            continue

    return results

def main():
    parser = argparse.ArgumentParser(description="Verify software installation on Windows")
    parser.add_argument("--name", type=str, required=True, help="Program name to search (e.g. 'git', 'vlc', 'python')")
    args = parser.parse_args()

    path_result = check_path(args.name)
    reg_results = search_registry(args.name)

    is_installed = path_result["found"] or len(reg_results) > 0

    output = {
        "query": args.name,
        "is_installed": is_installed,
        "path_lookup": path_result,
        "registry_matches": reg_results
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
