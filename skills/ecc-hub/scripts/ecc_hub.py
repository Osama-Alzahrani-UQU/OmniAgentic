#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ECC Hub & Agent Integrator for Antigravity
Provides instant search, discovery, and sub-agent invocation for ECC's
285+ engineering skills and 68 specialized agents.
"""

import os
import re
import sys
import json
import argparse

ECC_HOME = r"C:\Users\goldl\.gemini\ecc"
SKILLS_DIR = os.path.join(ECC_HOME, "skills")
AGENTS_DIR = os.path.join(ECC_HOME, "agents")

CONFLICTING_SKILLS = {
    "context-budget": "Conflicts with Sub-Agent Anti-Hallucination rule (forces token starvation and skipping files).",
    "verification-loop": "Conflicts with loop-debug (Claude Code stop-hook syntax). Use loop-debug instead.",
    "autonomous-loops": "Conflicts with end-to-end-executor and loop-debug. Use loop-debug instead.",
    "continuous-learning": "Conflicts with experience-learner. Use experience-learner instead.",
    "continuous-learning-v2": "Conflicts with experience-learner. Use experience-learner instead.",
    "delivery-gate": "Conflicts with request-completeness-sentinel and code-completeness-debugger.",
    "operator-approval-loop": "Conflicts with end-to-end-executor (stops and demands user permission).",
    "safety-guard": "Conflicts with Universal Mandate 1 (triggers trivial refusals).",
}

def load_skills():
    skills = []
    if not os.path.exists(SKILLS_DIR):
        return skills
    for name in os.listdir(SKILLS_DIR):
        sdir = os.path.join(SKILLS_DIR, name)
        if not os.path.isdir(sdir):
            continue
        sm = os.path.join(sdir, "SKILL.md")
        desc = ""
        if os.path.exists(sm):
            try:
                with open(sm, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                m = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
                if m:
                    desc = m.group(1).strip().strip('"').strip("'")
            except Exception:
                pass
        skills.append({
            "name": name,
            "path": sm,
            "description": desc,
            "is_conflicting": name in CONFLICTING_SKILLS,
            "conflict_reason": CONFLICTING_SKILLS.get(name, "")
        })
    return skills

def load_agents():
    agents = []
    if not os.path.exists(AGENTS_DIR):
        return agents
    for fname in os.listdir(AGENTS_DIR):
        if not fname.endswith(".md"):
            continue
        aname = fname[:-3]
        fpath = os.path.join(AGENTS_DIR, fname)
        desc = ""
        model = "inherit"
        tools = ""
        prompt = ""
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            m_desc = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
            if m_desc:
                desc = m_desc.group(1).strip().strip('"').strip("'")
            m_model = re.search(r"^model:\s*(.+)$", content, re.MULTILINE)
            if m_model:
                model = m_model.group(1).strip()
            m_tools = re.search(r"^tools:\s*(.+)$", content, re.MULTILINE)
            if m_tools:
                tools = m_tools.group(1).strip()
            parts = content.split("---", 2)
            if len(parts) >= 3:
                prompt = parts[2].strip()
        except Exception:
            pass
        agents.append({
            "name": aname,
            "path": fpath,
            "description": desc,
            "model": model,
            "tools": tools,
            "prompt": prompt
        })
    return agents

def cmd_search(query):
    query = query.lower()
    skills = load_skills()
    agents = load_agents()
    
    matched_skills = [s for s in skills if query in s["name"].lower() or query in s["description"].lower()]
    matched_agents = [a for a in agents if query in a["name"].lower() or query in a["description"].lower()]
    
    print(f"=== ECC Search Results for '{query}' ===")
    print(f"Matched Skills: {len(matched_skills)}")
    for s in matched_skills[:20]:
        status = "[CONFLICT - DEACTIVATED]" if s["is_conflicting"] else "[READY]"
        print(f"  {status} {s['name']:<32} - {s['description'][:70]}...")
    if len(matched_skills) > 20:
        print(f"  ... and {len(matched_skills) - 20} more skills.")
        
    print(f"\nMatched Agents: {len(matched_agents)}")
    for a in matched_agents[:15]:
        print(f"  [AGENT] {a['name']:<32} - {a['description'][:70]}...")
    if len(matched_agents) > 15:
        print(f"  ... and {len(matched_agents) - 15} more agents.")

def cmd_agent(name):
    agents = load_agents()
    agent = next((a for a in agents if a["name"] == name), None)
    if not agent:
        print(f"Error: Agent '{name}' not found.")
        sys.exit(1)
    print(f"=== ECC Agent Spec: {agent['name']} ===")
    print(f"Path: {agent['path']}")
    print(f"Description: {agent['description']}")
    print(f"Base Model: {agent['model']} (Antigravity tier: inherit/pro/flash)")
    print(f"\n--- System Prompt Preview ---")
    print(agent["prompt"][:600] + ("..." if len(agent["prompt"]) > 600 else ""))

def cmd_list_conflicts():
    print("=== ECC Conflicting / Deactivated Skills ===")
    for k, v in CONFLICTING_SKILLS.items():
        print(f"  - {k:<25}: {v}")

def main():
    parser = argparse.ArgumentParser(description="ECC Hub & Agent Integrator for Antigravity")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    p_search = subparsers.add_parser("search", help="Search ECC skills and agents")
    p_search.add_argument("query", help="Keyword or technology (e.g. flutter, react, rust, security)")
    
    p_agent = subparsers.add_parser("agent", help="Inspect an ECC agent specification")
    p_agent.add_argument("name", help="Agent name (e.g. code-reviewer, security-reviewer, architect)")
    
    subparsers.add_parser("conflicts", help="List neutralized conflicting skills")
    
    args = parser.parse_args()
    if args.command == "search":
        cmd_search(args.query)
    elif args.command == "agent":
        cmd_agent(args.name)
    elif args.command == "conflicts":
        cmd_list_conflicts()

if __name__ == "__main__":
    main()
