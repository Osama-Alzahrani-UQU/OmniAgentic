<#
.SYNOPSIS
    Universal Installer for Osama Alzahrani's AI Agentic Skills & Subagents Fleet (404 Skills + 120 Agents).
    Supports: Antigravity IDE, Claude Desktop / Claude Code, and OpenAI Codex CLI.
#>
param(
    [ValidateSet("All", "Antigravity", "Claude", "Codex")]
    [string]$Target = "All"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  AI Agentic Skills & Subagents Suite - Universal Installer " -ForegroundColor Cyan
Write-Host "  Author: Osama Alzahrani (Osama-Alzahrani-UQU)             " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

function Install-Antigravity {
    Write-Host "`n[+] Installing for Antigravity IDE..." -ForegroundColor Green
    $AgConfig = Join-Path $HOME ".gemini\config"
    $AgSkills = Join-Path $AgConfig "skills"
    $AgAgents = Join-Path $HOME ".gemini\ecc\agents"
    New-Item -ItemType Directory -Force -Path $AgSkills | Out-Null
    New-Item -ItemType Directory -Force -Path $AgAgents | Out-Null
    Copy-Item -Path "$RepoRoot\skills\*" -Destination $AgSkills -Recurse -Force
    Copy-Item -Path "$RepoRoot\agents\*" -Destination $AgAgents -Recurse -Force
    Copy-Item -Path "$RepoRoot\rules\GEMINI.md" -Destination (Join-Path $AgConfig "GEMINI.md") -Force
    Write-Host "    [OK] Installed 404 Skills -> $AgSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed 120 Agents -> $AgAgents" -ForegroundColor Gray
    Write-Host "    [OK] Installed Global Rules -> $AgConfig\GEMINI.md" -ForegroundColor Gray
}

function Install-Claude {
    Write-Host "`n[+] Installing for Claude Desktop & Claude Code..." -ForegroundColor Green
    $ClaudeDir = Join-Path $HOME ".claude"
    $ClaudeSkills = Join-Path $ClaudeDir "skills"
    $ClaudeAgents = Join-Path $ClaudeDir "agents"
    New-Item -ItemType Directory -Force -Path $ClaudeSkills | Out-Null
    New-Item -ItemType Directory -Force -Path $ClaudeAgents | Out-Null
    Copy-Item -Path "$RepoRoot\skills\*" -Destination $ClaudeSkills -Recurse -Force
    Copy-Item -Path "$RepoRoot\agents\*" -Destination $ClaudeAgents -Recurse -Force
    Copy-Item -Path "$RepoRoot\rules\CLAUDE.md" -Destination (Join-Path $ClaudeDir "CLAUDE.md") -Force
    Write-Host "    [OK] Installed 404 Skills -> $ClaudeSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed 120 Agents -> $ClaudeAgents" -ForegroundColor Gray
    Write-Host "    [OK] Installed Global Rules -> $ClaudeDir\CLAUDE.md" -ForegroundColor Gray
}

function Install-Codex {
    Write-Host "`n[+] Installing for OpenAI Codex CLI..." -ForegroundColor Green
    $CodexDir = Join-Path $HOME ".codex"
    $CodexSkills = Join-Path $CodexDir "skills"
    $CodexAgents = Join-Path $CodexDir "agents"
    New-Item -ItemType Directory -Force -Path $CodexSkills | Out-Null
    New-Item -ItemType Directory -Force -Path $CodexAgents | Out-Null
    Copy-Item -Path "$RepoRoot\skills\*" -Destination $CodexSkills -Recurse -Force
    Copy-Item -Path "$RepoRoot\agents\*" -Destination $CodexAgents -Recurse -Force
    Copy-Item -Path "$RepoRoot\rules\AGENTS.md" -Destination (Join-Path $CodexDir "AGENTS.md") -Force
    Write-Host "    [OK] Installed 404 Skills -> $CodexSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed 120 Agents -> $CodexAgents" -ForegroundColor Gray
    Write-Host "    [OK] Installed Global Rules -> $CodexDir\AGENTS.md" -ForegroundColor Gray
}

if ($Target -eq "All" -or $Target -eq "Antigravity") { Install-Antigravity }
if ($Target -eq "All" -or $Target -eq "Claude")      { Install-Claude }
if ($Target -eq "All" -or $Target -eq "Codex")       { Install-Codex }

Write-Host "`n[SUCCESS] Installation completed 100%!" -ForegroundColor Green
