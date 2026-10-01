#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experience Manager Utility for Continuous Learning
Manages recording, indexing, updating, and searching persistent problem-solution logs
across project-specific stores (troubleshooting.md) and global knowledge stores (~/.gemini/knowledge/).
"""

import os
import sys
import re
import argparse
import platform
from datetime import datetime
from pathlib import Path

GLOBAL_STORE_DIR = r"C:\Users\goldl\.gemini\knowledge"
GLOBAL_STORE_FILE = os.path.join(GLOBAL_STORE_DIR, "troubleshooting_history.md")

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def find_project_root(start_dir: str = None) -> str:
    """Intelligently detects project root by walking up directories looking for project markers."""
    if start_dir and os.path.isdir(start_dir):
        return os.path.abspath(start_dir)
        
    start_dir = os.path.abspath(os.getcwd())
    home_dir = os.path.abspath(os.path.expanduser("~"))
    
    project_markers = [
        ".git",
        "package.json",
        "pyproject.toml",
        "Cargo.toml",
        "go.mod",
        "pom.xml",
        "build.gradle",
        "CMakeLists.txt",
        ".sln",
        "troubleshooting.md",
    ]
    
    curr = start_dir
    while True:
        # Check project markers in current directory
        for m in project_markers:
            if os.path.exists(os.path.join(curr, m)):
                return curr
        # Check if local .gemini folder exists (and is not user home ~/.gemini)
        if os.path.exists(os.path.join(curr, ".gemini")) and curr != home_dir:
            return curr
            
        parent = os.path.dirname(curr)
        if parent == curr or curr == home_dir:
            break
        curr = parent
        
    return start_dir


def resolve_local_store(workspace_dir: str = None) -> str:
    """Resolves the path to the project-specific troubleshooting.md file."""
    root = find_project_root(workspace_dir)
    home_dir = os.path.abspath(os.path.expanduser("~"))
    # Check if a custom .gemini/troubleshooting.md exists inside the project (not global ~/.gemini)
    if root != home_dir:
        gemini_file = os.path.join(root, ".gemini", "troubleshooting.md")
        if os.path.exists(gemini_file):
            return gemini_file
    # Standard location: project root troubleshooting.md
    return os.path.join(root, "troubleshooting.md")


def ensure_global_store_exists():
    """Ensure the global knowledge directory and base troubleshooting file exist."""
    os.makedirs(GLOBAL_STORE_DIR, exist_ok=True)
    if not os.path.exists(GLOBAL_STORE_FILE):
        header = (
            "# Global Troubleshooting & Learned Solutions History\n\n"
            "This document stores verified technical solutions, root cause analyses, "
            "and prevention invariants to ensure mistakes are never repeated across conversations.\n\n"
            "---\n\n"
        )
        with open(GLOBAL_STORE_FILE, "w", encoding="utf-8") as f:
            f.write(header)


def init_project_store(store_path: str, project_name: str = "") -> str:
    """Initializes a new structured project-level troubleshooting.md file if not present."""
    store_dir = os.path.dirname(store_path)
    if store_dir:
        os.makedirs(store_dir, exist_ok=True)
        
    if not project_name:
        project_name = os.path.basename(os.path.abspath(store_dir if store_dir else "."))
        
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = (
        f"# Project Troubleshooting & Learned Solutions History\n\n"
        f"> **Project**: `{project_name}`  \n"
        f"> **Initialized**: `{now_str}`  \n"
        f"> **Last Updated**: `{now_str}`  \n"
        f"> **Total Solved Issues**: `0`\n\n"
        f"This document permanently records all technical issues, runtime exceptions, architectural pitfalls, "
        f"and verified solutions encountered specifically in this project. "
        f"Always consult this file before implementing new features or debugging regressions to avoid repeating known mistakes.\n\n"
        f"## Table of Contents\n"
        f"<!-- TOC_START -->\n"
        f"_No issues recorded yet._\n"
        f"<!-- TOC_END -->\n\n"
        f"---\n\n"
    )
    with open(store_path, "w", encoding="utf-8") as f:
        f.write(header)
    return store_path


def slugify(text: str) -> str:
    """Generate GitHub-compatible markdown anchor slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text


def refresh_table_of_contents(store_path: str):
    """Regenerates the Table of Contents and updates metadata in the project troubleshooting file."""
    if not os.path.exists(store_path):
        return
        
    with open(store_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all issue headers matching '### [YYYY-MM-DD ...'
    pattern = re.compile(r"^###\s+\[(.*?)\]\s+(.*?)$", re.MULTILINE)
    matches = pattern.findall(content)
    
    total_issues = len(matches)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Update header metadata
    content = re.sub(r">\s+\*\*Last Updated\*\*:\s+`.*?`", f"> **Last Updated**: `{now_str}`", content)
    content = re.sub(r">\s+\*\*Total Solved Issues\*\*:\s+`.*?`", f"> **Total Solved Issues**: `{total_issues}`", content)
    
    # Generate new TOC
    if matches:
        toc_lines = []
        for idx, (tstamp, title) in enumerate(matches, 1):
            clean_title = title.strip()
            anchor_text = f"{tstamp} {clean_title}"
            slug = slugify(anchor_text)
            toc_lines.append(f"{idx}. [{clean_title}](#{slug}) - *`{tstamp}`*")
        new_toc = "\n".join(toc_lines)
    else:
        new_toc = "_No issues recorded yet._"
        
    toc_block = f"<!-- TOC_START -->\n{new_toc}\n<!-- TOC_END -->"
    content = re.sub(r"<!-- TOC_START -->.*?<!-- TOC_END -->", toc_block, content, flags=re.DOTALL)
    
    with open(store_path, "w", encoding="utf-8") as f:
        f.write(content)


def format_full_entry(
    title: str,
    problem: str,
    cause: str,
    solution: str,
    stack_trace: str = "",
    steps: str = "",
    verification: str = "",
    prevention: str = "",
    files: str = "",
    severity: str = "Major",
    tags: str = "",
    env_info: str = ""
) -> str:
    """Builds a rich, fully-detailed markdown entry for the project troubleshooting log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Format tags
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    formatted_tags = " ".join([f"`[{t}]`" for t in tag_list]) if tag_list else "`[General]`"
    
    # Format affected files
    if files:
        files_list = [f.strip() for f in files.split(",") if f.strip()]
        formatted_files = ", ".join([f"`{f}`" for f in files_list])
    else:
        formatted_files = "N/A"
        
    # Format environment info
    if not env_info:
        env_info = f"OS: {platform.system()} {platform.release()} ({platform.machine()}) | Python: {platform.python_version()}"

    lines = [
        f"### [{timestamp}] {title.strip()}",
        f"- **Severity**: `{severity}` | **Status**: `Resolved` | **Tags**: {formatted_tags}",
        f"- **Affected Files**: {formatted_files}",
        f"- **Environment**: {env_info.strip()}",
        f"",
        f"#### 1. Problem & Symptoms",
        problem.strip(),
        f"",
    ]
    
    if steps.strip():
        lines.extend([
            f"#### 2. Trigger / Steps to Reproduce",
            steps.strip(),
            f"",
        ])
        
    if stack_trace.strip():
        lines.extend([
            f"#### 3. Error Output / Stack Trace",
            f"```text",
            stack_trace.strip(),
            f"```",
            f"",
        ])
        
    lines.extend([
        f"#### 4. Root Cause Analysis",
        cause.strip(),
        f"",
        f"#### 5. Verified Solution",
        solution.strip(),
        f"",
    ])
    
    if verification.strip():
        lines.extend([
            f"#### 6. Verification & Test",
            verification.strip(),
            f"",
        ])
        
    if prevention.strip():
        lines.extend([
            f"#### 7. Prevention Invariant & Lessons Learned",
            prevention.strip(),
            f"",
        ])
        
    lines.extend([
        f"---",
        f"",
        f""
    ])
    
    return "\n".join(lines)


def format_global_summary_entry(
    title: str,
    problem: str,
    cause: str,
    solution: str,
    prevention: str = "",
    tags: str = "",
    project_name: str = ""
) -> str:
    """Builds a cross-project summary entry for the global knowledge store."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    if project_name:
        tag_list.insert(0, project_name)
    formatted_tags = " ".join([f"`[{t}]`" for t in tag_list]) if tag_list else "`[General]`"
    
    lines = [
        f"### [{timestamp}] {title.strip()}",
        f"- **Tags**: {formatted_tags}",
        f"- **Problem & Error**: {problem.strip()}",
        f"- **Root Cause**: {cause.strip()}",
        f"- **Verified Solution**: {solution.strip()}",
    ]
    
    if prevention.strip():
        lines.append(f"- **Prevention Invariant**: {prevention.strip()}")
        
    lines.extend(["\n---\n"])
    return "\n".join(lines)


def add_entry(
    title: str,
    problem: str,
    cause: str,
    solution: str,
    stack_trace: str = "",
    steps: str = "",
    verification: str = "",
    prevention: str = "",
    files: str = "",
    severity: str = "Major",
    tags: str = "",
    workspace_dir: str = "",
    sync_global: bool = True
) -> dict:
    """Adds a full-detail troubleshooting entry to the project log and synchronizes globally."""
    # 1. Resolve local project store
    local_store_path = resolve_local_store(workspace_dir)
    project_root = os.path.dirname(local_store_path)
    project_name = os.path.basename(os.path.abspath(project_root))
    
    # Initialize if not existing
    if not os.path.exists(local_store_path):
        init_project_store(local_store_path, project_name)
        print(f"Initialized new project troubleshooting file: {local_store_path}")

    # Build full detailed entry
    full_entry = format_full_entry(
        title=title,
        problem=problem,
        cause=cause,
        solution=solution,
        stack_trace=stack_trace,
        steps=steps,
        verification=verification,
        prevention=prevention,
        files=files,
        severity=severity,
        tags=tags
    )

    # Append to local project store
    with open(local_store_path, "a", encoding="utf-8") as f:
        f.write(full_entry)
        
    # Refresh Table of Contents and counts
    refresh_table_of_contents(local_store_path)
    print(f"Recorded in Project Store: {local_store_path}")

    # 2. Append to global store if enabled
    if sync_global:
        ensure_global_store_exists()
        global_entry = format_global_summary_entry(
            title=title,
            problem=problem,
            cause=cause,
            solution=solution,
            prevention=prevention,
            tags=tags,
            project_name=project_name
        )
        with open(GLOBAL_STORE_FILE, "a", encoding="utf-8") as f:
            f.write(global_entry)
        print(f"Synchronized with Global Store: {GLOBAL_STORE_FILE}")

    return {
        "local_file": local_store_path,
        "global_file": GLOBAL_STORE_FILE if sync_global else None,
        "project": project_name
    }


def search_entries(query: str, workspace_dir: str = "") -> list:
    """Search for relevant entries across local project and global stores."""
    ensure_global_store_exists()
    query_terms = query.lower().split()
    results = []

    files_to_search = []
    local_file = resolve_local_store(workspace_dir)
    if os.path.exists(local_file):
        files_to_search.append(("Project Local", local_file))
        
    files_to_search.append(("Global Knowledge", GLOBAL_STORE_FILE))

    for scope, fpath in files_to_search:
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        sections = content.split("### [")
        for sec in sections[1:]:
            full_sec = "### [" + sec
            lower_sec = full_sec.lower()
            if any(term in lower_sec for term in query_terms):
                results.append((scope, fpath, full_sec.strip()))

    return results


def get_stats(workspace_dir: str = "") -> dict:
    """Compute statistics for project-local and global troubleshooting files."""
    local_file = resolve_local_store(workspace_dir)
    stats = {
        "local_file": local_file,
        "local_exists": os.path.exists(local_file),
        "local_issues": 0,
        "global_file": GLOBAL_STORE_FILE,
        "global_exists": os.path.exists(GLOBAL_STORE_FILE),
        "global_issues": 0
    }
    
    if stats["local_exists"]:
        with open(local_file, "r", encoding="utf-8") as f:
            content = f.read()
        stats["local_issues"] = len(re.findall(r"^###\s+\[", content, re.MULTILINE))
        
    if stats["global_exists"]:
        with open(GLOBAL_STORE_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        stats["global_issues"] = len(re.findall(r"^###\s+\[", content, re.MULTILINE))
        
    return stats


def main():
    parser = argparse.ArgumentParser(description="Experience Manager for Project & Global Continuous Learning")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # Init subcommand
    init_parser = subparsers.add_parser("init", help="Initialize project-specific troubleshooting.md")
    init_parser.add_argument("--workspace", default="", help="Project root workspace directory")
    init_parser.add_argument("--name", default="", help="Project name")

    # Add subcommand
    add_parser = subparsers.add_parser("add", help="Record a fully detailed solved issue")
    add_parser.add_argument("--title", required=True, help="Title of the issue")
    add_parser.add_argument("--problem", required=True, help="Detailed problem description and symptoms")
    add_parser.add_argument("--cause", required=True, help="Root cause analysis")
    add_parser.add_argument("--solution", required=True, help="Exact verified solution / code changes")
    add_parser.add_argument("--stack-trace", default="", help="Raw error output or stack trace")
    add_parser.add_argument("--steps", default="", help="Steps to reproduce or trigger context")
    add_parser.add_argument("--verification", default="", help="Verification commands and test results")
    add_parser.add_argument("--prevention", default="", help="Prevention invariant / golden rule")
    add_parser.add_argument("--files", default="", help="Comma-separated affected files")
    add_parser.add_argument("--severity", default="Major", choices=["Critical", "Major", "Minor", "Info"], help="Issue severity")
    add_parser.add_argument("--tags", default="", help="Comma-separated tags (e.g. Node,Auth,API,Vulkan)")
    add_parser.add_argument("--workspace", default="", help="Project workspace directory")
    add_parser.add_argument("--no-global", action="store_true", help="Skip synchronizing with global store")

    # Search subcommand
    search_parser = subparsers.add_parser("search", help="Search past solved issues")
    search_parser.add_argument("--query", required=True, help="Search query keywords")
    search_parser.add_argument("--workspace", default="", help="Project workspace directory")

    # Stats subcommand
    stats_parser = subparsers.add_parser("stats", help="Display troubleshooting database statistics")
    stats_parser.add_argument("--workspace", default="", help="Project workspace directory")

    # Update TOC subcommand
    toc_parser = subparsers.add_parser("update-toc", help="Regenerate Table of Contents in project log")
    toc_parser.add_argument("--workspace", default="", help="Project workspace directory")

    args = parser.parse_args()

    if args.action == "init":
        target = resolve_local_store(args.workspace)
        init_project_store(target, args.name)
        print(f"Created and initialized: {target}")
        return 0

    elif args.action == "add":
        add_entry(
            title=args.title,
            problem=args.problem,
            cause=args.cause,
            solution=args.solution,
            stack_trace=args.stack_trace,
            steps=args.steps,
            verification=args.verification,
            prevention=args.prevention,
            files=args.files,
            severity=args.severity,
            tags=args.tags,
            workspace_dir=args.workspace,
            sync_global=not args.no_global
        )
        print("Successfully logged fully detailed issue and solution!")
        return 0

    elif args.action == "search":
        matches = search_entries(args.query, args.workspace)
        if not matches:
            print(f"No previous issues found matching '{args.query}'.")
            return 0
        print(f"Found {len(matches)} matching previous issue(s):\n")
        for scope, path, entry in matches:
            print(f"[{scope}] {path}\n{entry}\n" + "=" * 60)
        return 0

    elif args.action == "stats":
        st = get_stats(args.workspace)
        print("Troubleshooting Knowledge Stats:")
        print(f"  - Local Project Store : {st['local_file']} ({st['local_issues']} issues)")
        print(f"  - Global Store        : {st['global_file']} ({st['global_issues']} issues)")
        return 0

    elif args.action == "update-toc":
        target = resolve_local_store(args.workspace)
        refresh_table_of_contents(target)
        print(f"Refreshed Table of Contents for: {target}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
