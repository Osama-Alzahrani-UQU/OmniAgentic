---
name: subagent-skill-inheritance
description: Subagent skill inheritance & portable execution
---

# Universal Sub-Agent Skill Inheritance & Portability Protocol

This skill enforces 100% skill inheritance, cross-platform portability, and explicit `SKILL.md` execution across all autonomous subagents, irrespective of the underlying model (Claude Opus 4.6, Claude 3.7 Sonnet, Gemini Pro, GPT-4o, OpenAI Codex) or runtime host (Antigravity IDE, Claude Desktop / Claude Code, OpenAI Codex CLI, Cursor).

---

## 1. Problem & Architecture

In multi-agent architectures, subagents frequently suffer from "skill blindness":
1. **System Prompt Isolation**: Subagents run with isolated context windows where global skills summaries may not be pre-injected.
2. **Model Caution & Rule Filters**: Overly cautious models (e.g., Claude Opus 4.6, Claude 3.7 Sonnet) avoid inspecting skill files unless explicitly directed.
3. **Platform Directory Fragmentation**: Different AI coding tools query different skill roots (`~/.gemini`, `~/.claude`, `~/.codex`, `.agents/`).

This protocol guarantees that whenever a subagent is invoked, it discovers, loads, and executes the required domain skill without failure.

---

## 2. Universal Runtime Path Resolution

Skills are organized uniformly across all platforms:

| Runtime / Host | Primary Skills Location | Fallback Location |
| :--- | :--- | :--- |
| **Workspace (Universal)** | `.agents/skills/<skill>/SKILL.md` | `skills/<skill>/SKILL.md` |
| **Antigravity / Gemini CLI** | `~/.gemini/config/skills/<skill>/SKILL.md` | `%USERPROFILE%\.gemini\config\skills\` |
| **Claude Code / Desktop** | `~/.claude/skills/<skill>/SKILL.md` | `%USERPROFILE%\.claude\skills\` |
| **OpenAI Codex CLI** | `~/.codex/skills/<skill>/SKILL.md` | `%USERPROFILE%\.codex\skills\` |
| **Cursor IDE** | `~/.cursor/skills/<skill>/SKILL.md` | `.cursor/skills/` or `.agents/skills/` |

---

## 3. Subagent Execution Invariants

Every subagent MUST follow this 4-step bootstrap loop:

### Step 1: Detect Bound Skill
Check if the parent agent passed an explicit skill file or skill name in the invocation `Prompt`:
- Example: `"Follow skill: ~/.gemini/config/skills/loop-debug/SKILL.md"`
- If explicitly specified, navigate immediately to Step 3.

### Step 2: Autonomous Domain Skill Lookup
If no skill was explicitly specified in the prompt, inspect the task domain:
- Code Review / Bug Hunting: `code-review-and-quality`, `code-completeness-debugger`
- Testing / Live Verification: `loop-debug`, `test-driven-development`
- Game Modding / Reverse Engineering: `mod-any-game`, `reverse-engineering`, `fal-assets`
- 3D / Assets: `asset-pipeline`, `fal-assets`, `kiln-author-asset`
- Video Editing: `video-editing`, `showcase-video`, `moneyprinterturbo-video`
- Web / Mobile Engineering: `frontend-patterns`, `react-patterns`, `flutter-dart-code-review`

### Step 3: Mandatory Read-Before-Act
Before writing, editing, or executing any commands:
- Call `view_file` on `<resolved_skill_path>/SKILL.md`.
- Read the entire procedure, checklists, and failure modes.

### Step 4: Technical Subagent Reporting
In the final report sent back to the parent agent (via `send_message` or return value):
- Explicitly state: `Applied Skill: <skill-name> (<file-path>)`.
- Confirm 100% adherence to the skill's instructions.
