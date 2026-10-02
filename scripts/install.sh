#!/usr/bin/env bash
# Universal Installer for Osama Alzahrani's OmniAgentic Skills & Subagents Fleet.
# Supports: Antigravity IDE, Claude Desktop / Claude Code, OpenAI Codex CLI, Cursor, and Universal Workspace Adapter (.agents/).

set -e
TARGET="${1:-all}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SKILL_COUNT=$(find "$REPO_ROOT/skills" -mindepth 1 -maxdepth 1 -type d | wc -l)
AGENT_COUNT=$(find "$REPO_ROOT/agents" -name "*.md" | wc -l)

echo "============================================================"
echo "  OmniAgentic Multi-Agent Operating Suite - Installer       "
echo "  Author: Osama Alzahrani (Osama-Alzahrani-UQU)             "
echo "  Fleet: $SKILL_COUNT Verified Skills | $AGENT_COUNT Specialized Agents"
echo "============================================================"

install_antigravity() {
    echo "[+] Installing for Antigravity IDE & Gemini..."
    mkdir -p "$HOME/.gemini/config/skills" "$HOME/.gemini/ecc/agents"
    cp -r "$REPO_ROOT/skills/"* "$HOME/.gemini/config/skills/"
    cp -r "$REPO_ROOT/agents/"* "$HOME/.gemini/ecc/agents/"
    cp "$REPO_ROOT/rules/GEMINI.md" "$HOME/.gemini/config/GEMINI.md"
    echo "    [OK] Antigravity installation complete."
}

install_claude() {
    echo "[+] Installing for Claude Desktop & Claude Code..."
    mkdir -p "$HOME/.claude/skills" "$HOME/.claude/agents"
    cp -r "$REPO_ROOT/skills/"* "$HOME/.claude/skills/"
    cp -r "$REPO_ROOT/agents/"* "$HOME/.claude/agents/"
    cp "$REPO_ROOT/rules/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
    echo "    [OK] Claude installation complete."
}

install_codex() {
    echo "[+] Installing for OpenAI Codex CLI..."
    mkdir -p "$HOME/.codex/skills" "$HOME/.codex/agents"
    cp -r "$REPO_ROOT/skills/"* "$HOME/.codex/skills/"
    cp -r "$REPO_ROOT/agents/"* "$HOME/.codex/agents/"
    cp "$REPO_ROOT/rules/AGENTS.md" "$HOME/.codex/AGENTS.md"
    echo "    [OK] Codex installation complete."
}

install_cursor() {
    echo "[+] Installing for Cursor IDE..."
    mkdir -p "$HOME/.cursor/skills" "$HOME/.cursor/skills-cursor" "$HOME/.cursor/agents"
    cp -r "$REPO_ROOT/skills/"* "$HOME/.cursor/skills/"
    cp -r "$REPO_ROOT/skills/"* "$HOME/.cursor/skills-cursor/"
    cp -r "$REPO_ROOT/agents/"* "$HOME/.cursor/agents/"
    echo "    [OK] Cursor installation complete."
}

install_workspace() {
    echo "[+] Configuring Universal Workspace Adapter (.agents/)..."
    mkdir -p "$REPO_ROOT/.agents/skills" "$REPO_ROOT/.agents/rules"
    cp -r "$REPO_ROOT/skills/"* "$REPO_ROOT/.agents/skills/"
    cp "$REPO_ROOT/rules/GEMINI.md" "$REPO_ROOT/.agents/rules/GEMINI.md"
    cp "$REPO_ROOT/rules/AGENTS.md" "$REPO_ROOT/.agents/rules/AGENTS.md"
    echo "    [OK] Workspace adapter configured."
}

case "${TARGET,,}" in
    antigravity) install_antigravity ;;
    claude)      install_claude ;;
    codex)       install_codex ;;
    cursor)      install_cursor ;;
    workspace)   install_workspace ;;
    all|*)       install_antigravity; install_claude; install_codex; install_cursor; install_workspace ;;
esac

echo "[SUCCESS] All selected targets installed with 100% portability!"
