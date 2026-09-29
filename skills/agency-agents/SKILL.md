---
name: agency-agents
description: On-demand bridge and catalog for 279 specialized Agency Agents across 18 enterprise divisions.
metadata:
  origin: upstream
  author: msitarzewski
  upstream: https://github.com/msitarzewski/agency-agents
---

# The Agency: 279 Specialized AI Agents (`agency-agents`)

The **Agency Agents** library provides access to **279 battle-tested, domain-specific AI specialist personas** organized across 18 enterprise divisions (Engineering, Security, GIS, Game Development, Spatial Computing, Marketing, Design, Academic, Sales, Support, Testing, Finance, etc.).

All agents are installed and accessible on this machine at:
- `C:\Users\goldl\.gemini\agents\` (Gemini CLI / Antigravity)
- `C:\Users\goldl\.claude\agents\` (Claude Code)
- `C:\Users\goldl\.codex\agents\` (Codex)
- `C:\Users\goldl\agency-agents\` (Full Source Repository)

---

## 1. Quick Discovery via CLI

Search or inspect any agent across the 18 divisions using the included `agency_hub.py` tool:

```powershell
# Search for agents by keyword (e.g. gis, roblox, unreal, marketing, visionos, whimsy)
python "C:\Users\goldl\.gemini\config\skills\agency-agents\scripts\agency_hub.py" search "unreal"

# List all available divisions
python "C:\Users\goldl\.gemini\config\skills\agency-agents\scripts\agency_hub.py" divisions

# View full agent persona details and mission
python "C:\Users\goldl\.gemini\config\skills\agency-agents\scripts\agency_hub.py" show "visionos-spatial-engineer"
```

---

## 2. Launching an Agency Specialist

When a user request requires deep domain mastery in a specific agency discipline:
1. Locate the agent file at `C:\Users\goldl\.gemini\agents\<agent-slug>.md`.
2. Inspect or view the prompt instructions.
3. Spawn a specialized subagent via `invoke_subagent` using the agent's persona prompt.
4. The subagent executes with full domain depth and returns a comprehensive report.

---

## 3. Supported Divisions Catalog

| Division | Highlights |
| :--- | :--- |
| **GIS & Mapping** | `gis-analyst`, `3d-scene-developer`, `cartography-designer`, `drone-reality-mapping-specialist` |
| **Spatial Computing** | `visionos-spatial-engineer`, `macos-spatial-metal-engineer`, `terminal-integration-specialist` |
| **Game Dev** | `unreal-systems-engineer`, `unreal-multiplayer-architect`, `roblox-systems-scripter`, `economy-designer` |
| **Design & UX** | `whimsy-injector`, `persona-walkthrough-specialist`, `brand-guardian`, `visual-storyteller` |
| **Marketing & AEO** | `aeo-foundations-architect`, `agentic-search-optimizer`, `growth-hacker`, `content-creator` |
| **Finance** | `finance-fpa-analyst`, `investment-researcher`, `tax-strategist`, `bookkeeper-controller` |
| **Academic** | `statistician`, `narratologist`, `historian`, `anthropologist`, `psychologist` |
