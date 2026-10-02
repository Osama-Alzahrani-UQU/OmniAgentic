<#
.SYNOPSIS
    Universal Installer for Osama Alzahrani's OmniAgentic Skills & Subagents Fleet.
    Supports: Antigravity IDE, Claude Desktop / Claude Code, OpenAI Codex CLI, Cursor IDE, and Universal Workspace Adapter (.agents/).
#>
param(
    [ValidateSet("All", "Antigravity", "Claude", "Codex", "Cursor", "Workspace")]
    [string]$Target = "All"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

$SkillCount = (Get-ChildItem -Path "$RepoRoot\skills" -Directory).Count
$AgentCount = (Get-ChildItem -Path "$RepoRoot\agents" -File -Filter "*.md").Count

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  OmniAgentic Multi-Agent Operating Suite - Installer       " -ForegroundColor Cyan
Write-Host "  Author: Osama Alzahrani (Osama-Alzahrani-UQU)             " -ForegroundColor Cyan
Write-Host "  Fleet: $SkillCount Verified Skills | $AgentCount Specialized Agents " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

function Install-Antigravity {
    Write-Host "`n[+] Installing for Antigravity IDE & Gemini..." -ForegroundColor Green
    $AgConfig = Join-Path $HOME ".gemini\config"
    $AgSkills = Join-Path $AgConfig "skills"
    $AgAgents = Join-Path $HOME ".gemini\ecc\agents"
    New-Item -ItemType Directory -Force -Path $AgSkills | Out-Null
    New-Item -ItemType Directory -Force -Path $AgAgents | Out-Null
    Copy-Item -Path "$RepoRoot\skills\*" -Destination $AgSkills -Recurse -Force
    Copy-Item -Path "$RepoRoot\agents\*" -Destination $AgAgents -Recurse -Force
    Copy-Item -Path "$RepoRoot\rules\GEMINI.md" -Destination (Join-Path $AgConfig "GEMINI.md") -Force
    Write-Host "    [OK] Installed $SkillCount Skills -> $AgSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed $AgentCount Agents -> $AgAgents" -ForegroundColor Gray
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
    Write-Host "    [OK] Installed $SkillCount Skills -> $ClaudeSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed $AgentCount Agents -> $ClaudeAgents" -ForegroundColor Gray
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
    Write-Host "    [OK] Installed $SkillCount Skills -> $CodexSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed $AgentCount Agents -> $CodexAgents" -ForegroundColor Gray
    Write-Host "    [OK] Installed Global Rules -> $CodexDir\AGENTS.md" -ForegroundColor Gray
}

function Install-Cursor {
    Write-Host "`n[+] Installing for Cursor IDE..." -ForegroundColor Green
    $CursorDir = Join-Path $HOME ".cursor"
    $CursorSkills = Join-Path $CursorDir "skills"
    $CursorSkillsAlt = Join-Path $CursorDir "skills-cursor"
    $CursorAgents = Join-Path $CursorDir "agents"
    New-Item -ItemType Directory -Force -Path $CursorSkills | Out-Null
    New-Item -ItemType Directory -Force -Path $CursorSkillsAlt | Out-Null
    New-Item -ItemType Directory -Force -Path $CursorAgents | Out-Null
    Copy-Item -Path "$RepoRoot\skills\*" -Destination $CursorSkills -Recurse -Force
    Copy-Item -Path "$RepoRoot\skills\*" -Destination $CursorSkillsAlt -Recurse -Force
    Copy-Item -Path "$RepoRoot\agents\*" -Destination $CursorAgents -Recurse -Force
    Write-Host "    [OK] Installed $SkillCount Skills -> $CursorSkills" -ForegroundColor Gray
    Write-Host "    [OK] Installed $AgentCount Agents -> $CursorAgents" -ForegroundColor Gray
}

function Install-Workspace {
    Write-Host "`n[+] Configuring Universal Workspace Adapter (.agents/)..." -ForegroundColor Green
    $WsAgentsDir = Join-Path $RepoRoot ".agents"
    $WsSkillsDir = Join-Path $WsAgentsDir "skills"
    $WsRulesDir  = Join-Path $WsAgentsDir "rules"
    New-Item -ItemType Directory -Force -Path $WsRulesDir | Out-Null
    Copy-Item -Path "$RepoRoot\rules\GEMINI.md" -Destination (Join-Path $WsRulesDir "GEMINI.md") -Force
    Copy-Item -Path "$RepoRoot\rules\AGENTS.md" -Destination (Join-Path $WsRulesDir "AGENTS.md") -Force
    if (-not (Test-Path $WsSkillsDir)) {
        New-Item -ItemType Junction -Path $WsSkillsDir -Target "$RepoRoot\skills" | Out-Null
    }
    Write-Host "    [OK] Workspace Adapter configured (Junction) -> $WsAgentsDir" -ForegroundColor Gray
}

if ($Target -eq "All" -or $Target -eq "Antigravity") { Install-Antigravity }
if ($Target -eq "All" -or $Target -eq "Claude")      { Install-Claude }
if ($Target -eq "All" -or $Target -eq "Codex")       { Install-Codex }
if ($Target -eq "All" -or $Target -eq "Cursor")      { Install-Cursor }
if ($Target -eq "All" -or $Target -eq "Workspace")   { Install-Workspace }

Write-Host "`n[SUCCESS] All platforms fully synchronized with 100% portability!" -ForegroundColor Green
