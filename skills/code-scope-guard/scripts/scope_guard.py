#!/usr/bin/env python3
"""
Code Scope Guard & Anti-Destruction Shield (code-scope-guard)
Enforces surgical edit scope, prevents accidental deletion, symbol gutting, and collateral file damage.
Part of the OmniAgentic Multi-Agent Framework.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

IGNORE_DIRS = {
    ".git", ".svn", ".hg", "node_modules", "venv", ".venv", "env",
    "__pycache__", ".pytest_cache", ".mypy_cache", "dist", "build",
    ".idea", ".vscode", "target", "bin", "obj", ".code_memory", ".scope_guard"
}

CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".lua", ".gd", ".cs",
    ".cpp", ".hpp", ".c", ".h", ".go", ".rs", ".java", ".kt",
    ".rb", ".php", ".swift", ".dart", ".sh", ".ps1", ".md", ".json", ".toml", ".yaml", ".yml"
}

def get_file_hash(path: Path) -> str:
    try:
        content = path.read_bytes()
        return hashlib.sha256(content).hexdigest()
    except Exception:
        return ""

def extract_symbol_names(lines: list[str], ext: str) -> set[str]:
    """Quickly extract declared function/class symbol names."""
    symbols = set()
    for line in lines:
        m = re.match(r"^[ \t]*(?:async\s+def|def|class|function|const|let|var|fn|func)\s+([a-zA-Z0-9_]+)", line)
        if m:
            symbols.add(m.group(1))
    return symbols

class ScopeGuard:
    def __init__(self, root_dir: str | Path):
        self.root = Path(root_dir).resolve()
        if self.root.is_file():
            self.guard_dir = self.root.parent / ".scope_guard"
        else:
            self.guard_dir = self.root / ".scope_guard"
        self.baseline_file = self.guard_dir / "baseline.json"
        self.backup_dir = self.guard_dir / "backup"

    def _collect_files(self) -> dict[str, dict]:
        manifest = {}
        target = self.root
        if target.is_file():
            files = [target]
        else:
            files = []
            for root, dirs, f_list in os.walk(target):
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
                for f in f_list:
                    p = Path(root) / f
                    if p.suffix.lower() in CODE_EXTENSIONS and p.stat().st_size < 2_000_000:
                        files.append(p)

        for p in files:
            rel = str(p.relative_to(self.root) if not self.root.is_file() else p.name)
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
                lines = text.splitlines()
                symbols = list(extract_symbol_names(lines, p.suffix.lower()))
                manifest[rel] = {
                    "hash": get_file_hash(p),
                    "lines": len(lines),
                    "size": p.stat().st_size,
                    "symbols": sorted(symbols)
                }
            except Exception:
                continue
        return manifest

    def lock(self, allow_files: list[str] | None = None, allow_symbols: list[str] | None = None) -> dict:
        """Lock baseline snapshot and define allowed scope."""
        self.guard_dir.mkdir(parents=True, exist_ok=True)
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir, ignore_errors=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

        manifest = self._collect_files()

        # Backup files
        for rel in manifest:
            src = self.root / rel if not self.root.is_file() else self.root
            dst = self.backup_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(src, dst)
            except Exception:
                pass

        baseline_data = {
            "locked_at": time.time(),
            "allow_files": [os.path.normpath(f) for f in (allow_files or [])],
            "allow_symbols": allow_symbols or [],
            "files": manifest
        }

        self.baseline_file.write_text(json.dumps(baseline_data, indent=2, ensure_ascii=False), encoding="utf-8")
        return {"locked_files": len(manifest), "allow_files": baseline_data["allow_files"]}

    def verify(self) -> dict:
        """Verify that current workspace strictly obeys the locked scope and preserved existing code."""
        if not self.baseline_file.exists():
            return {"status": "error", "message": "No active baseline lock found. Run 'lock' first."}

        baseline = json.loads(self.baseline_file.read_text(encoding="utf-8"))
        base_files = baseline["files"]
        allow_files = [os.path.normpath(f).lower() for f in baseline.get("allow_files", [])]

        violations = []
        modified_in_scope = []
        new_files = []

        current_manifest = self._collect_files()

        # Check for deleted files
        for rel, meta in base_files.items():
            curr_path = self.root / rel if not self.root.is_file() else self.root
            if not curr_path.exists():
                violations.append({
                    "type": "FILE_DELETION",
                    "severity": "CRITICAL",
                    "file": rel,
                    "detail": f"File '{rel}' was deleted completely! Collateral damage detected."
                })

        # Check modified and out-of-scope files
        for rel, curr_meta in current_manifest.items():
            norm_rel = os.path.normpath(rel).lower()
            if rel not in base_files:
                # Newly created file
                new_files.append(rel)
                # If allow_files is strictly enforced and not empty, check if new file is permitted
                if allow_files and not any(norm_rel.endswith(af) or af in norm_rel for af in allow_files):
                    violations.append({
                        "type": "UNAUTHORIZED_NEW_FILE",
                        "severity": "WARNING",
                        "file": rel,
                        "detail": f"New file '{rel}' created outside designated scope."
                    })
                continue

            old_meta = base_files[rel]
            if curr_meta["hash"] != old_meta["hash"]:
                # File was modified!
                is_allowed = (not allow_files) or any(norm_rel.endswith(af) or af in norm_rel for af in allow_files)
                if not is_allowed:
                    violations.append({
                        "type": "OUT_OF_SCOPE_MODIFICATION",
                        "severity": "CRITICAL",
                        "file": rel,
                        "detail": f"File '{rel}' was modified but is NOT in the allowed scope: {baseline['allow_files']}"
                    })
                else:
                    modified_in_scope.append(rel)

                # Check for symbol gutting / accidental deletion inside modified files
                old_symbols = set(old_meta.get("symbols", []))
                curr_symbols = set(curr_meta.get("symbols", []))
                deleted_symbols = old_symbols - curr_symbols

                if deleted_symbols:
                    violations.append({
                        "type": "SYMBOL_GUTTING",
                        "severity": "HIGH",
                        "file": rel,
                        "detail": f"Functions/Classes deleted in '{rel}': {list(deleted_symbols)}. Verify if deletion was explicitly requested."
                    })

                # Check for severe line shrinkage (> 40% reduction or > 50 lines dropped)
                if old_meta["lines"] > 30 and curr_meta["lines"] < (old_meta["lines"] * 0.6):
                    violations.append({
                        "type": "SUSPICIOUS_SHRINKAGE",
                        "severity": "HIGH",
                        "file": rel,
                        "detail": f"File '{rel}' shrunk from {old_meta['lines']} to {curr_meta['lines']} lines. Possible accidental truncation!"
                    })

        is_clean = len([v for v in violations if v["severity"] == "CRITICAL"]) == 0
        return {
            "status": "clean" if is_clean else "violation",
            "modified_in_scope": modified_in_scope,
            "new_files": new_files,
            "violations": violations
        }

    def rollback(self, target_file: str | None = None) -> int:
        """Restore files from baseline backup."""
        if not self.backup_dir.exists():
            print("[ERROR] No backup directory available for rollback.")
            return 1

        restored = 0
        if target_file:
            norm_target = os.path.normpath(target_file)
            src = self.backup_dir / norm_target
            dst = self.root / norm_target if not self.root.is_file() else self.root
            if src.exists():
                shutil.copy2(src, dst)
                print(f"[RESTORED] {target_file} recovered from pre-edit baseline snapshot.")
                return 0
            else:
                print(f"[ERROR] Backup for {target_file} not found.")
                return 1
        else:
            for root, dirs, files in os.walk(self.backup_dir):
                for f in files:
                    backup_path = Path(root) / f
                    rel = backup_path.relative_to(self.backup_dir)
                    dest_path = self.root / rel if not self.root.is_file() else self.root
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(backup_path, dest_path)
                    restored += 1
            print(f"[RESTORED] Full rollback complete. {restored} files restored to pristine state.")
            return 0

    def commit(self):
        """Clear baseline lock after clean verification."""
        if self.guard_dir.exists():
            shutil.rmtree(self.guard_dir, ignore_errors=True)
        print("[COMMITTED] Scope guard baseline finalized and unlocked.")

def main():
    parser = argparse.ArgumentParser(description="Scope Guard & Anti-Destruction Shield for AI Agents")
    parser.add_argument("--root", default=".", help="Root project directory")
    subparsers = parser.add_subparsers(dest="command")

    # lock
    p_lock = subparsers.add_parser("lock", help="Lock baseline snapshot and set allowed scope")
    p_lock.add_argument("--allow-files", nargs="*", default=[], help="Allowed file paths to edit")
    p_lock.add_argument("--allow-symbols", nargs="*", default=[], help="Allowed symbols to edit")

    # verify
    p_verify = subparsers.add_parser("verify", help="Verify modifications against baseline")
    p_verify.add_argument("--json", action="store_true", help="Output as JSON")

    # rollback
    p_rb = subparsers.add_parser("rollback", help="Rollback files from baseline backup")
    p_rb.add_argument("file", nargs="?", default=None, help="Specific file to rollback (or all)")

    # commit
    subparsers.add_parser("commit", help="Commit changes and release lock")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    guard = ScopeGuard(args.root)

    if args.command == "lock":
        res = guard.lock(allow_files=args.allow_files, allow_symbols=args.allow_symbols)
        print(f"[LOCKED] Baseline snapshot secured: {res['locked_files']} files protected.")
        if res["allow_files"]:
            print(f"         Allowed edit scope: {res['allow_files']}")
        else:
            print("         Allowed edit scope: ANY (Monitoring for accidental deletions and symbol gutting)")
    elif args.command == "verify":
        res = guard.verify()
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            if res.get("status") == "error":
                print(f"[ERROR] {res.get('message')}")
                sys.exit(1)

            print("==================================================")
            print(f" SCOPE GUARD AUDIT RESULT: {res['status'].upper()}")
            print("==================================================")
            if res["modified_in_scope"]:
                print(f"[OK] Modified within scope: {res['modified_in_scope']}")
            if res["new_files"]:
                print(f"[+] New files created: {res['new_files']}")

            if res["violations"]:
                print("\n[!] DETECTED SCOPE VIOLATIONS / ANOMALIES:")
                for v in res["violations"]:
                    print(f"  * [{v['severity']}] {v['type']} in {v['file']}: {v['detail']}")
                if res["status"] == "violation":
                    print("\n-> ACTION: Review violations or run 'python scope_guard.py rollback' to restore.")
                    sys.exit(1)
            else:
                print("[PASS] Zero out-of-scope edits. Zero deleted files. Zero gutted functions.")
    elif args.command == "rollback":
        ret = guard.rollback(args.file)
        sys.exit(ret)
    elif args.command == "commit":
        guard.commit()

if __name__ == "__main__":
    main()
