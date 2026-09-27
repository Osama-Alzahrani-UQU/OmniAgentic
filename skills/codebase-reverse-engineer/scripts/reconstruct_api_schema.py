"""
API and Route Schema Reconstruction Tool.
Reverse-engineers HTTP endpoints from source code (FastAPI, Flask, Express, Django).
Extracts route paths, HTTP methods, and parameter schemas into an OpenAPI-like summary.
"""
import argparse
import json
import os
import re
import sys

ROUTE_PATTERNS = [
    # FastAPI / Flask: @app.get("/path"), @router.post("/path")
    (r"""@(?:app|router|blueprint|bp)\.(get|post|put|delete|patch)\s*\(\s*['"]([^'"]+)['"]""", "Python"),
    # Express.js: app.get('/path', ...), router.post('/path', ...)
    (r"""(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*['"]([^'"]+)['"]""", "JavaScript/TypeScript"),
    # Django: path('route/', view)
    (r"""path\s*\(\s*['"]([^'"]+)['"]\s*,\s*([a-zA-Z0-9_\.]+)""", "Django")
]

def scan_file_for_routes(file_path):
    endpoints = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        for idx, line in enumerate(lines, 1):
            for pattern, framework in ROUTE_PATTERNS:
                matches = re.finditer(pattern, line)
                for m in matches:
                    if framework == "Django":
                        endpoints.append({
                            "line": idx,
                            "method": "ANY",
                            "path": "/" + m.group(1).lstrip("/"),
                            "handler": m.group(2),
                            "framework": framework
                        })
                    else:
                        endpoints.append({
                            "line": idx,
                            "method": m.group(1).upper(),
                            "path": m.group(2),
                            "framework": framework
                        })
    except Exception:
        pass
    return endpoints

def reconstruct_apis(dir_path):
    dir_path = os.path.abspath(dir_path)
    if not os.path.exists(dir_path):
        return {"status": "error", "message": f"Path not found: {dir_path}"}

    all_endpoints = []
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs if d not in [".git", "node_modules", "venv", ".venv", "__pycache__"]]
        for f in files:
            if f.endswith((".py", ".js", ".ts")):
                full_path = os.path.join(root, f)
                routes = scan_file_for_routes(full_path)
                for r in routes:
                    r["file"] = os.path.relpath(full_path, dir_path).replace("\\", "/")
                    all_endpoints.append(r)

    # Group by path
    grouped = {}
    for ep in all_endpoints:
        path = ep["path"]
        if path not in grouped:
            grouped[path] = []
        grouped[path].append({
            "method": ep["method"],
            "file": ep["file"],
            "line": ep["line"],
            "framework": ep.get("framework")
        })

    return {
        "status": "success",
        "total_endpoints_found": len(all_endpoints),
        "unique_paths_count": len(grouped),
        "endpoints_by_path": grouped
    }

def main():
    parser = argparse.ArgumentParser(description="Reconstruct API schemas from codebase")
    parser.add_argument("--path", type=str, default=".", help="Codebase directory to scan")
    args = parser.parse_args()

    result = reconstruct_apis(args.path)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
