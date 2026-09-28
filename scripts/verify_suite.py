#!/usr/bin/env python3
"""
Pre-Flight & Post-Install Verification Suite for Antigravity-Agentic-Suite.
Validates all 404 Skills, 120 Specialized Agents, Global Rules, and Helper Scripts.
"""
import py_compile
import sys
import yaml
from pathlib import Path

def verify_repository():
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"
    agents_dir = repo_root / "agents"
    rules_dir = repo_root / "rules"

    skills = sorted([p for p in skills_dir.iterdir() if p.is_dir() and (p / "SKILL.md").exists()])
    agents = sorted(list(agents_dir.glob("*.md")))

    assert len(skills) == 410, f"Expected 410 skills, found {len(skills)}"
    assert len(agents) == 120, f"Expected 120 agents, found {len(agents)}"

    for s in skills:
        raw = (s / "SKILL.md").read_text(encoding="utf-8")
        assert raw.startswith("---"), f"Missing YAML frontmatter in skill {s.name}"
        parts = raw.split("---", 2)
        fm = yaml.safe_load(parts[1])
        assert fm.get("name") == s.name and fm.get("description"), f"Invalid metadata in skill {s.name}"

    for a in agents:
        raw = a.read_text(encoding="utf-8")
        assert raw.startswith("---"), f"Missing YAML frontmatter in agent {a.name}"
        parts = raw.split("---", 2)
        fm = yaml.safe_load(parts[1])
        assert fm.get("name") == a.stem and fm.get("description"), f"Invalid metadata in agent {a.name}"

    py_files = list(skills_dir.rglob("*.py"))
    for pf in py_files:
        py_compile.compile(str(pf), doraise=True)

    for rf in ["GEMINI.md", "CLAUDE.md", "AGENTS.md"]:
        assert (rules_dir / rf).exists(), f"Missing rule file {rf}"

    print("============================================================")
    print("  [PASS] VERIFICATION SUITE PASSED 100% (ZERO ERRORS)       ")
    print(f"  - Verified Skills       : {len(skills)}/410")
    print(f"  - Verified Subagents    : {len(agents)}/120")
    print(f"  - Verified Python Tools : {len(py_files)}/{len(py_files)}")
    print("  - Rule Configurations   : GEMINI.md | CLAUDE.md | AGENTS.md")
    print("============================================================")

if __name__ == "__main__":
    verify_repository()
