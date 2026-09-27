#!/usr/bin/env bash
# Universal Installer for Osama Alzahrani's AI Agentic Skills & Subagents Fleet (404 Skills + 120 Agents)
# Supports: Antigravity IDE, Claude Desktop / Claude Code, and OpenAI Codex CLI.

set -e
TARGET="${1:-all}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

install_antigravity() {
    echo "[+] Installing for Antigravity IDE..."
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

case "${TARGET,,}" in
    antigravity) install_antigravity ;;
    claude)      install_claude ;;
    codex)       install_codex ;;
    all|*)       install_antigravity; install_claude; install_codex ;;
esac

echo "[SUCCESS] All selected targets installed 100%!"
