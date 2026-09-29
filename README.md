# 🚀 OmniAgentic | Enterprise Multi-Agent Operating Suite

<p align="center">
  <img src="https://img.shields.io/badge/Total%20Skills-445%20Production%20Grade-0A84FF?style=for-the-badge&logo=anthropic&logoColor=white" alt="445 Skills" />
  <img src="https://img.shields.io/badge/Specialized%20Agents-145%20Verified-30D158?style=for-the-badge&logo=openai&logoColor=white" alt="145 Agents" />
  <img src="https://img.shields.io/badge/Token%20Savings-~19,000%20Tokens/Turn-FF9F0A?style=for-the-badge&logo=speedtest&logoColor=white" alt="Token Savings" />
  <img src="https://img.shields.io/badge/Target%20Platforms-Antigravity%20|%20Claude%20|%20Codex-BF5AF2?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="Platforms" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <img src="assets/banner.jpg" alt="OmniAgentic Framework Banner" width="100%" />
</p>

<p align="center">
  <b>Engineered & Maintained by <a href="https://github.com/Osama-Alzahrani-UQU">Osama Alzahrani</a></b><br>
  <span>Computer Science • Umm Al-Qura University</span><br>
  <sub>Integrated with pioneering open-source work by <b>Maciej Sitarzewski</b>, <b>Harry</b>, <b>Matthew Kissinger</b>, <b>Affaan Mustafa</b> & <b>Unity Technologies</b></sub>
</p>

<p align="center">
  <a href="#english-documentation">English Documentation</a> •
  <a href="#upstream-creators">Upstream Creators</a> •
  <a href="#agents-showcase">Agents Showcase</a> •
  <a href="#skills-catalog">Skills Catalog</a> •
  <a href="#installation--setup">Installation Guide</a> •
  <a href="#acknowledgments--credits">Acknowledgments</a> •
  <a href="CATALOG.md">Full Catalog</a> •
  <a href="AUTHORS.md">Authors & Credits</a> •
  <a href="#arabic-documentation">Arabic Documentation</a>
</p>

---

<a name="english-documentation"></a>
## 🌟 Executive Overview

The **OmniAgentic Suite** is a unified, enterprise-grade multi-agent operating framework that equips AI coding assistants (**Antigravity IDE**, **Claude Desktop / Claude Code**, and **OpenAI Codex CLI**) with **445 curated, production-tested engineering skills** and **145 autonomous specialized subagents**.

Engineered specifically to solve the common failure modes of modern agentic workflows (hallucinations, token bloat, forgotten instructions, dropped functions, and tool deadlocks), this suite implements a formal **Zero-Hallucination & Token-Efficiency Protocol** with an autonomous `Test -> Diagnose -> Fix -> Retest` pre-delivery verification loop.

### 🏆 Key Engineering Achievements
1. **Context-Window Token Compression (70% Reduction)**: Slashed prompt metadata from **112,154 characters down to 35,843 characters**, reclaiming over **~19,000 tokens per turn**. This eliminates context-budget starvation and prevents subagent drop-outs.
2. **Autonomous Pre-Delivery Debug Loop (`loop-debug`)**: Enforces an automated, closed-loop debug cycle where the agent autonomously runs diagnostics, compiles code, tests edge cases, and verifies 100% completion before delivering results to the user.
3. **Zero-Omission Sentinel (`request-completeness-sentinel`)**: Guarantees that every single user constraint, sub-task, and formatting rule is tracked and satisfied without truncated code, missing functions, or placeholder stubs (`TODO` / `pass`).
4. **Academic & Student Excellence Suite**: 14 purpose-built subagents designed for university coursework, literature reviews, active-recall study coaching, quantitative statistics, thesis LaTeX typesetting, and graduation capstone architecture.
5. **Universal Portability**: Identical, seamless execution across **Antigravity**, **Claude Desktop / Claude Code**, and **OpenAI Codex CLI** with cross-platform automated installers (`install.ps1` / `install.sh`).

---

<a name="upstream-creators"></a>
### 🌟 Upstream Creators & Open-Source Pioneers

OmniAgentic proudly builds upon, adapts, and integrates breakthrough open-source projects created by world-class software engineers and AI researchers:

<table align="center">
  <tr>
    <td align="center" width="160">
      <a href="https://github.com/msitarzewski">
        <img src="https://github.com/msitarzewski.png?size=80" width="80px;" alt="Maciej Sitarzewski" style="border-radius: 50%;" /><br />
        <sub><b>Maciej Sitarzewski</b></sub><br />
        <sub>@msitarzewski</sub>
      </a><br />
      <small><a href="https://github.com/msitarzewski/agency-agents">The Agency (Agency Agents)</a></small>
    </td>
    <td align="center" width="160">
      <a href="https://github.com/harry0703">
        <img src="https://github.com/harry0703.png?size=80" width="80px;" alt="Harry" style="border-radius: 50%;" /><br />
        <sub><b>Harry</b></sub><br />
        <sub>@harry0703</sub>
      </a><br />
      <small><a href="https://github.com/harry0703/MoneyPrinterTurbo">MoneyPrinterTurbo</a></small>
    </td>
    <td align="center" width="160">
      <a href="https://github.com/matthew-kissinger">
        <img src="https://github.com/matthew-kissinger.png?size=80" width="80px;" alt="Matthew Kissinger" style="border-radius: 50%;" /><br />
        <sub><b>Matthew Kissinger</b></sub><br />
        <sub>@matthew-kissinger</sub>
      </a><br />
      <small><a href="https://github.com/matthew-kissinger/kiln">Kiln (3D Engine)</a></small>
    </td>
    <td align="center" width="160">
      <a href="https://github.com/affaan-m">
        <img src="https://github.com/affaan-m.png?size=80" width="80px;" alt="Affaan Mustafa" style="border-radius: 50%;" /><br />
        <sub><b>Affaan Mustafa</b></sub><br />
        <sub>@affaan-m</sub>
      </a><br />
      <small><a href="https://github.com/affaan-m/everything-claude-code">Everything Claude Code</a></small>
    </td>
    <td align="center" width="160">
      <a href="https://github.com/Unity-Technologies">
        <img src="https://github.com/Unity-Technologies.png?size=80" width="80px;" alt="Unity Technologies" style="border-radius: 50%;" /><br />
        <sub><b>Unity Technologies</b></sub><br />
        <sub>@Unity-Technologies</sub>
      </a><br />
      <small><a href="https://github.com/Unity-Technologies/skills">Unity Official Skills</a></small>
    </td>
  </tr>
</table>

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph UserInterface["User & Harness Layer"]
        CLI["User Prompt / Terminal"]
        Rules["Global Rules Matrix
(GEMINI.md / CLAUDE.md / AGENTS.md)"]
    end

    subgraph CoreEngine["Agentic Execution Engine"]
        Supervisor["Supervisor & Task Router
(project-supervisor-orchestrator)"]
        Decomposer["DAG Task Decomposer
(task-decomposition-expert)"]
        ContextMgr["Context & Memory Curator
(context-manager)"]
    end

    subgraph AgentFleet["145 Specialized Domain Subagents"]
        direction TB
        Academic["🎓 Academic & Student Suite
(academic-researcher, exam-coach, latex-thesis)"]
        GameDev["🎮 Game Dev, Unreal & Roblox
(unreal-systems, roblox-scripter, godot, fivem)"]
        Spatial["🥽 Spatial Computing & GIS
(visionos, macos-metal, gis-analyst, 3d-scene)"]
        CloudDB["☁️ Cloud, DevOps & DBs
(docker, k8s, terraform, postgres, redis)"]
        CodeReview["🛡️ Language Reviewers & Resolvers
(python, rust, react, typescript, go, build-resolvers)"]
    end

    subgraph SkillsMatrix["445 Curated Production Skills"]
        SkillsHub["On-Demand Skill Hubs
(ecc-hub / agency-agents / skill-scout)"]
        ActiveSkills["Active Skills Engine
(TDD, API Design, Security, Git, Video, 3D)"]
    end

    subgraph QualityGate["Autonomous Verification Loop"]
        Verifier["loop-debug & code-completeness-debugger"]
        FactGuard["hallucination-fact-guard"]
        Delivery["100% Verified Delivery + Debug Confirmation"]
    end

    CLI --> Rules --> Supervisor
    Supervisor --> Decomposer --> ContextMgr
    ContextMgr --> AgentFleet
    AgentFleet <--> SkillsMatrix
    AgentFleet --> Verifier --> FactGuard --> Delivery
```

---

<a name="agents-showcase"></a>
## 🤖 145 Specialized Subagents Fleet

All 145 subagents are defined as structured personas located in `agents/`. They are invoked dynamically via `invoke_subagent` / `define_subagent` at zero baseline token overhead:

### 1. University Student & Academic Research Suite (14 Agents)
* **`academic-researcher`**: Searches and analyzes peer-reviewed literature, scholarly journals, and research methodologies.
* **`academic-research-synthesizer`**: Synthesizes multiple research papers into cohesive literature reviews, highlighting consensus and research gaps.
* **`academic-statistician`**: Quantitative research methodology, experimental design, power analysis, ANOVA, regression modeling, and statistical proofs.
* **`academic-narratologist`**: Narrative theory, story structure, hero's journey, character arcs, and literary analysis.
* **`academic-historian`**: Historiographical analysis, primary source evaluation, material culture, and historical periodization.
* **`academic-anthropologist`**: Cultural systems, ethnographic fieldwork, rituals, kinship dynamics, and qualitative inquiry.
* **`research-brief-generator`**: Transforms long textbooks, papers, and complex lectures into structured study outlines and executive briefs.
* **`exam-study-coach`**: University exam preparation coach utilizing active recall, Anki flashcard generation, and past-exam walkthroughs.
* **`algorithms-math-tutor`**: University CS and Math tutor for Data Structures, Algorithms, Big-O proofs, Discrete Math, and Linear Algebra.
* **`latex-thesis-specialist`**: Typesetting master for university graduation theses, IEEE/ACM papers, Beamer presentations, and KaTeX equations.
* **`capstone-graduation-advisor`**: End-to-end graduation project advisor (proposal, SRS documentation, UML/ERD modeling, and defense preparation).
* **`hypotheses-manager`**: Bias-isolated scientific agent that formulates, tracks, and evaluates hypotheses against experimental data.
* **`claim-auditor`**: Quantitative auditor that verifies every claim, statistic, formula, and citation against primary evidence.
* **`hackathon-ai-strategist`**: University hackathon strategist helping students scope winning MVPs and technical pitches under time pressure.

### 2. Meta-Agents for Agent Support & Orchestration (10 Agents)
* **`agent-expert`**: Meta-agent architect that designs, audits, and optimizes subagent system prompts, tool boundaries, and workflows.
* **`project-supervisor-orchestrator`**: Supervises multi-agent workflows, routes sub-tasks to specialist subagents, and verifies cross-agent integration.
* **`task-decomposition-expert`**: Decomposes large objectives into dependency-ordered DAG sub-tasks with strict I/O contracts.
* **`context-manager`**: Manages shared context across multi-agent workflows, pruning redundant history while preserving critical state.
* **`memory-extractor`**: Extracts durable architectural decisions, technical facts, and project patterns into persistent memory.
* **`query-clarifier`**: Refines underspecified user prompts into crisp, unambiguous technical specifications for downstream agents.
* **`historical-context-reviewer`**: Audits git history and prior design rationale before subagents modify legacy codebases.
* **`error-detective`**: Deep log and stack-trace analyzer that pinpoints root causes when subagent commands fail.
* **`url-context-validator`**: Validates URLs, citations, and documentation links cited by agents to eliminate broken or hallucinated links.
* **`hallucination-fact-guard`**: Cross-checks subagent code symbols, imports, and file paths against the real disk before delivery.

### 3. Game Engines, Unreal, Roblox & Spatial Computing (16 Agents)
* **Unreal Engine 5**: `unreal-systems-engineer` (C++/Blueprints/GAS), `unreal-multiplayer-architect` (Actor replication/NetDriver), `unreal-technical-artist` (Niagara/Nanite/Lumen/Materials), `unreal-world-builder` (Level streaming/World Partition).
* **Roblox Studio**: `roblox-systems-scripter` (Luau scripting/replication), `roblox-experience-designer` (monetization/game loops), `roblox-avatar-creator` (UGC/rigging).
* **Spatial Computing**: `visionos-spatial-engineer` (Apple Vision Pro/RealityKit), `macos-spatial-metal-engineer` (Metal/Swift 3D rendering).
* **Godot & FiveM**: `godot-architect` (Godot 4/GDScript/MCP), `fivem-redm-specialist` (CFX.re/VORP/QBCore), `game-modding-specialist` (Unity BepInEx/Harmony/IL2CPP), `lua-expert`, `economy-designer` (game tokenomics/currency sinks).

### 4. GIS, Mapping & Earth Science (4 Agents)
* **`gis-analyst`**: Spatial analysis, layer management, GeoJSON, PostGIS, QGIS/ArcGIS workflows.
* **`3d-scene-developer`**: Web 3D geographic scenes, Cesium, Three.js terrain rendering.
* **`cartography-designer`**: Map design, projection systems, symbology, and visual hierarchy.
* **`drone-reality-mapping-specialist`**: Photogrammetry, aerial point clouds, orthomosaics, and flight telemetry.

### 5. Creative Design, Whimsy & Growth Marketing (6 Agents)
* **`whimsy-injector`**: Micro-interactions, playful UI details, Easter eggs, delightful animations, and tactile feedback.
* **`persona-walkthrough-specialist`**: Cognitive walkthrough simulation from diverse user personas.
* **`brand-guardian`**: Visual identity, brand consistency, color harmony, and design systems.
* **`aeo-foundations-architect`**: AI Engine Optimization, llms.txt, AI-aware robots.txt, structured citations for LLMs.
* **`agentic-search-optimizer`**: WebMCP readiness, web agent discovery, and agentic task optimization.
* **`growth-hacker`**: Viral loops, conversion rate optimization, referral mechanics, and user activation funnels.

### 6. Reverse Engineering, Security & Forensics (7 Agents)
* **`reverse-engineering-specialist`**: Binary reverse engineering (x64dbg, Ghidra, IDA Pro, PE/ELF, assembly, Frida hooks).
* **`firmware-analyst`**: Embedded systems and IoT firmware extraction and reverse engineering (ARM, MIPS, x86/x64).
* **`windows-forensics-hunter`**: Windows OS internals, rootkit/malware hunting, persistence auditing, and system file recovery (DISM/SFC).
* **`windows-desktop-automator`**: Windows GUI and desktop automation engineer (Win32 API, UIAutomation, PowerShell, silent installers).
* **`electron-expert`**: Electron desktop application engineer for multi-process architecture and IPC security.
* **`tauri-expert`**: Lightweight desktop application engineer for Rust + WebView Tauri applications.
* **`codebase-archaeologist`**: Historical architectural intent extraction, legacy git excavation, and technical debt analysis.

### 7. Cloud, DevOps, Databases & Backend Frameworks (19 Agents)
* **Cloud & DevOps**: `docker-expert`, `kubernetes-architect`, `terraform-specialist`, `cloud-architect`, `github-actions-expert`, `observability-engineer`.
* **Databases & Caching**: `postgres-expert`, `redis-expert`, `mongodb-expert`, `vector-db-expert`, `prisma-expert`.
* **Backend & Realtime**: `nestjs-expert`, `nextjs-expert`, `tailwind-expert`, `graphql-expert`, `websocket-expert`, `kafka-expert`.
* **Data & AI Pipelines**: `prompt-engineer`, `langchain-expert`, `data-engineer`, `playwright-expert`.

### 8. Specialized Language Reviewers & Build Resolvers (69 Core Agents)
* **Build Error Resolvers (12)**: `build-error-resolver`, `cpp-build-resolver`, `dart-build-resolver`, `django-build-resolver`, `go-build-resolver`, `harmonyos-app-resolver`, `java-build-resolver`, `kotlin-build-resolver`, `pytorch-build-resolver`, `react-build-resolver`, `rust-build-resolver`, `swift-build-resolver`.
* **Code Reviewers (21)**: `code-reviewer`, `cpp-reviewer`, `csharp-reviewer`, `database-reviewer`, `django-reviewer`, `fastapi-reviewer`, `flutter-reviewer`, `fsharp-reviewer`, `go-reviewer`, `healthcare-reviewer`, `java-reviewer`, `kotlin-reviewer`, `mle-reviewer`, `network-config-reviewer`, `php-reviewer`, `python-reviewer`, `react-reviewer`, `rust-reviewer`, `swift-reviewer`, `typescript-reviewer`, `vue-reviewer`.
* **Architecture & Quality (36)**: `architect`, `code-architect`, `planner`, `spec-miner`, `security-reviewer`, `performance-optimizer`, `refactor-cleaner`, `silent-failure-hunter`, `tdd-guide`, and more.

*(Browse the complete alphabetical directory of all 145 agents in [CATALOG.md](CATALOG.md)).*

---

<a name="skills-catalog"></a>
## 🛠️ 445 Production Skills Catalog

All 445 skills in `skills/` have been audited for zero syntax errors, valid YAML frontmatters, and compressed descriptions to maintain context efficiency:

* **Core Operational Sentinels**: `loop-debug`, `code-completeness-debugger`, `request-completeness-sentinel`, `concise-responder`, `bilingual-clean-layout`, `end-to-end-executor`, `experience-learner`, `zero-duplicate-guard`.
* **Meta-Hubs & Ecosystem Bridges**: `ecc-hub` (ECC catalog), `agency-agents` (The Agency catalog), `skill-scout` (skill discovery).
* **Generative Media & Automated Video**: `moneyprinterturbo-video` (automated short-form video generation from prompts with TTS, subtitles, and stock footage), `fal-ai-media`, `manim-video`, `remotion-video-creation`.
* **Procedural 3D & Vision**: `kiln-author-asset`, `kiln-compose-scene`, `kiln-qa-asset`, `kiln-refine-asset`, `kiln-batch-dispatch`, `kiln-setup-workspace`.
* **Game Development (33 Official Unity Skills)**: URP RenderGraph, UI Toolkit, Netcode for GameObjects, Vivox Voice, In-App Purchases, NavMesh, SpriteAtlas, Audio Mixers, LevelPlay Ads.
* **Software Architecture & Patterns**: `backend-patterns`, `api-design`, `api-and-interface-design`, `architecture-decision-records`, `documentation-and-adrs`, `clean-architecture-ddd`, `contract-first`, `microservices-patterns`.
* **Testing & Quality Engineering**: `tdd-workflow`, `test-driven-development`, `e2e-testing`, `browser-qa`, `code-review-and-quality`, `pr-test-analyzer`, `mutation-testing`.
* **Product Management & Strategy (69 PM Skills)**: `create-prd`, `sprint-plan`, `customer-journey-map`, `lean-canvas`, `opportunity-solution-tree`, `brainstorm-okrs`, `prioritize-features`, `growth-loops`, `monetization-strategy`.
* **Full-Stack Frameworks**: React, Next.js, Vue, Nuxt, Angular, Flutter, Django, FastAPI, Spring Boot, Quarkus, NestJS, Rails, Laravel, Express.

---

<a name="installation--setup"></a>
## ⚙️ Installation & Platform Setup

### ⚡ One-Command Automatic Installation

#### Windows (PowerShell):
```powershell
# Install across All platforms (Antigravity, Claude, Codex)
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Target All

# Or target a specific environment:
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Target Antigravity
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Target Claude
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Target Codex
```

#### macOS / Linux (Bash):
```bash
chmod +x ./scripts/install.sh
./scripts/install.sh all        # or: antigravity | claude | codex
```

---

### 📖 Manual Setup Guides

#### 1. Antigravity IDE Setup
Antigravity automatically discovers skills and agents placed in the user configuration directory:
1. Copy the `skills/` folder to: `~/.gemini/config/skills/` (Windows: `%USERPROFILE%\.gemini\config\skills\`)
2. Copy the `agents/` folder to: `~/.gemini/ecc/agents/` (Windows: `%USERPROFILE%\.gemini\ecc\agents\`)
3. Copy `rules/GEMINI.md` to: `~/.gemini/config/GEMINI.md`
4. Verify installation:
   ```bash
   python scripts/verify_suite.py
   ```

#### 2. Claude Desktop & Claude Code Setup
1. Copy the `skills/` folder to: `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`)
2. Copy the `agents/` folder to: `~/.claude/agents/` (Windows: `%USERPROFILE%\.claude\agents\`)
3. Copy `rules/CLAUDE.md` to: `~/.claude/CLAUDE.md`
4. *(Optional for Claude Desktop)* Mount the filesystem via MCP by copying `configs/claude_desktop_config.example.json` to your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "agentic-suite": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "<PATH_TO_CLAUDE_DIR>/skills", "<PATH_TO_CLAUDE_DIR>/agents"]
       }
     }
   }
   ```

#### 3. OpenAI Codex CLI Setup
1. Copy the `skills/` folder to: `~/.codex/skills/` (Windows: `%USERPROFILE%\.codex\skills\`)
2. Copy the `agents/` folder to: `~/.codex/agents/` (Windows: `%USERPROFILE%\.codex\agents\`)
3. Copy `rules/AGENTS.md` to: `~/.codex/AGENTS.md`
4. Copy `configs/codex_config.example.toml` to: `~/.codex/config.toml`

---

### 📂 Repository File Tree

```
OmniAgentic/
├── skills/                     # 445 Production Engineering Skills
├── agents/                     # 145 Specialized Domain Subagents
├── rules/                      # Cross-Platform Operational Rules Matrix
│   ├── GEMINI.md               # Antigravity Global Rules
│   ├── CLAUDE.md               # Claude Desktop & Claude Code Rules
│   └── AGENTS.md               # OpenAI Codex CLI Rules
├── configs/                    # Ready-to-Use Platform Configuration Templates
│   ├── claude_desktop_config.example.json
│   └── codex_config.example.toml
├── scripts/                    # Automation & Verification Suite
│   ├── install.ps1             # Automated Windows PowerShell Installer
│   ├── install.sh              # Automated Linux/macOS Bash Installer
│   └── verify_suite.py         # 100% Pre-Flight Verification Script
├── CATALOG.md                  # Complete Categorized Directory of All Skills & Agents
├── LICENSE                     # MIT Open-Source License
└── README.md                   # Comprehensive Dual-Language Documentation
```

---

<a name="author--maintainer"></a>
## 👨‍💻 Author & Maintainer

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Osama-Alzahrani-UQU">
        <img src="https://github.com/Osama-Alzahrani-UQU.png?size=100" width="100px;" alt="Osama Alzahrani" style="border-radius: 50%;" /><br />
        <sub><b>Osama Alzahrani</b></sub>
      </a><br />
      <sub>Computer Science • Umm Al-Qura University</sub><br />
      <a href="https://github.com/Osama-Alzahrani-UQU">
        <img src="https://img.shields.io/badge/GitHub-@Osama--Alzahrani--UQU-181717?style=flat-square&logo=github" alt="GitHub Profile" />
      </a>
    </td>
  </tr>
</table>

---

<a name="acknowledgments--credits"></a>
## 🙏 Acknowledgments & Upstream Credits

This framework stands on the shoulders of giants. We express our sincere gratitude to the open-source engineering community and upstream contributors whose pioneering work made this unified suite possible:

* **[The Agency (Agency Agents)](https://github.com/msitarzewski/agency-agents)**: Created and maintained by **[Maciej Sitarzewski (msitarzewski)](https://github.com/msitarzewski)** (@msitarzewski) for the 270+ battle-tested agency agent personalities across 18 specialized enterprise divisions (GIS, Spatial Computing, Roblox, Unreal Engine 5, AEO, Whimsy Design, and Quantitative Research).
* **[MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)**: Created and maintained by **[Harry (harry0703)](https://github.com/harry0703)** (@harry0703) for the automated end-to-end AI video generation engine, Edge-TTS audio synthesis, stock footage orchestration, and Whisper subtitle synchronization.
* **[Unity Technologies Official Skills](https://github.com/Unity-Technologies/skills)**: Created and maintained by **Unity Technologies** and its engineering contributors (**[ziyiunity](https://github.com/ziyiunity)**, **[andresbayon](https://github.com/andresbayon)**, **[GabrielBelmonteUnity](https://github.com/GabrielBelmonteUnity)**, **[kimberleymday](https://github.com/kimberleymday)**, **[chris-addison](https://github.com/chris-addison)**, **[ewhittom](https://github.com/ewhittom)**, **[jli-u3d](https://github.com/jli-u3d)**, **[peterhall-unity3d](https://github.com/peterhall-unity3d)**, **[renanfagundes](https://github.com/renanfagundes)**, **[csantayanaUnity](https://github.com/csantayanaUnity)**, **[elham-saboori](https://github.com/elham-saboori)**, **[unity-at-github](https://github.com/unity-at-github)**) for the 33 official Unity 6+ game development, URP RenderGraph, UI Toolkit, Netcode multiplayer, and optimization skills.
* **[Kiln](https://github.com/matthew-kissinger/kiln)**: Created and maintained by **[Matthew Kissinger](https://github.com/matthew-kissinger)** (@matthew-kissinger) for the procedural 3D modeling engine, Three.js geometry recipes, and vision-in-the-loop rendering architecture.
* **[Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)**: Created and maintained by **[Affaan Mustafa](https://github.com/affaan-m)** (@affaan-m) and core contributors (**[haelyra](https://github.com/haelyra)**, **[pangerlkr](https://github.com/pangerlkr)**, **[gaurav0107](https://github.com/gaurav0107)**) for the foundational multi-agent concepts, specialized domain personas, and curated engineering skills catalog.
* **Anthropic & Claude Community**: For the pioneer prompt engineering patterns and Model Context Protocol (MCP) tooling ecosystem.
* **Open-Source AI Community**: For continuous benchmarks, defensive testing frameworks, and multi-agent coordination paradigms.

> *All original tool concepts, agent schemas, and community skills remain the intellectual property of their respective creators under their open-source licenses.*

---

## 📄 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---
---

<a name="arabic-documentation"></a>
# 🇸🇦 دليل التوثيق باللغة العربية (Arabic Documentation)

### 📌 نبذة تنفيذية عن المشروع
تعتبر منظومة **OmniAgentic** إطار عمل معماري متكامل للوكلاء البرمجيين، تم تصميمه وهندسته ليمنح بيئات ومساعدي الذكاء الاصطناعي (**Antigravity IDE** و **Claude Desktop / Claude Code** و **OpenAI Codex CLI**) ترسانة برمجية موحدة تضم **445 مهارة هندسية معتمدة** و **145 وكيلاً فرعياً تخصصياً**.

تم بناء هذه المنظومة خصيصاً للقضاء على التحديات والعيوب الشائعة في الوكلاء الحاليين (مثل: الهلوسة، استنزاف الرموز / Tokens، نسيان متطلبات المستخدم، الأكواد الناقصة أو المختصرة، وتوقف الجلسات)، من خلال تطبيق حلقة فحص وتصحيح ذاتية إلزامية (`Test -> Diagnose -> Fix -> Retest`) قبل تسليم أي كود.

### 🌟 أبرز الإنجازات التقنية والمعمارية
1. **ترشيد استهلاك الذاكرة والرموز بنسبة 70%**: تم تقليص حجم نصوص الأوصاف من **112,154 حرفاً إلى 35,843 حرفاً فقط**، مما وفر أكثر من **19,000 توكن في كل محادثة** ومنع استبعاد الوكلاء تلقائياً بسبب حد الذاكرة (`Context Budget Limits`).
2. **حلقة الفحص والتصحيح التلقائية (`loop-debug`)**: إلزام الوكيل بالدخول التلقائي في حلقة اختبار وتصحيح عبر أوامر الطرفية حتى يصبح البرنامج خالياً من الأخطاء ويعمل بنسبة 100% مع تأكيد صريح لنجاح الـ `Debug`.
3. **حارس الاكتمال الصارم (`request-completeness-sentinel`)**: حظر تسليم أي مشروع يحتوي على دوال ناقصة أو أكواد مختصرة (`TODO` أو `pass`)، وضمان تلبية كافة متطلبات المستخدم دون إسقاط أي تفصيل.
4. **حزمة الطالب والباحث الجامعي المتكاملة**: توفير 14 وكيلاً تخصصياً لدعم طلاب الجامعات في المراجعات الأدبية للبحوث، التحليل الإحصائي، الاستذكار الفعال، كتابة الرسائل الجامعية بـ `LaTeX`، وإعداد وتوثيق مشاريع التخرج بالكامل.
5. **توافق تشغيلي شامل**: تعمل المنظومة بنقرة واحدة عبر كافة المنصات الرائدة مع سكريبتات تثبيت آلية لنظامي ويندوز (`install.ps1`) ولينكس/ماك (`install.sh`).

---

### 📂 هيكل مستودع المشروع

```
OmniAgentic/
├── skills/                     # 445 مهارة برمجية وفنية جاهزة ومحدثة
├── agents/                     # 145 وكيلاً تخصصياً بصيغة Markdown
├── rules/                      # القواعد العامة الصارمة لكل منصة
│   ├── GEMINI.md               # قواعد Antigravity IDE العامة
│   ├── CLAUDE.md               # قواعد Claude Desktop & Claude Code
│   └── AGENTS.md               # قواعد OpenAI Codex CLI
├── configs/                    # قوالب الإعدادات الجاهزة للمنصات
│   ├── claude_desktop_config.example.json
│   └── codex_config.example.toml
├── scripts/                    # سكريبتات التثبيت والفحص الشامل
│   ├── install.ps1             # سكريبت التثبيت التلقائي لنظام ويندوز
│   ├── install.sh              # سكريبت التثبيت التلقائي لأنظمة لينكس وماك
│   └── verify_suite.py         # سكريبت الفحص والتحقق البرمجي بنسبة 100%
├── CATALOG.md                  # الفهرس التفصيلي لجميع المهارات والوكلاء
├── LICENSE                     # رخصة الاستخدام مفتوحة المصدر (MIT)
└── README.md                   # التوثيق الشامل ثنائي اللغة للمشروع
```

---

### 🛠️ دليل التثبيت السريع

#### لنظام ويندوز (PowerShell):
```powershell
# لتثبيت المنظومة على كافة البيئات (Antigravity و Claude و Codex):
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Target All
```

#### لأنظمة ماك ولينكس (Bash):
```bash
chmod +x ./scripts/install.sh
./scripts/install.sh all
```

---

### 👨‍💻 المطور والمشرف
* **أسامة الزهراني** (Osama Alzahrani)
* قسم علوم الحاسب الآلي • جامعة أم القرى
* حساب المستودع: `https://github.com/Osama-Alzahrani-UQU`

---

### 🙏 شكر وإسناد للمبتكرين والمصادر المفتوحة
تعتمد هذه المنظومة على جهود رائدة من نخبة من المطورين ومجتمع المصادر المفتوحة، ونتوجه بالعرفان والشكر والتقدير للأشخاص والمطورين الأصليين الذين بنينا على إبداعاتهم:
* **ماسيج سيتارزيفسكي (Maciej Sitarzewski - @msitarzewski)**: المبتكر والمطور لمشروع `The Agency (Agency Agents)` ومزود المنظومة بأكثر من 270 شخصية تخصصية ذكية عبر 18 قطاعاً مؤسسياً.
* **هاري (Harry - @harry0703)**: المبتكر والمطور لمشروع `MoneyPrinterTurbo` لمنظومة توليد وإنتاج الفيديو الذاتي المتقدم والمزامنة الصوتية عبر الذكاء الاصطناعي.
* **ماثيو كيسنجر (Matthew Kissinger - @matthew-kissinger)**: المبتكر والمطور لمشروع `Kiln` لنظام النمذجة الإجرائية ثلاثية الأبعاد والتوليد الهندسي التفاعلي.
* **عفان مصطفى (Affaan Mustafa - @affaan-m)** وفريقه: المبتكر والمطور لمشروع `Everything Claude Code (ECC)` للمفاهيم التأسيسية وترسانة المهارات البرمجية وهندسة الوكلاء.
* **فريق مهندسي Unity Technologies (@Unity-Technologies)**: المطورون الرسميون لحزمة مهارات محرك الألعاب `Unity 6` والشبكات متعددة اللاعبين ومعالجة الرسوميات.
* **مجتمع الذكاء الاصطناعي والمصادر المفتوحة**: لدعم بروتوكولات الوكلاء المتعددة وتطوير منظومة الأدوات المفتوحة.

---

### 📄 رخصة الاستخدام
هذا المشروع مرخص تحت رخصة **MIT** مفتوحة المصدر — راجع ملف [LICENSE](LICENSE) لمزيد من التفاصيل.
