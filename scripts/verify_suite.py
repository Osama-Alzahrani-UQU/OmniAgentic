#!/usr/bin/env python3
"""
Pre-Flight & Post-Install Verification Suite for Antigravity-Agentic-Suite.
Validates all 443 Skills, 120 Specialized Agents, Zero-Duplication Invariants, Global Rules, and Helper Scripts.
"""
import hashlib
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

    assert len(skills) == 460, f"Expected 460 skills, found {len(skills)}"
    assert len(agents) == 147, f"Expected 147 agents, found {len(agents)}"

    seen_skill_names = set()
    seen_skill_descs = {}
    seen_skill_bodies = {}

    for s in skills:
        raw = (s / "SKILL.md").read_text(encoding="utf-8")
        assert raw.startswith("---"), f"Missing YAML frontmatter in skill {s.name}"
        parts = raw.split("---", 2)
        fm = yaml.safe_load(parts[1])
        name = fm.get("name")
        desc = " ".join(str(fm.get("description", "")).split()).lower()
        body_hash = hashlib.sha256(parts[2].strip().encode("utf-8")).hexdigest()

        assert name == s.name and desc, f"Invalid metadata in skill {s.name}"
        assert name not in seen_skill_names, f"Duplicate skill name detected: {name}"
        assert desc not in seen_skill_descs, f"Duplicate skill description in {name} and {seen_skill_descs[desc]}"
        assert body_hash not in seen_skill_bodies, f"Duplicate skill body in {name} and {seen_skill_bodies[body_hash]}"

        seen_skill_names.add(name)
        seen_skill_descs[desc] = name
        seen_skill_bodies[body_hash] = name

    seen_agent_names = set()
    seen_agent_descs = {}
    seen_agent_bodies = {}

    for a in agents:
        raw = a.read_text(encoding="utf-8")
        assert raw.startswith("---"), f"Missing YAML frontmatter in agent {a.name}"
        parts = raw.split("---", 2)
        fm = yaml.safe_load(parts[1])
        name = fm.get("name")
        desc = " ".join(str(fm.get("description", "")).split()).lower()
        body_hash = hashlib.sha256(parts[2].strip().encode("utf-8")).hexdigest()

        assert name == a.stem and desc, f"Invalid metadata in agent {a.name}"
        assert name not in seen_agent_names, f"Duplicate agent name detected: {name}"
        assert desc not in seen_agent_descs, f"Duplicate agent description in {name} and {seen_agent_descs[desc]}"
        assert body_hash not in seen_agent_bodies, f"Duplicate agent body in {name} and {seen_agent_bodies[body_hash]}"

        seen_agent_names.add(name)
        seen_agent_descs[desc] = name
        seen_agent_bodies[body_hash] = name

    py_files = list(skills_dir.rglob("*.py"))
    for pf in py_files:
        py_compile.compile(str(pf), doraise=True)

    for rf in ["GEMINI.md", "CLAUDE.md", "AGENTS.md"]:
        assert (rules_dir / rf).exists(), f"Missing rule file {rf}"

    print("============================================================")
    print("  [PASS] VERIFICATION SUITE PASSED 100% (ZERO ERRORS)       ")
    print(f"  - Verified Skills       : {len(skills)}/460 (0 Duplicates)")
    print(f"  - Verified Subagents    : {len(agents)}/147 (0 Duplicates)")
    print(f"  - Verified Python Tools : {len(py_files)}/{len(py_files)}")
    print("  - Rule Configurations   : GEMINI.md | CLAUDE.md | AGENTS.md")
    print("============================================================")

if __name__ == "__main__":
    verify_repository()

