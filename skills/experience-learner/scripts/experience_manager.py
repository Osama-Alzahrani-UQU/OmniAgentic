#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experience Manager Utility for Continuous Learning
Manages recording, indexing, and searching through persistent problem-solution logs
across global (~/.gemini/knowledge/) and workspace-level stores.
"""

import os
import sys
import argparse
from datetime import datetime

GLOBAL_STORE_DIR = r"C:\Users\goldl\.gemini\knowledge"
GLOBAL_STORE_FILE = os.path.join(GLOBAL_STORE_DIR, "troubleshooting_history.md")

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def ensure_store_exists():
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


def add_entry(title: str, problem: str, cause: str, solution: str, tags: str = "", workspace_dir: str = ""):
    """Add a structured problem-solution entry to the global and optionally local store."""
    ensure_store_exists()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    formatted_tags = " ".join([f"`[{t}]`" for t in tag_list]) if tag_list else "`[General]`"

    entry = (
        f"### [{timestamp}] {title}\n"
        f"- **Tags**: {formatted_tags}\n"
        f"- **Problem & Error**: {problem.strip()}\n"
        f"- **Root Cause**: {cause.strip()}\n"
        f"- **Verified Solution**: {solution.strip()}\n\n"
        f"---\n\n"
    )

    # 1. Append to global store
    with open(GLOBAL_STORE_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Recorded in Global Store: {GLOBAL_STORE_FILE}")

    # 2. Append to workspace local store if provided
    if workspace_dir and os.path.isdir(workspace_dir):
        local_gemini = os.path.join(workspace_dir, ".gemini")
        os.makedirs(local_gemini, exist_ok=True)
        local_file = os.path.join(local_gemini, "troubleshooting.md")
        with open(local_file, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"Recorded in Workspace Store: {local_file}")


def search_entries(query: str, workspace_dir: str = "") -> list:
    """Search for relevant entries in global and local stores."""
    ensure_store_exists()
    query_terms = query.lower().split()
    results = []

    files_to_search = [GLOBAL_STORE_FILE]
    if workspace_dir:
        local_file = os.path.join(workspace_dir, ".gemini", "troubleshooting.md")
        if os.path.exists(local_file):
            files_to_search.append(local_file)

    for fpath in files_to_search:
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        sections = content.split("### [")
        for sec in sections[1:]:
            full_sec = "### [" + sec
            lower_sec = full_sec.lower()
            if any(term in lower_sec for term in query_terms):
                results.append((fpath, full_sec.strip()))

    return results


def main():
    parser = argparse.ArgumentParser(description="Experience Manager for Continuous Learning")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # Add subcommand
    add_parser = subparsers.add_parser("add", help="Record a solved issue")
    add_parser.add_argument("--title", required=True, help="Title of the issue")
    add_parser.add_argument("--problem", required=True, help="Description of the problem / error")
    add_parser.add_argument("--cause", required=True, help="Root cause of the problem")
    add_parser.add_argument("--solution", required=True, help="Verified solution")
    add_parser.add_argument("--tags", default="", help="Comma-separated tags (e.g. Vulkan,DirectX,UAC)")
    add_parser.add_argument("--workspace", default="", help="Workspace directory for local logging")

    # Search subcommand
    search_parser = subparsers.add_parser("search", help="Search past solved issues")
    search_parser.add_argument("--query", required=True, help="Search query keywords")
    search_parser.add_argument("--workspace", default="", help="Optional workspace directory")

    # List subcommand
    list_parser = subparsers.add_parser("list", help="List all recorded issues")

    args = parser.parse_args()

    if args.action == "add":
        add_entry(args.title, args.problem, args.cause, args.solution, args.tags, args.workspace)
        print("Successfully logged issue and solution for future reference!")
        return 0

    elif args.action == "search":
        matches = search_entries(args.query, args.workspace)
        if not matches:
            print(f"No previous issues found matching '{args.query}'.")
            return 0
        print(f"Found {len(matches)} matching previous issue(s):\n")
        for path, entry in matches:
            print(f"Source: {path}\n{entry}\n" + "=" * 50)
        return 0

    elif args.action == "list":
        ensure_store_exists()
        with open(GLOBAL_STORE_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        titles = [l.strip() for l in lines if l.startswith("### [")]
        print(f"Total Recorded Issues: {len(titles)}")
        for t in titles:
            print(f"  - {t}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
