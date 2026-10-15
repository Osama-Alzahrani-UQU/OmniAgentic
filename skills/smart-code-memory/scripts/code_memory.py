#!/usr/bin/env python3
"""
Smart Code Memory Engine (smart-code-memory)
Fast working memory, symbol indexing, line-targeted retrieval, and agent scratchpad.
Part of the OmniAgentic Multi-Agent Framework.
"""

import argparse
import hashlib
import json
import os
import re
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
    ".rb", ".php", ".swift", ".dart", ".sh", ".ps1"
}

def get_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8", errors="replace")).hexdigest()

def extract_symbols(lines: list[str], ext: str) -> list[dict]:
    """Extract classes, functions, and methods with accurate start and end line numbers."""
    symbols = []
    total_lines = len(lines)
    
    # Python parsing
    if ext == ".py":
        for idx, line in enumerate(lines):
            line_no = idx + 1
            # match class or def
            m = re.match(r"^([ \t]*)(async\s+def|def|class)\s+([a-zA-Z0-9_]+)\s*(\([^\)]*\))?", line)
            if m:
                indent = len(m.group(1).expandtabs(4))
                kind = "class" if m.group(2) == "class" else "function"
                name = m.group(3)
                sig = line.strip().rstrip(":")
                
                # Determine end line by indentation of subsequent non-empty lines
                end_line = total_lines
                for future_idx in range(idx + 1, total_lines):
                    future_line = lines[future_idx]
                    if not future_line.strip() or future_line.strip().startswith("#"):
                        continue
                    future_indent = len(future_line[:len(future_line) - len(future_line.lstrip(" \t"))].expandtabs(4))
                    if future_indent <= indent:
                        end_line = future_idx
                        break
                symbols.append({
                    "name": name,
                    "kind": kind,
                    "start_line": line_no,
                    "end_line": max(line_no, end_line),
                    "signature": sig
                })
        return symbols

    # JavaScript / TypeScript
    if ext in {".js", ".ts", ".jsx", ".tsx"}:
        for idx, line in enumerate(lines):
            line_no = idx + 1
            # match function, class, const func, export
            m = re.match(r"^[ \t]*(?:export\s+)?(?:async\s+)?(?:function\s+([a-zA-Z0-9_]+)|class\s+([a-zA-Z0-9_]+)|(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*(?:async\s*)?\([^\)]*\)\s*=>)", line)
            if m:
                name = m.group(1) or m.group(2) or m.group(3)
                kind = "class" if "class " in line else "function"
                sig = line.strip().rstrip("{")
                
                # Count braces to find approximate end_line
                brace_count = line.count("{") - line.count("}")
                end_line = line_no
                if "{" in line and brace_count > 0:
                    for future_idx in range(idx + 1, total_lines):
                        future_line = lines[future_idx]
                        brace_count += future_line.count("{") - future_line.count("}")
                        if brace_count <= 0:
                            end_line = future_idx + 1
                            break
                else:
                    end_line = min(total_lines, line_no + 10)
                    
                symbols.append({
                    "name": name,
                    "kind": kind,
                    "start_line": line_no,
                    "end_line": max(line_no, end_line),
                    "signature": sig
                })
        return symbols

    # Generic C / C++ / C# / Java / Go / Rust / Lua / GDScript
    for idx, line in enumerate(lines):
        line_no = idx + 1
        stripped = line.strip()
        if not stripped or stripped.startswith(("//", "/*", "*", "#", "--")):
            continue
        
        # Class or struct declaration
        m_cls = re.match(r"^(?:public\s+|private\s+|protected\s+|internal\s+)?(?:class|struct|interface|enum)\s+([a-zA-Z0-9_]+)", stripped)
        if m_cls:
            symbols.append({
                "name": m_cls.group(1),
                "kind": "class",
                "start_line": line_no,
                "end_line": min(total_lines, line_no + 20),
                "signature": stripped.rstrip("{")
            })
            continue

        # Function or method declaration
        m_fn = re.match(r"^(?:public\s+|private\s+|protected\s+|static\s+|async\s+|fn\s+|func\s+|function\s+)?(?:[a-zA-Z0-9_<>\*&]+\s+)?([a-zA-Z0-9_]+)\s*\([^\)]*\)\s*(?:\{|->|;|const)", stripped)
        if m_fn and m_fn.group(1) not in {"if", "for", "while", "switch", "catch", "return"}:
            symbols.append({
                "name": m_fn.group(1),
                "kind": "function",
                "start_line": line_no,
                "end_line": min(total_lines, line_no + 15),
                "signature": line.strip()
            })
            continue

    return symbols

class CodeMemory:
    def __init__(self, root_dir: str | Path = "."):
        resolved = Path(root_dir).resolve()
        if str(root_dir) in {".", ""} and not (resolved / ".git").exists():
            # Check if parent directories contain a git root
            cur = resolved
            while cur.parent != cur:
                if (cur / ".git").exists():
                    resolved = cur
                    break
                cur = cur.parent
        self.root = resolved
        if self.root.is_file():
            self.store_dir = self.root.parent / ".code_memory"
        else:
            self.store_dir = self.root / ".code_memory"
        self.index_file = self.store_dir / "index.json"
        self.scratchpad_file = self.store_dir / "scratchpad.json"
        self.data = self._load_index()

    def _load_index(self) -> dict:
        if self.index_file.exists():
            try:
                return json.loads(self.index_file.read_text(encoding="utf-8"))
            except Exception:
                pass
        return {"version": 1, "last_scan": 0, "files": {}}

    def _save_index(self):
        self.store_dir.mkdir(parents=True, exist_ok=True)
        self.data["last_scan"] = time.time()
        self.index_file.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")

    def _load_scratchpad(self) -> dict:
        if self.scratchpad_file.exists():
            try:
                return json.loads(self.scratchpad_file.read_text(encoding="utf-8"))
            except Exception:
                pass
        return {}

    def _save_scratchpad(self, notes: dict):
        self.store_dir.mkdir(parents=True, exist_ok=True)
        self.scratchpad_file.write_text(json.dumps(notes, indent=2, ensure_ascii=False), encoding="utf-8")

    def scan(self, force: bool = False) -> dict:
        """Scan directory and index files and symbols."""
        if force:
            self.data["files"] = {}
        target = self.root
        files_to_scan = []
        if target.is_file():
            files_to_scan.append(target)
        else:
            for root, dirs, files in os.walk(target):
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
                for f in files:
                    p = Path(root) / f
                    if p.suffix.lower() in CODE_EXTENSIONS and p.stat().st_size < 1_500_000:
                        files_to_scan.append(p)

        scanned = 0
        symbols_count = 0
        current_time = time.time()

        for f in files_to_scan:
            rel_path = (f.relative_to(self.root) if not self.root.is_file() else Path(f.name)).as_posix()
            try:
                content = f.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            content_hash = get_hash(content)
            cached = self.data["files"].get(rel_path)
            if not force and cached and cached.get("hash") == content_hash:
                symbols_count += len(cached.get("symbols", []))
                continue

            lines = content.splitlines()
            symbols = extract_symbols(lines, f.suffix.lower())
            self.data["files"][rel_path] = {
                "hash": content_hash,
                "lines": len(lines),
                "symbols": symbols,
                "updated_at": current_time
            }
            scanned += 1
            symbols_count += len(symbols)

        self._save_index()
        return {"scanned_files": scanned, "total_files": len(self.data["files"]), "total_symbols": symbols_count}

    def lookup(self, query: str) -> list[dict]:
        """Search symbol by name or keyword across indexed files."""
        results = []
        q_lower = query.lower()
        
        for rel_path, f_meta in self.data["files"].items():
            for sym in f_meta.get("symbols", []):
                sym_name = sym["name"].lower()
                sym_sig = sym.get("signature", "").lower()
                
                # Match score
                score = 0
                if sym_name == q_lower:
                    score = 100
                elif sym_name.startswith(q_lower):
                    score = 80
                elif q_lower in sym_name:
                    score = 60
                elif q_lower in sym_sig:
                    score = 40
                
                if score > 0:
                    results.append({
                        "file": rel_path,
                        "symbol": sym["name"],
                        "kind": sym["kind"],
                        "start_line": sym["start_line"],
                        "end_line": sym["end_line"],
                        "signature": sym.get("signature", ""),
                        "score": score
                    })

        results.sort(key=lambda x: (-x["score"], x["file"], x["start_line"]))
        return results

    def outline(self, file_path: str) -> dict:
        """Get compact structure outline of a specific file."""
        target_path = Path(file_path)
        if target_path.is_absolute():
            try:
                rel_path = target_path.relative_to(self.root).as_posix()
            except ValueError:
                rel_path = target_path.name
        else:
            rel_path = target_path.as_posix().lstrip("./")

        # Direct posix lookup
        meta = self.data["files"].get(rel_path)

        # Fallback 1: match normalizing backslashes
        if not meta:
            norm_target = rel_path.lower().replace("\\", "/")
            for k, v in self.data["files"].items():
                if k.lower() == norm_target or k.lower().endswith("/" + norm_target):
                    meta = v
                    rel_path = k
                    break

        # Fallback 2: match by basename if unique
        if not meta:
            base_matches = [k for k in self.data["files"] if Path(k).name.lower() == target_path.name.lower()]
            if len(base_matches) == 1:
                rel_path = base_matches[0]
                meta = self.data["files"][rel_path]

        # Auto-scan file if not indexed
        if not meta:
            full_path = self.root / rel_path if not self.root.is_file() else self.root
            if full_path.exists():
                self.scan()
                meta = self.data["files"].get(rel_path)

        if not meta:
            return {"error": f"File {file_path} not found in memory index"}

        return {
            "file": rel_path,
            "total_lines": meta.get("lines", 0),
            "symbols_count": len(meta.get("symbols", [])),
            "symbols": meta.get("symbols", [])
        }

    def note_store(self, key: str, value: str):
        notes = self._load_scratchpad()
        notes[key] = {"value": value, "timestamp": time.time()}
        self._save_scratchpad(notes)

    def note_get(self, key: str) -> str | None:
        notes = self._load_scratchpad()
        item = notes.get(key)
        return item["value"] if item else None

    def note_list(self) -> dict:
        return self._load_scratchpad()

def main():
    parser = argparse.ArgumentParser(description="Smart Code Memory Engine for AI Agents")
    parser.add_argument("--root", default=".", help="Root directory or file to index")
    subparsers = parser.add_subparsers(dest="command")

    # scan
    p_scan = subparsers.add_parser("scan", help="Scan and index code files")
    p_scan.add_argument("--force", action="store_true", help="Force re-indexing all files")

    # lookup
    p_lookup = subparsers.add_parser("lookup", help="Look up a symbol or keyword")
    p_lookup.add_argument("query", help="Symbol name or keyword")
    p_lookup.add_argument("--json", action="store_true", help="Output as JSON")

    # outline
    p_outline = subparsers.add_parser("outline", help="Get file outline")
    p_outline.add_argument("file", help="File path")

    # note
    p_note = subparsers.add_parser("note", help="Manage scratchpad working memory")
    p_note.add_argument("action", choices=["set", "get", "list", "clear"])
    p_note.add_argument("key", nargs="?", default="")
    p_note.add_argument("val", nargs="?", default="")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    mem = CodeMemory(args.root)

    if args.command == "scan":
        res = mem.scan(force=args.force)
        print(f"[OK] Memory Scan Complete: {res['scanned_files']} modified files scanned, {res['total_files']} files total, {res['total_symbols']} symbols indexed.")
    elif args.command == "lookup":
        results = mem.lookup(args.query)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            if not results:
                print(f"[FALLBACK] No symbol matching '{args.query}' found in memory index.")
                print("-> Recommendation: Review full file or search text directly.")
                sys.exit(2)
            print(f"Found {len(results)} matches for '{args.query}':")
            for r in results[:10]:
                print(f"  * {r['file']} [{r['start_line']}-{r['end_line']}] ({r['kind']}): {r['signature']}")
    elif args.command == "outline":
        res = mem.outline(args.file)
        if "error" in res:
            print(f"[ERROR] {res['error']}")
            sys.exit(1)
        print(f"Outline for {res['file']} ({res['total_lines']} lines, {res['symbols_count']} symbols):")
        for s in res["symbols"]:
            print(f"  L{s['start_line']:<4}-L{s['end_line']:<4} [{s['kind']:<8}] {s['name']}")
    elif args.command == "note":
        if args.action == "set":
            if not args.key or not args.val:
                print("Usage: note set <key> <val>")
                sys.exit(1)
            mem.note_store(args.key, args.val)
            print(f"[OK] Memory note saved: '{args.key}'")
        elif args.action == "get":
            val = mem.note_get(args.key)
            if val is not None:
                print(val)
            else:
                print(f"[NOT FOUND] Memory note '{args.key}' does not exist.")
                sys.exit(1)
        elif args.action == "list":
            notes = mem.note_list()
            print(json.dumps(notes, indent=2))
        elif args.action == "clear":
            mem._save_scratchpad({})
            print("[OK] Working memory notes cleared.")

if __name__ == "__main__":
    main()
