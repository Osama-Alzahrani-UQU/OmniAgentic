#!/usr/bin/env python3
"""
Agency Hub: Dynamic Discovery and Dispatcher for 279 Specialized Agency Agents.
"""
import argparse
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

AGENTS_DIR = Path(r"C:\Users\goldl\.gemini\agents")
if not AGENTS_DIR.exists():
    AGENTS_DIR = Path.home() / ".gemini" / "agents"

DIVISIONS = {
    "Academic": ["anthropologist", "geographer", "historian", "narratologist", "psychologist", "statistician"],
    "Design": ["brand-guardian", "inclusive-visuals-specialist", "persona-walkthrough-specialist", "ux-researcher", "visual-storyteller", "whimsy-injector"],
    "Engineering": ["ai-engineer", "api-platform-engineer", "backend-architect", "cloud-architect", "frontend-developer", "fullstack-developer"],
    "GIS & Mapping": ["3d-scene-developer", "bim-gis-specialist", "cartography-designer", "drone-reality-mapping-specialist", "geoai-ml-engineer", "gis-analyst", "web-gis-developer"],
    "Game Dev": ["economy-designer", "game-audio-engineer", "game-designer", "roblox-avatar-creator", "roblox-experience-designer", "roblox-systems-scripter", "unreal-multiplayer-architect", "unreal-systems-engineer", "unreal-technical-artist", "unreal-world-builder"],
    "Spatial Computing": ["macos-spatial-metal-engineer", "terminal-integration-specialist", "visionos-spatial-engineer"],
    "Marketing & AEO": ["aeo-foundations-architect", "agentic-search-optimizer", "ai-citation-strategist", "content-creator", "growth-hacker", "seo-specialist", "social-media-strategist"],
    "Finance": ["bookkeeper-controller", "financial-analyst", "fpa-analyst", "investment-researcher", "tax-strategist"],
    "Security": ["ai-generated-code-auditor", "appsec-engineer", "cloud-security-architect", "penetration-tester", "security-architect"],
    "Testing": ["accessibility-auditor", "api-tester", "evidence-collector", "performance-benchmarker", "reality-checker", "test-automation-engineer"],
}

def search_agents(query: str):
    q = query.lower()
    matches = []
    for f in AGENTS_DIR.glob("*.md"):
        raw = f.read_text(encoding="utf-8")
        if q in f.stem.lower() or q in raw.lower()[:500]:
            parts = raw.split("---", 2)
            desc = ""
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1])
                    desc = fm.get("description", "")
                except Exception:
                    pass
            matches.append((f.stem, desc))
    print(f"=== Found {len(matches)} matching Agency Agents for '{query}' ===")
    for name, desc in sorted(matches):
        print(f"  * {name}: {desc[:90]}...")

def list_divisions():
    print("=== Agency Agents Enterprise Divisions (279 Total Agents) ===")
    for div, sample in sorted(DIVISIONS.items()):
        print(f"\n📂 {div}:")
        for s in sample:
            print(f"   - {s}")

def show_agent(name: str):
    target = AGENTS_DIR / f"{name}.md"
    if not target.exists():
        for f in AGENTS_DIR.glob("*.md"):
            if name.lower() in f.stem.lower():
                target = f
                break
    if not target.exists():
        print(f"Error: Agent '{name}' not found.")
        sys.exit(1)
    print(target.read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser(description="Agency Hub: Search and inspect 279 Agency Agents.")
    subparsers = parser.add_subparsers(dest="cmd")
    
    s_search = subparsers.add_parser("search", help="Search agents by keyword")
    s_search.add_argument("query", help="Keyword to search")
    
    subparsers.add_parser("divisions", help="List all 18 enterprise divisions")
    
    s_show = subparsers.add_parser("show", help="Show full agent markdown")
    s_show.add_argument("agent", help="Agent name or slug")
    
    args = parser.parse_args()
    if args.cmd == "search":
        search_agents(args.query)
    elif args.cmd == "divisions":
        list_divisions()
    elif args.cmd == "show":
        show_agent(args.agent)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
