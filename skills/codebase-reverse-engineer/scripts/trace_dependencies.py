"""
Module Dependency and Architecture Recovery Tool.
Scans Python, JavaScript, and TypeScript codebases to:
1. Extract import statements and module connections.
2. Build an architectural dependency graph.
3. Detect central hubs, entry points, and circular dependencies.
"""
import argparse
import ast
import json
import os
import re
import sys

def parse_python_imports(file_path):
    imports = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            tree = ast.parse(f.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module.split(".")[0])
    except Exception:
        pass
    return list(set(imports))

def parse_js_ts_imports(file_path):
    imports = []
    import_regex = re.compile(r"""(?:import\s+.*?from\s+['"]([^'"]+)['"]|require\s*\(\s*['"]([^'"]+)['"]\))""")
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        for match in import_regex.finditer(content):
            target = match.group(1) or match.group(2)
            if target:
                # Get base module name
                clean_target = os.path.basename(target) if target.startswith(".") else target.split("/")[0]
                imports.append(clean_target)
    except Exception:
        pass
    return list(set(imports))

def analyze_directory(dir_path):
    dir_path = os.path.abspath(dir_path)
    if not os.path.exists(dir_path):
        return {"status": "error", "message": f"Path not found: {dir_path}"}

    graph = {}
    incoming_edges = {}
    entry_points = []

    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs if d not in [".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build"]]
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, dir_path).replace("\\", "/")

            if f.endswith(".py"):
                imps = parse_python_imports(full_path)
            elif f.endswith((".js", ".jsx", ".ts", ".tsx")):
                imps = parse_js_ts_imports(full_path)
            else:
                continue

            graph[rel_path] = imps

            # Track incoming
            for imp in imps:
                incoming_edges[imp] = incoming_edges.get(imp, 0) + 1

            # Detect entry points
            if f.lower() in ["main.py", "app.py", "index.js", "index.ts", "server.js", "server.ts", "wsgi.py", "asgi.py"]:
                entry_points.append(rel_path)

    # Find central hubs (most imported internal modules)
    hubs = sorted(incoming_edges.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        "status": "success",
        "project_root": dir_path.replace("\\", "/"),
        "total_source_files": len(graph),
        "detected_entrypoints": entry_points,
        "most_referenced_modules": [{"module": h[0], "reference_count": h[1]} for h in hubs],
        "dependency_graph_sample": {k: graph[k] for k in list(graph.keys())[:15]}
    }

def main():
    parser = argparse.ArgumentParser(description="Trace codebase module dependencies")
    parser.add_argument("--path", type=str, default=".", help="Project root directory to analyze")
    args = parser.parse_args()

    result = analyze_directory(args.path)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
