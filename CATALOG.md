# Complete Catalog: 404 Skills & 120 Specialized Agents | الفهرس الشامل للمهارات والوكلاء
This catalog lists every verified skill and specialized subagent included in the suite.
---
## Part 1: 120 Specialized Agents (`agents/`)
| # | Agent Name | Description |
| :--- | :--- | :--- |
| 1 | **`a11y-architect`** | Accessibility Architect specializing in WCAG 2.2 compliance for Web and Native platforms. Use PROACTIVELY when designing UI components, establishing design systems, or auditing code for inclusive user experiences. |
| 2 | **`academic-research-synthesizer`** | Synthesize findings across multiple academic papers into structured literature reviews, highlighting consensus and research gaps. |
| 3 | **`academic-researcher`** | Find and analyze scholarly sources, peer-reviewed research papers, citations, and academic methodologies. |
| 4 | **`agent-evaluator`** | Evaluates agent output against 5-axis quality rubric (accuracy, completeness, clarity, actionability, conciseness). Use after any non-trivial task when the user wants a quality assessment, or when the agent-self-evaluation skill is active. Produces structured scorecard with evidence and improvement suggestions. |
| 5 | **`agent-expert`** | Meta-agent architect that designs, audits, and optimizes specialized subagent prompts, tool boundaries, and workflows. |
| 6 | **`algorithms-math-tutor`** | University Computer Science and Mathematics tutor specializing in Data Structures, Algorithms, Big-O analysis, Discrete Math, Linear Algebra, and Probability. |
| 7 | **`arabic-localization-specialist`** | Game and software Arabic localization engineer specializing in RTL layout mirroring, Arabic glyph shaping, HarfBuzz/Fribidi integration, font asset injection, and context-aware translation. |
| 8 | **`architect`** | Software architecture specialist for system design, scalability, and technical decision-making. Use PROACTIVELY when planning new features, refactoring large systems, or making architectural decisions. |
| 9 | **`build-error-resolver`** | Build and TypeScript error resolution specialist. Use PROACTIVELY when build fails or type errors occur. Fixes build/type errors only with minimal diffs, no architectural edits. Focuses on getting the build green quickly. |
| 10 | **`capstone-graduation-advisor`** | University graduation and capstone project advisor guiding proposal writing, SRS documentation, UML/architecture diagrams, milestone planning, and defense prep. |
| 11 | **`chief-of-staff`** | Personal communication chief of staff that triages email, Slack, LINE, and Messenger. Classifies messages into 4 tiers (skip/info_only/meeting_info/action_required), generates draft replies, and enforces post-send follow-through via hooks. Use when managing multi-channel communication workflows. |
| 12 | **`claim-auditor`** | Quantitative and factual auditor that verifies claims, statistics, formulas, and citations in reports against primary evidence. |
| 13 | **`cloud-architect`** | Expert cloud architect specializing in AWS/Azure/GCP/OCI multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. Masters serverless, microservices, security, compliance, and disaster recovery. Use PROACTIVELY for cloud architecture, cost optimization, migration planning, or multi-cloud strategies. |
| 14 | **`code-architect`** | Designs feature architectures by analyzing existing codebase patterns and conventions, then providing implementation blueprints with concrete files, interfaces, data flow, and build order. |
| 15 | **`code-explorer`** | Deeply analyzes existing codebase features by tracing execution paths, mapping architecture layers, and documenting dependencies to inform new development. |
| 16 | **`code-reviewer`** | Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code. MUST BE USED for all code changes. |
| 17 | **`code-simplifier`** | Simplifies and refines code for clarity, consistency, and maintainability while preserving behavior. Focus on recently modified code unless instructed otherwise. |
| 18 | **`comment-analyzer`** | Analyze code comments for accuracy, completeness, maintainability, and comment rot risk. |
| 19 | **`context-manager`** | Manages shared context across multi-agent workflows, pruning redundant tokens while preserving critical execution state. |
| 20 | **`conversation-analyzer`** | Use this agent when analyzing conversation transcripts to find behaviors worth preventing with hooks. Triggered by /hookify without arguments. |
| 21 | **`cpp-build-resolver`** | C++ build, CMake, and compilation error resolution specialist. Fixes build errors, linker issues, and template errors with minimal changes. Use when C++ builds fail. |
| 22 | **`cpp-reviewer`** | Expert C++ code reviewer specializing in memory safety, modern C++ idioms, concurrency, and performance. Use for all C++ code changes. MUST BE USED for C++ projects. |
| 23 | **`csharp-reviewer`** | Expert C# code reviewer specializing in .NET conventions, async patterns, security, nullable reference types, and performance. Use for all C# code changes. MUST BE USED for C# projects. |
| 24 | **`dart-build-resolver`** | Dart/Flutter build, analysis, and dependency error resolution specialist. Fixes `dart analyze` errors, Flutter compilation failures, pub dependency conflicts, and build_runner issues with minimal, surgical changes. Use when Dart/Flutter builds fail. |
| 25 | **`data-engineer`** | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and cloud-native data platforms. Use PROACTIVELY for data pipeline design, analytics infrastructure, or modern data stack implementation. |
| 26 | **`database-reviewer`** | PostgreSQL database specialist for query optimization, schema design, security, and performance. Use PROACTIVELY when writing SQL, creating migrations, designing schemas, or troubleshooting database performance. Incorporates Supabase best practices. |
| 27 | **`django-build-resolver`** | Django/Python build, migration, and dependency error resolution specialist. Fixes pip/Poetry errors, migration conflicts, import errors, Django configuration issues, and collectstatic failures with minimal changes. Use when Django setup or startup fails. |
| 28 | **`django-reviewer`** | Expert Django code reviewer specializing in ORM correctness, DRF patterns, migration safety, security misconfigurations, and production-grade Django practices. Use for all Django code changes. MUST BE USED for Django projects. |
| 29 | **`doc-updater`** | Documentation and codemap specialist. Use PROACTIVELY for updating codemaps and documentation. Generates docs/CODEMAPS/*, updates READMEs and guides. Backs the /update-codemaps and /update-docs commands. |
| 30 | **`docker-expert`** | Expert in all aspects of Docker, including containerization, image creation, and orchestration. |
| 31 | **`docs-lookup`** | When the user asks how to use a library, framework, or API or needs up-to-date code examples, use Context7 MCP to fetch current documentation and return answers with examples. Invoke for docs/API/setup questions. |
| 32 | **`e2e-runner`** | End-to-end testing specialist using Vercel Agent Browser (preferred) with Playwright fallback. Use PROACTIVELY for generating, maintaining, and running E2E tests. Manages test journeys, quarantines flaky tests, uploads artifacts (screenshots, videos, traces), and ensures critical user flows work. |
| 33 | **`electron-expert`** | Specializes in building cross-platform desktop applications using Electron. Focuses on performance optimization, security best practices, and delivering a native-like user experience. |
| 34 | **`error-detective`** | Analyzes complex logs, stack traces, and distributed failure patterns to pinpoint root causes when subagent commands fail. |
| 35 | **`exam-study-coach`** | University exam preparation coach specializing in active recall, Anki spaced-repetition flashcards, practice quizzes, and step-by-step problem walkthroughs. |
| 36 | **`fastapi-reviewer`** | Reviews FastAPI applications for async correctness, dependency injection, Pydantic schemas, security, OpenAPI quality, testing, and production readiness. |
| 37 | **`firmware-analyst`** | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. Masters firmware extraction, analysis, and vulnerability research for routers, IoT devices, automotive systems, and industrial controllers. Use PROACTIVELY for firmware security audits, IoT penetration testing, or embedded systems research. |
| 38 | **`fivem-redm-specialist`** | FiveM and RedM (CFX.re) server/client architect specializing in VORP Core, QBCore, ESX, CitizenFX Lua/JS/C#, NUI interfaces, oxmysql, and statebag synchronization. |
| 39 | **`flutter-reviewer`** | Flutter and Dart code reviewer. Reviews Flutter code for widget best practices, state management patterns, Dart idioms, performance pitfalls, accessibility, and clean architecture violations. Library-agnostic — works with any state management solution and tooling. |
| 40 | **`fsharp-reviewer`** | Expert F# code reviewer specializing in functional idioms, type safety, pattern matching, computation expressions, and performance. Use for all F# code changes. MUST BE USED for F# projects. |
| 41 | **`game-modding-specialist`** | Advanced game modding architect for Unity (BepInEx, HarmonyX, IL2CPP, Mono), Unreal Engine (UE4SS, Pak/UAsset), and native C++/C# runtime injection. |
| 42 | **`gan-evaluator`** | GAN Harness — Evaluator agent. Tests the live running application via Playwright, scores against rubric, and provides actionable feedback to the Generator. |
| 43 | **`gan-generator`** | GAN Harness — Generator agent. Implements features according to the spec, reads evaluator feedback, and iterates until quality threshold is met. |
| 44 | **`gan-planner`** | GAN Harness — Planner agent. Expands a one-line prompt into a full product specification with features, sprints, evaluation criteria, and design direction. |
| 45 | **`github-actions-expert`** | Expert in GitHub Actions for automating workflows and CI/CD processes. |
| 46 | **`go-build-resolver`** | Go build, vet, and compilation error resolution specialist. Fixes build errors, go vet issues, and linter warnings with minimal changes. Use when Go builds fail. |
| 47 | **`go-reviewer`** | Expert Go code reviewer specializing in idiomatic Go, concurrency patterns, error handling, and performance. Use for all Go code changes. MUST BE USED for Go projects. |
| 48 | **`godot-architect`** | Godot 4.x Engine architect and GDScript specialist. Masters scene tree composition, custom signals, shaders, physics, tilemaps, and direct integration with the Godot MCP server. |
| 49 | **`graphql-expert`** | Expert in GraphQL API design, query optimization, and implementation. Master introspection, schemas, and GraphQL best practices. Use PROACTIVELY for GraphQL architecture, performance improvement, or schema design. |
| 50 | **`hackathon-ai-strategist`** | University hackathon and competition strategist for ideating, scoping, and building winning MVPs and technical pitches. |
| 51 | **`hallucination-fact-guard`** | Meta-agent verification sentinel that audits subagent outputs against actual filesystem paths, code symbols, imports, and factual evidence to prevent hallucinations. |
| 52 | **`harmonyos-app-resolver`** | HarmonyOS application development expert specializing in ArkTS and ArkUI. Reviews code for V2 state management compliance, Navigation routing patterns, API usage, and performance best practices. Use for HarmonyOS/OpenHarmony projects. |
| 53 | **`harness-optimizer`** | Improve local agent-harness configuration reliability and cost using eval-driven grading (pass@k/pass^k) derived from the eval-harness skill. |
| 54 | **`healthcare-reviewer`** | Reviews healthcare application code for clinical safety, CDSS accuracy, PHI compliance, and medical data integrity. Specialized for EMR/EHR, clinical decision support, and health information systems. |
| 55 | **`historical-context-reviewer`** | Reviews git history, commit rationale, and prior architectural context before subagents modify existing codebases. |
| 56 | **`homelab-architect`** | Designs home and small-lab network plans from hardware inventory, goals, and operator experience level, with safe staged changes and rollback guidance. |
| 57 | **`hypotheses-manager`** | Bias-isolated scientific agent that formulates, tracks, and evaluates hypotheses against experimental evidence. |
| 58 | **`java-build-resolver`** | Java/Maven/Gradle build, compilation, and dependency error resolution specialist. Automatically detects Spring Boot or Quarkus and applies framework-specific fixes. Fixes build errors, Java compiler errors, and Maven/Gradle issues with minimal changes. Use when Java builds fail. |
| 59 | **`java-reviewer`** | Expert Java code reviewer for Spring Boot and Quarkus projects. Automatically detects the framework and applies the appropriate review rules. Covers layered architecture, JPA/Panache, MongoDB, security, and concurrency. MUST BE USED for all Java code changes. |
| 60 | **`kafka-expert`** | Write highly efficient, scalable, and fault-tolerant Kafka architectures. Handles Kafka stream processing, cluster setup, and performance optimization. Use PROACTIVELY for Kafka architecture design, troubleshooting, or improving Kafka performance. |
| 61 | **`kotlin-build-resolver`** | Kotlin/Gradle build, compilation, and dependency error resolution specialist. Fixes build errors, Kotlin compiler errors, and Gradle issues with minimal changes. Use when Kotlin builds fail. |
| 62 | **`kotlin-reviewer`** | Kotlin and Android/KMP code reviewer. Reviews Kotlin code for idiomatic patterns, coroutine safety, Compose best practices, clean architecture violations, and common Android pitfalls. |
| 63 | **`kubernetes-architect`** | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. Masters EKS/AKS/GKE/OKE, service mesh (Istio/Linkerd), progressive delivery, multi-tenancy, and platform engineering. Handles security, observability, cost optimization, and developer experience. Use PROACTIVELY for K8s architecture, GitOps implementation, or cloud-native platform design. |
| 64 | **`langchain-expert`** | Expert in LangChain with focus on document processing, pipeline construction, and optimization. |
| 65 | **`latex-thesis-specialist`** | Academic LaTeX and BibTeX specialist for university theses, IEEE/ACM/Springer research papers, Beamer slides, and KaTeX mathematical typesetting. |
| 66 | **`loop-operator`** | Operate autonomous agent loops, monitor progress, and intervene safely when loops stall. |
| 67 | **`lua-expert`** | Write efficient and idiomatic Lua code, mastering the language features, patterns, and performance optimization. Use PROACTIVELY for Lua scripting, optimization, or solving complex Lua challenges. |
| 68 | **`marketing-agent`** | Marketing strategist and copywriter for campaign planning, audience research, positioning, copy creation, and content review. Covers landing pages, email sequences, social posts, ad copy, short-form video scripts, and content calendars. Use when the user wants to plan or execute a product launch or marketing campaign. |
| 69 | **`memory-extractor`** | Extracts durable technical facts, architectural decisions, and project patterns into structured long-term agent memory. |
| 70 | **`mle-reviewer`** | Production machine-learning engineering reviewer for data contracts, feature pipelines, training reproducibility, offline/online evaluation, model serving, monitoring, and rollback. Use when ML, MLOps, model training, inference, feature store, or evaluation code changes. |
| 71 | **`mongodb-expert`** | Master MongoDB operations, schema design, performance optimization, and data modeling. Handles indexing, aggregations, and replication. Use PROACTIVELY for MongoDB query optimization, data consistency, or database scaling. |
| 72 | **`nestjs-expert`** | Expert in building scalable and efficient applications using the NestJS framework. Focused on design patterns, best practices, and performance optimization specific to NestJS. |
| 73 | **`network-architect`** | Designs enterprise or multi-site network architecture from requirements, using existing network skills for focused routing, validation, automation, and troubleshooting detail. |
| 74 | **`network-config-reviewer`** | Reviews router and switch configurations for security, correctness, stale references, risky change-window commands, and missing operational guardrails. |
| 75 | **`network-troubleshooter`** | Diagnoses network connectivity, routing, DNS, interface, and policy symptoms with a read-only OSI-layer workflow and evidence-backed root cause summary. |
| 76 | **`nextjs-expert`** | Expert in Next.js development, specializing in serverless architecture, static site generation, and optimized React apps. |
| 77 | **`observability-engineer`** | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows. Use PROACTIVELY for monitoring infrastructure, performance optimization, or production reliability. |
| 78 | **`opensource-forker`** | Fork any project for open-sourcing. Copies files, strips secrets and credentials (20+ patterns), replaces internal references with placeholders, generates .env.example, and cleans git history. First stage of the opensource-pipeline skill. |
| 79 | **`opensource-packager`** | Generate complete open-source packaging for a sanitized project. Produces CLAUDE.md, setup.sh, README.md, LICENSE, CONTRIBUTING.md, and GitHub issue templates. Makes any repo immediately usable with Claude Code. Third stage of the opensource-pipeline skill. |
| 80 | **`opensource-sanitizer`** | Verify an open-source fork is fully sanitized before release. Scans for leaked secrets, PII, internal references, and dangerous files using 20+ regex patterns. Generates a PASS/FAIL/PASS-WITH-WARNINGS report. Second stage of the opensource-pipeline skill. Use PROACTIVELY before any public release. |
| 81 | **`performance-optimizer`** | Performance analysis and optimization specialist. Use PROACTIVELY for identifying bottlenecks, optimizing slow code, reducing bundle sizes, and improving runtime performance. Profiling, memory leaks, render optimization, and algorithmic improvements. |
| 82 | **`php-reviewer`** | Expert PHP code reviewer specializing in PSR-12 compliance, PHP type system, Eloquent ORM patterns, security, and performance. Use for all PHP code changes. MUST BE USED for PHP projects. |
| 83 | **`planner`** | Expert planning specialist for complex features and refactoring. Use PROACTIVELY when users request feature implementation, architectural changes, or complex refactoring. Automatically activated for planning tasks. |
| 84 | **`playwright-expert`** | Expert in Playwright testing for modern web applications. Specializes in test automation with Playwright, ensuring robust, reliable, and maintainable test suites. |
| 85 | **`postgres-expert`** | Expert in PostgreSQL database management and optimization, handling complex SQL queries, indexing strategies, and ensuring high-performance database systems. |
| 86 | **`pr-test-analyzer`** | Review pull request test coverage quality and completeness, with emphasis on behavioral coverage and real bug prevention. |
| 87 | **`prisma-expert`** | Write efficient, type-safe, and maintainable database queries using Prisma. Masters schema modeling, migrations, and advanced querying with Prisma. Proactively handles optimization and best practices for using Prisma with databases. |
| 88 | **`project-supervisor-orchestrator`** | Supervises multi-agent execution pipelines, routes tasks to specialist subagents, and verifies end-to-end integration. |
| 89 | **`prompt-engineer`** | Expert prompt engineer specializing in advanced prompting techniques, LLM optimization, and AI system design. Masters chain-of-thought, constitutional AI, and production prompt strategies. Use when building AI features, improving agent performance, or crafting system prompts. |
| 90 | **`python-reviewer`** | Expert Python code reviewer specializing in PEP 8 compliance, Pythonic idioms, type hints, security, and performance. Use for all Python code changes. MUST BE USED for Python projects. |
| 91 | **`pytorch-build-resolver`** | PyTorch runtime, CUDA, and training error resolution specialist. Fixes tensor shape mismatches, device errors, gradient issues, DataLoader problems, and mixed precision failures with minimal changes. Use when PyTorch training or inference crashes. |
| 92 | **`query-clarifier`** | Translates broad or ambiguous tasks into crisp, unambiguous technical specifications so subagents execute with zero guesswork. |
| 93 | **`rag-pipeline-reviewer`** | Reviews RAG (Retrieval-Augmented Generation) pipelines for retrieval quality, chunking strategy, embedding choices, and evaluation coverage. Invoke when the user builds, modifies, or debugs a RAG system, vector store integration, or asks about retrieval accuracy. |
| 94 | **`react-build-resolver`** | Diagnose and fix React build failures across Vite, webpack, Next.js, CRA, Parcel, esbuild, and Bun. Handles JSX/TSX compile errors, hydration mismatches, server/client component boundary failures, missing types, and bundler-specific configuration issues with minimal, surgical changes. MUST BE USED when a React build fails. |
| 95 | **`react-reviewer`** | Expert React/JSX code reviewer specializing in hook correctness, render performance, server/client component boundaries, accessibility, and React-specific security. Use for any change touching .tsx/.jsx files or React component logic. MUST BE USED for React projects. |
| 96 | **`redis-expert`** | Expert in Redis for in-memory data storage, caching, and real-time analytics. |
| 97 | **`refactor-cleaner`** | Dead code cleanup and consolidation specialist. Use PROACTIVELY for removing unused code, duplicates, and refactoring. Runs analysis tools (knip, depcheck, ts-prune) to identify dead code and safely removes it. |
| 98 | **`research-brief-generator`** | Transform complex research questions or academic material into structured study briefs and executive academic outlines. |
| 99 | **`reverse-engineering-specialist`** | Binary reverse engineering and dynamic analysis specialist mastering x64dbg, Ghidra, IDA Pro, PE/ELF internals, assembly (x86/x64/ARM), API hooking, and Frida instrumentation. |
| 100 | **`rust-build-resolver`** | Rust build, compilation, and dependency error resolution specialist. Fixes cargo build errors, borrow checker issues, and Cargo.toml problems with minimal changes. Use when Rust builds fail. |
| 101 | **`rust-reviewer`** | Expert Rust code reviewer specializing in ownership, lifetimes, error handling, unsafe usage, and idiomatic patterns. Use for all Rust code changes. MUST BE USED for Rust projects. |
| 102 | **`security-reviewer`** | Security vulnerability detection and remediation specialist. Use PROACTIVELY after writing code that handles user input, authentication, API endpoints, or sensitive data. Flags secrets, SSRF, injection, unsafe crypto, and OWASP Top 10 vulnerabilities. |
| 103 | **`seo-specialist`** | SEO specialist for technical SEO audits, on-page optimization, structured data, Core Web Vitals, and content/keyword mapping. Use for site audits, meta tag reviews, schema markup, sitemap and robots issues, and SEO remediation plans. |
| 104 | **`silent-failure-hunter`** | Review code for silent failures, swallowed errors, bad fallbacks, and missing error propagation. |
| 105 | **`spec-miner`** | Extracts behavioral specs from existing codebases for OpenSpec. Produces flat Requirement and Invariant blocks with structured metadata (entities, enforced, id, test anchors). Outputs openspec/specs/<capability>/spec.md. Fully self-bootstrapping — no dependency on codebase-onboarding. Use when onboarding a brownfield project to spec-driven development. |
| 106 | **`swift-build-resolver`** | Swift/Xcode build, compilation, and dependency error resolution specialist. Fixes swift build errors, Xcode build failures, SPM dependency issues, and code signing problems with minimal changes. Use when Swift builds fail. |
| 107 | **`swift-reviewer`** | Expert Swift code reviewer specializing in protocol-oriented design, value semantics, ARC memory management, Swift Concurrency, and idiomatic patterns. Use for all Swift code changes. MUST BE USED for Swift projects. |
| 108 | **`tailwind-expert`** | Expert in Tailwind CSS for efficient and responsive styling of web projects, utilizing utility-first approaches and responsive design principles. |
| 109 | **`task-decomposition-expert`** | Decomposes complex objectives into dependency-ordered DAG sub-tasks with explicit input/output contracts for subagents. |
| 110 | **`tauri-expert`** | Expert in Tauri for building cross-platform desktop applications leveraging web technologies. |
| 111 | **`tdd-guide`** | Test-Driven Development specialist enforcing write-tests-first methodology. Use PROACTIVELY when writing new features, fixing bugs, or refactoring code. Ensures 80%+ test coverage. |
| 112 | **`terraform-specialist`** | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles complex module design, multi-cloud deployments, GitOps workflows, policy as code, and CI/CD integration. Covers migration strategies, security best practices, and modern IaC ecosystems. Use PROACTIVELY for advanced IaC, state management, or infrastructure automation. |
| 113 | **`type-design-analyzer`** | Analyze type design for encapsulation, invariant expression, usefulness, and enforcement. |
| 114 | **`typescript-reviewer`** | Expert TypeScript/JavaScript code reviewer specializing in type safety, async correctness, Node/web security, and idiomatic patterns. Use for all TypeScript and JavaScript code changes. MUST BE USED for TypeScript/JavaScript projects. |
| 115 | **`url-context-validator`** | Validates URLs, references, and external documentation links cited by agents to prevent broken or hallucinated links. |
| 116 | **`vector-db-expert`** | Expert in Vector Databases, handling indexing, querying, and optimization of vector data. |
| 117 | **`vue-reviewer`** | Expert Vue.js code reviewer specializing in Composition API correctness, reactivity pitfalls, component architecture, template security, and Vue-specific performance. Use for any change touching .vue, .ts/.js files with Vue imports, or Vue ecosystem code (Pinia, Vue Router, Nuxt). MUST BE USED for Vue projects. |
| 118 | **`websocket-expert`** | Specializes in WebSocket protocol, implementation, and application. Provides expertise for real-time data exchange using WebSockets. |
| 119 | **`windows-desktop-automator`** | Windows GUI and desktop automation engineer specializing in Win32 API, UIAutomation, PowerShell, PyWinAuto, WPF/WinForms, and silent unattended software deployment. |
| 120 | **`windows-forensics-hunter`** | Windows OS internals, malware forensics, and system repair specialist. Masters persistence hunting (Registry, WMI, Scheduled Tasks, Services), process memory inspection, and DISM/SFC recovery. |

---
## Part 2: 404 Production Skills (`skills/`)
| # | Skill Name | Description |
| :--- | :--- | :--- |
| 1 | **`ab-test-analysis`** | Analyze A/B test results with statistical significance, sample size validation, confidence intervals. |
| 2 | **`accessibility`** | Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA. |
| 3 | **`adaptive-ui-designer`** | Specializes in designing domain-adaptive user interfaces (e.g., Gaming, SaaS, E-commerce. |
| 4 | **`agent-architecture-audit`** | Full-stack diagnostic for agent and LLM applications. |
| 5 | **`agent-eval`** | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate. |
| 6 | **`agent-harness-construction`** | Design and optimize AI agent action spaces, tool definitions. |
| 7 | **`agent-introspection-debugging`** | Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery. |
| 8 | **`agent-payment-x402`** | Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets. |
| 9 | **`agent-self-evaluation`** | Use after completing any non-trivial task. |
| 10 | **`agent-sort`** | Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks. |
| 11 | **`agentic-engineering`** | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. |
| 12 | **`agentic-os`** | Build persistent multi-agent operating systems on Claude Code. |
| 13 | **`ai-first-engineering`** | Engineering operating model for teams where AI agents generate a large share of implementation output. |
| 14 | **`ai-model-trainer`** | Equips agents and sub-agents with specialized expertise in training and fine-tuning AI models (LLMs, VLMs. |
| 15 | **`ai-regression-testing`** | Regression testing strategies for AI-assisted development. |
| 16 | **`algorithmic-art`** | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. |
| 17 | **`analyze-feature-requests`** | Analyze and prioritize a list of feature requests by theme, strategic alignment, impact, effort, and risk. |
| 18 | **`android-clean-architecture`** | Clean Architecture patterns for Android and Kotlin Multiplatform projects , module structure, dependency rules. |
| 19 | **`angular-developer`** | Generates Angular code and provides architectural guidance. |
| 20 | **`ansoff-matrix`** | Generate an Ansoff Matrix analysis mapping growth strategies across market penetration, market development. |
| 21 | **`api-and-interface-design`** | Internal software interface design , module boundaries, class contracts, TypeScript interfaces, SDK ergonomics. |
| 22 | **`api-connector-builder`** | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. |
| 23 | **`api-design`** | RESTful HTTP API design patterns , resource naming, HTTP status codes, pagination, query filtering. |
| 24 | **`architecture-decision-records`** | Format, record, and maintain Architecture Decision Records (ADRs) using standardized MADR templates for. |
| 25 | **`article-writing`** | Write articles, guides, blog posts, tutorials, newsletter issues. |
| 26 | **`automation-audit-ops`** | Evidence-first automation inventory and overlap audit workflow for ECC. |
| 27 | **`autonomous-agent-harness`** | Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations. |
| 28 | **`backend-patterns`** | Backend architecture patterns, API design, database optimization, and. Use when building or reviewing Node. |
| 29 | **`beachhead-segment`** | Identify the first beachhead market segment for a product launch. |
| 30 | **`benchmark`** | Use this skill to measure performance baselines, detect regressions before/after PRs. |
| 31 | **`benchmark-methodology`** | Use after competitive-platform-analysis has produced a tiered competitor set. |
| 32 | **`benchmark-optimization-loop`** | Use when the user asks to make something faster, try many variants, run recursive optimization. |
| 33 | **`bilingual-clean-layout`** | Enforces clean line separation and empty-line paragraph isolation (Split & Continuation Rule) between. |
| 34 | **`blender-motion-state-inspection`** | Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact. |
| 35 | **`blueprint`** | Turn a one-line objective into a step-by-step construction plan for multi-session. |
| 36 | **`brainstorm-experiments-existing`** | Design experiments to test assumptions for an existing product , prototypes, A/B tests, spikes. |
| 37 | **`brainstorm-experiments-new`** | Design lean startup experiments (pretotypes) for a new product. |
| 38 | **`brainstorm-ideas-existing`** | Brainstorm product ideas for an existing product using multi-perspective ideation from PM, Designer. |
| 39 | **`brainstorm-ideas-new`** | Brainstorm feature ideas for a new product in initial discovery from PM, Designer, and Engineer perspectives. |
| 40 | **`brainstorm-okrs`** | Brainstorm team-level OKRs aligned with company objectives . |
| 41 | **`brand-discovery`** | Use when a brand needs to discover or articulate its identity through structured multi-session interviews. |
| 42 | **`brand-guidelines`** | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from. |
| 43 | **`brand-voice`** | Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy. |
| 44 | **`browser-qa`** | Use this skill to automate visual testing and UI interaction verification using browser automation after. |
| 45 | **`browser-testing-with-devtools`** | Tests in real browsers via Chrome DevTools MCP. |
| 46 | **`bun-runtime`** | Bun as runtime, package manager, bundler, and test runner. |
| 47 | **`business-model`** | Generate a Business Model Canvas with all 9 building blocks. |
| 48 | **`canary-watch`** | Use this skill to monitor and verify a deployed URL after releases , checks HTTP endpoints, SSE streams. |
| 49 | **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. |
| 50 | **`carrier-relationship-management`** | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance. |
| 51 | **`ci-cd-and-automation`** | Automates CI/CD pipeline setup. |
| 52 | **`cisco-ios-patterns`** | Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement. |
| 53 | **`ck`** | Persistent per-project memory for Claude Code. |
| 54 | **`claude-devfleet`** | Orchestrate multi-agent coding tasks via Claude DevFleet , plan projects. |
| 55 | **`click-path-audit`** | Trace every user-facing button/touchpoint through its full state change sequence to find bugs where. |
| 56 | **`clickhouse-io`** | ClickHouse database patterns, query optimization, analytics. |
| 57 | **`code-completeness-debugger`** | Audits and debugs the entire project before user delivery to detect and complete any missing functions. |
| 58 | **`code-mentor`** | Dedicated programming assistant and educational mentor. |
| 59 | **`code-review`** | Deep bug hunting and defect discovery in code changes , verify edge cases, logic flaws, race conditions. |
| 60 | **`code-review-and-quality`** | Multi-axis quality gate for PRs and commits , assesses code architecture, style conventions, readability. |
| 61 | **`code-simplification`** | Simplifies code for clarity. |
| 62 | **`code-tour`** | Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. |
| 63 | **`codebase-onboarding`** | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map. |
| 64 | **`codebase-reverse-engineer`** | Equips agents and sub-agents with advanced software reverse engineering capabilities: architectural. |
| 65 | **`codehealth-mcp`** | Real-time structural Code Health via CodeScene MCP , review before edits, verify score deltas after changes. |
| 66 | **`coding-standards`** | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. |
| 67 | **`cohort-analysis`** | Perform cohort analysis on user engagement data , retention curves, feature adoption trends. |
| 68 | **`competitive-battlecard`** | Create sales-ready competitive battlecards comparing your product against a specific competitor , positioning. |
| 69 | **`competitive-platform-analysis`** | Use when scoping a competitive landscape , identifying, categorising. |
| 70 | **`competitive-report-structure`** | Use after benchmark-methodology has produced scored competitor profile cards. |
| 71 | **`competitor-analysis`** | Analyze competitors with strengths, weaknesses, and differentiation opportunities. |
| 72 | **`compose-multiplatform-patterns`** | Compose Multiplatform and Jetpack Compose patterns for KMP projects , state management, navigation, theming. |
| 73 | **`concise-responder`** | Enforces ultra-short, direct, and minimal user-facing responses (1-2 lines max) after 100% completion. |
| 74 | **`config-gc`** | Garbage collection for your Claude Code configuration. |
| 75 | **`configure-ecc`** | Guide ECC installation, update, or reconfiguration from inside Claude Code, Codex. |
| 76 | **`connections-optimizer`** | Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations. |
| 77 | **`constraint-driven-development`** | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. |
| 78 | **`content-engine`** | Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters. |
| 79 | **`content-hash-cache-pattern`** | Cache expensive file processing results using SHA-256 content hashes , path-independent, auto-invalidating. |
| 80 | **`context-engineering`** | Optimizes agent context setup. |
| 81 | **`continuous-agent-loop`** | Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. |
| 82 | **`contract-first`** | Use when multiple consumers and providers must evolve an API or event schema without field drift. |
| 83 | **`cost-aware-llm-pipeline`** | Cost optimization patterns for LLM API usage , model routing by task complexity, budget tracking, retry logic. |
| 84 | **`cost-tracking`** | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. |
| 85 | **`council`** | Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. |
| 86 | **`council-multi-model`** | Add one optional external Codex critique after the existing council has produced a decision draft. |
| 87 | **`counterparty-channel-discipline`** | Per-channel strict prompts, mention gating, silent observation. |
| 88 | **`cpp-coding-standards`** | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). |
| 89 | **`cpp-testing`** | Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest. |
| 90 | **`create-prd`** | Create a Product Requirements Document using a comprehensive 8-section template covering problem, objectives. |
| 91 | **`crosspost`** | Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. |
| 92 | **`csharp-testing`** | C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests. |
| 93 | **`customer-billing-ops`** | Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery. |
| 94 | **`customer-journey-map`** | Create an end-to-end customer journey map with stages, touchpoints, emotions, pain points, and opportunities. |
| 95 | **`customs-trade-compliance`** | Codified expertise for customs documentation, tariff classification, duty optimization. |
| 96 | **`dart-flutter-patterns`** | Production-ready Dart and Flutter patterns covering null safety, immutable state, async composition. |
| 97 | **`dashboard-builder`** | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. |
| 98 | **`data-scraper-agent`** | Build a fully automated AI-powered data collection agent for any public source , job boards, prices, news. |
| 99 | **`data-throughput-accelerator`** | Use when large data ingestion, backfill, export, ETL, warehouse loading, manifest catch-up. |
| 100 | **`database-migrations`** | Database migration best practices for schema changes, data migrations, rollbacks. |
| 101 | **`debugging-and-error-recovery`** | Guides systematic root-cause debugging. |
| 102 | **`deep-research`** | Multi-source deep research using firecrawl and exa MCPs. |
| 103 | **`defi-amm-security`** | Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. |
| 104 | **`deployment-patterns`** | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies. |
| 105 | **`deprecation-and-migration`** | Manages deprecation and migration. |
| 106 | **`design-system`** | Use this skill to generate or audit design systems, check visual consistency. |
| 107 | **`desktop-automator`** | Enables desktop and GUI automation on Windows. |
| 108 | **`dev-team`** | Simulate a collaborative dev team session where multiple role-based personas (PM, Architect, Developer. |
| 109 | **`django-celery`** | Django + Celery async task patterns , configuration, task design, beat scheduling, retries, canvas workflows. |
| 110 | **`django-patterns`** | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware. |
| 111 | **`django-security`** | Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention. |
| 112 | **`django-tdd`** | Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage. |
| 113 | **`django-verification`** | Verification loop for Django projects: migrations, linting, tests with coverage, security scans. |
| 114 | **`dmux-workflows`** | Multi-agent orchestration using dmux (tmux pane manager for AI agents). |
| 115 | **`docker-patterns`** | Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security. |
| 116 | **`documentation-and-adrs`** | Comprehensive technical documentation engineering , system overviews, developer guides, READMEs. |
| 117 | **`documentation-lookup`** | Use up-to-date library and framework docs via Context7 MCP instead of training data. |
| 118 | **`dotnet-patterns`** | Idiomatic C# and .NET patterns, conventions, dependency injection, async/await. Use when writing or reviewing C# / . |
| 119 | **`doubt-driven-development`** | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. |
| 120 | **`draft-nda`** | Draft a detailed Non-Disclosure Agreement between two parties covering information types, jurisdiction. |
| 121 | **`dummy-dataset`** | Generate realistic dummy datasets for testing with customizable columns, constraints, and output formats (CSV. |
| 122 | **`dynamic-workflow-mode`** | Design task-local harnesses, eval gates. |
| 123 | **`e2e-testing`** | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management. |
| 124 | **`ecc-guide`** | Guide users through ECC's current agents, skills, commands, hooks, rules, install profiles. |
| 125 | **`ecc-hub`** | On-demand bridge and catalog for the Everything Coding Companion (ECC) suite and 120 specialized domain agents. |
| 126 | **`ecc-recipes`** | Map a described workflow to the right ECC command-GROUP with run-order and stop condition. |
| 127 | **`ecc-tools-cost-audit`** | Evidence-first ECC Tools burn and billing audit workflow. |
| 128 | **`email-ops`** | Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. |
| 129 | **`end-to-end-executor`** | Ensures tasks are completed 100% autonomously end-to-end without leaving intermediate steps, scripts. |
| 130 | **`energy-procurement`** | Codified expertise for electricity and gas procurement, tariff optimization, demand charge management. |
| 131 | **`enterprise-agent-ops`** | Operate long-lived agent workloads with observability, security boundaries, and lifecycle management. |
| 132 | **`error-handling`** | Patterns for robust error handling across TypeScript, Python, and Go. |
| 133 | **`esign-field-placement`** | Deterministic method for placing signature, date. |
| 134 | **`eval-harness`** | Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles. |
| 135 | **`evm-token-decimals`** | Prevent silent decimal mismatch bugs across EVM chains. |
| 136 | **`exa-search`** | Neural search via Exa MCP for web, code, and company research. |
| 137 | **`experience-learner`** | Automatically records encountered technical issues, bugs. |
| 138 | **`fal-ai-media`** | Unified media generation via fal.ai MCP — image, video, and audio. |
| 139 | **`fastapi-patterns`** | FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers. |
| 140 | **`finance-billing-ops`** | Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. |
| 141 | **`flox-environments`** | Create reproducible, cross-platform (macOS/Linux) development environments with Flox. |
| 142 | **`flutter-dart-code-review`** | Library-agnostic Flutter/Dart code review checklist covering widget best practices. |
| 143 | **`foundation-models-on-device`** | Apple FoundationModels framework for on-device LLM , text generation, guided generation with @Generable. |
| 144 | **`frontend-a11y`** | Accessibility patterns for React and Next.js , semantic HTML, ARIA attributes, form labeling. |
| 145 | **`frontend-design`** | Bespoke visual and aesthetic design system , custom palettes, typography hierarchy, spatial rhythm. |
| 146 | **`frontend-design-direction`** | Design token audits and design system consistency validation across existing production application screens. |
| 147 | **`frontend-patterns`** | React and Next.js application architecture , server components, state management, hydration safety. |
| 148 | **`frontend-slides`** | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| 149 | **`frontend-ui-engineering`** | UI component implementation , responsive CSS layouts (Flexbox/Grid), accessible semantic markup (WCAG/a11y). |
| 150 | **`fsharp-testing`** | F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration tests. |
| 151 | **`game-arabic-localizer`** | Equips agents and sub-agents with comprehensive game localization and Arabic translation expertise: text. |
| 152 | **`game-mod-artisan`** | Equips agents and sub-agents with advanced game and software modding expertise: Unity (BepInEx/Harmony C#). |
| 153 | **`gan-style-harness`** | GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. |
| 154 | **`gateguard`** | Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation. |
| 155 | **`generating-python-installer`** | Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming. |
| 156 | **`git-workflow`** | Git branching strategies, rebase vs merge workflows, pull request mechanics. |
| 157 | **`git-workflow-and-versioning`** | Git commit message conventions, semantic versioning (SemVer), automated changelog generation. |
| 158 | **`github-ops`** | GitHub repository operations, automation, and management. |
| 159 | **`golang-patterns`** | Idiomatic Go patterns, best practices, and conventions for building robust, efficient. |
| 160 | **`golang-testing`** | Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. |
| 161 | **`google-workspace-ops`** | Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks. |
| 162 | **`grammar-check`** | Identify grammar, logical, and flow errors in text and suggest targeted fixes without rewriting the. |
| 163 | **`growth-log`** | Use after a complex task, failure, or when reviewing what was learned. |
| 164 | **`growth-loops`** | Identify growth loops (flywheels) for sustainable traction. |
| 165 | **`gtm-motions`** | Identify the best GTM motions and tools across 7 motion types: Inbound, Outbound, Paid Digital, Community. |
| 166 | **`gtm-strategy`** | Create a go-to-market strategy covering marketing channels, messaging, success metrics, and launch timeline. |
| 167 | **`healthcare-cdss-patterns`** | Clinical Decision Support System (CDSS) development patterns. |
| 168 | **`healthcare-emr-patterns`** | EMR/EHR development patterns for healthcare applications. |
| 169 | **`healthcare-eval-harness`** | Patient safety evaluation harness for healthcare application deployments. |
| 170 | **`healthcare-phi-compliance`** | Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for. |
| 171 | **`hermes-imports`** | Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. |
| 172 | **`hexagonal-architecture`** | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion. |
| 173 | **`hipaa-compliance`** | HIPAA-specific entrypoint for healthcare privacy and security work. |
| 174 | **`homelab-network-readiness`** | Readiness checklist for homelab VLAN segmentation, local DNS filtering. |
| 175 | **`homelab-network-setup`** | Practical home and homelab network planning for gateways, switches, access points, IP ranges. |
| 176 | **`homelab-pihole-dns`** | Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records. |
| 177 | **`homelab-vlan-segmentation`** | Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense. |
| 178 | **`homelab-wireguard-vpn`** | WireGuard VPN server setup, peer configuration, key generation, split tunneling vs full tunnel routing. |
| 179 | **`hookify-rules`** | This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify. |
| 180 | **`idea-refine`** | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. |
| 181 | **`ideal-customer-profile`** | Identify the Ideal Customer Profile (ICP) from research data with demographics, behaviors, JTBD, and needs. |
| 182 | **`identify-assumptions-existing`** | Identify risky assumptions for a feature idea in an existing product across Value, Usability, Viability. |
| 183 | **`identify-assumptions-new`** | Identify risky assumptions for a new product idea across 8 risk categories including Go-to-Market, Strategy. |
| 184 | **`incremental-implementation`** | Delivers changes incrementally in thin, verifiable slices. |
| 185 | **`inherit-legacy-style`** | Legacy-project style inheritance skill. |
| 186 | **`intended-vs-implemented`** | The method for finding the gap between what a system is supposed to do and what the code actually does . |
| 187 | **`intent-driven-development`** | Turn ambiguous or high-impact product and engineering changes into scoped. |
| 188 | **`interview-me`** | Extracts what the user actually wants instead of what they think they should want. |
| 189 | **`interview-script`** | Create a structured customer interview script with JTBD probing questions, warm-up, core exploration. |
| 190 | **`inventory-demand-planning`** | Codified expertise for demand forecasting, safety stock optimization, replenishment planning. |
| 191 | **`investor-materials`** | Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models. |
| 192 | **`investor-outreach`** | Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. |
| 193 | **`ios-icon-gen`** | Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or. |
| 194 | **`iterative-retrieval`** | Pattern for progressively refining context retrieval to solve the subagent context problem. |
| 195 | **`ito-baskets`** | Read-only Itô basket and prediction-market data skill. |
| 196 | **`ito-compute`** | Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status. |
| 197 | **`ito-inference`** | Inspect the availability of model serving on a completed Itô compute booking and. |
| 198 | **`ito-training`** | Inspect the availability of ML training on a completed Itô compute booking and. |
| 199 | **`java-coding-standards`** | Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams. |
| 200 | **`jira-integration`** | Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments. |
| 201 | **`job-stories`** | Create job stories using the 'When [situation], I want to [motivation]. |
| 202 | **`jpa-patterns`** | JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing. |
| 203 | **`knowledge-ops`** | Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files. |
| 204 | **`kotlin-coroutines-flows`** | Kotlin Coroutines and Flow patterns for Android and KMP , structured concurrency, Flow operators, StateFlow. |
| 205 | **`kotlin-exposed-patterns`** | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling. |
| 206 | **`kotlin-ktor-patterns`** | Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization. |
| 207 | **`kotlin-patterns`** | Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient. |
| 208 | **`kotlin-testing`** | Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. |
| 209 | **`kubernetes-patterns`** | Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling. |
| 210 | **`laravel-patterns`** | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching. |
| 211 | **`laravel-plugin-discovery`** | Discover and evaluate Laravel packages via LaraPlugins.io MCP. |
| 212 | **`laravel-security`** | Laravel security best practices , authentication, authorization, Eloquent safety, CSRF, XSS prevention. |
| 213 | **`laravel-tdd`** | Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing. |
| 214 | **`laravel-verification`** | Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage. |
| 215 | **`latency-critical-systems`** | Use for latency-sensitive systems such as realtime dashboards, market data, streaming agents. |
| 216 | **`lead-intelligence`** | AI-native lead intelligence and outreach pipeline. |
| 217 | **`lean-canvas`** | Generate a Lean Canvas with problem, solution, metrics, cost structure, UVP, unfair advantage, channels. |
| 218 | **`liquid-glass-design`** | iOS 26 Liquid Glass design system , dynamic glass material with blur, reflection. |
| 219 | **`living-docs-governance`** | Keep a long-lived project's documentation from rotting by assigning existing project docs clear constitution. |
| 220 | **`llm-trading-agent-security`** | Security patterns for autonomous trading agents with wallet or transaction authority. |
| 221 | **`logistics-exception-management`** | Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes. |
| 222 | **`loop-debug`** | Enforces an autonomous iterative debug-and-repair loop (Test -> Diagnose -> Fix -> Retest) and mandatory. |
| 223 | **`loop-design-check`** | Design a goal-oriented agent loop, and review it for the ways loops go wrong, spinning and burning tokens. |
| 224 | **`mailtrap-email-integration`** | Guides agents through integrating transactional email sending via Mailtrap's Email API. |
| 225 | **`make-interfaces-feel-better`** | Apply concrete design-engineering details that make interfaces feel polished. |
| 226 | **`malware-root-hunter`** | Deep malware, spyware, and persistence hunting skill for Windows. |
| 227 | **`manim-video`** | Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs. |
| 228 | **`market-research`** | Conduct market research, competitive analysis, investor due diligence. |
| 229 | **`market-segments`** | Identify 3-5 potential customer segments with demographics, JTBD, and product fit analysis. |
| 230 | **`market-sizing`** | Estimate market size using TAM, SAM, and SOM with top-down and bottom-up approaches. |
| 231 | **`marketing-campaign`** | End-to-end marketing campaign planning and execution. |
| 232 | **`marketing-ideas`** | Generate 5 creative, cost-effective marketing ideas with channels, messaging, and engagement rationale. |
| 233 | **`master-agreement-generator`** | Generate review drafts of counterparty master agreements from one template plus a JSON spec. |
| 234 | **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with. |
| 235 | **`mcp-server-patterns`** | Build MCP servers with Node/TypeScript SDK , tools, resources, prompts, Zod validation. |
| 236 | **`messages-ops`** | Evidence-first live messaging workflow for ECC. |
| 237 | **`metrics-dashboard`** | Define and design a product metrics dashboard with key metrics, data sources, visualization types. |
| 238 | **`ml-adoption-playbook`** | End-to-end methodology for AI agents and software engineers to add machine learning algorithms to. |
| 239 | **`mle-workflow`** | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation. |
| 240 | **`monetization-strategy`** | Brainstorm 3-5 monetization strategies with audience fit, risks, and validation experiments. |
| 241 | **`motion-advanced`** | Advanced motion patterns for React / Next.js , drag & drop, gestures, text animations, SVG path drawing. |
| 242 | **`motion-foundations`** | Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement. |
| 243 | **`motion-patterns`** | Production-ready animation patterns for React / Next.js , button, modal, toast, stagger, page transitions. |
| 244 | **`mysql-patterns`** | MySQL and MariaDB schema, query, indexing, transaction, replication. |
| 245 | **`nanoclaw-repl`** | Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p. |
| 246 | **`nasiko-control-plane`** | Use the experimental Nasiko CLI lifecycle bridge for pinned installation, read-only status. |
| 247 | **`nestjs-patterns`** | NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config. |
| 248 | **`netmiko-ssh-automation`** | Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing. |
| 249 | **`network-bgp-diagnostics`** | Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy. |
| 250 | **`network-config-validation`** | Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses. |
| 251 | **`network-interface-health`** | Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues. |
| 252 | **`nextjs-turbopack`** | Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack. |
| 253 | **`nodejs-keccak256`** | Prevent Ethereum hashing bugs in JavaScript and TypeScript. |
| 254 | **`north-star-metric`** | Define a North Star Metric and 3-5 supporting input metrics that form a metrics constellation. |
| 255 | **`nutrient-document-processing`** | Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. |
| 256 | **`nuxt4-patterns`** | Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading. |
| 257 | **`observability-and-instrumentation`** | Instruments code so production behavior is visible and diagnosable. |
| 258 | **`openclaw-persona-forge`** | 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图. |
| 259 | **`opensource-pipeline`** | Open-source pipeline: fork, sanitize, and package private projects for safe public release. |
| 260 | **`opportunity-solution-tree`** | Build an Opportunity Solution Tree (OST) to structure product discovery . |
| 261 | **`orch-add-feature`** | Orchestrate building a brand-new feature end to end , research, plan, TDD implementation, review. |
| 262 | **`orch-build-mvp`** | Orchestrate bootstrapping a working MVP from a design or spec document , ingest the doc. |
| 263 | **`orch-change-feature`** | Orchestrate altering an existing, working feature to new desired behavior, update its tests to the new spec. |
| 264 | **`orch-fix-defect`** | Orchestrate fixing a bug , reproduce it as a failing regression test, fix to green, review, and gated commit. |
| 265 | **`orch-pipeline`** | Shared orchestration engine for the orch-* skill family. |
| 266 | **`orch-refine-code`** | Orchestrate a behavior-preserving refactor , confirm tests are green, restructure without changing behavior. |
| 267 | **`outcome-roadmap`** | Transform an output-focused roadmap into an outcome-focused one that communicates strategic intent. |
| 268 | **`parallel-execution-optimizer`** | Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls. |
| 269 | **`pdf-artisan`** | Guides agents and sub-agents to generate high-fidelity, beautifully styled PDF documents (invoices, reports. |
| 270 | **`performance-optimization`** | Optimizes application performance across frontend, backend, queries, and databases. |
| 271 | **`perl-patterns`** | Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications. |
| 272 | **`perl-security`** | Comprehensive Perl security covering taint mode, input validation, safe process execution. |
| 273 | **`perl-testing`** | Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover. |
| 274 | **`pestle-analysis`** | Perform a PESTLE analysis covering Political, Economic, Social, Technological, Legal. |
| 275 | **`plan-canvas`** | Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats. |
| 276 | **`plan-orchestrate`** | Read a plan document, decompose it into steps, design a per-step agent chain from the ECC catalogue. |
| 277 | **`plankton-code-quality`** | Write-time code quality enforcement using Plankton , auto-formatting, linting. |
| 278 | **`planning-and-task-breakdown`** | Breaks work into ordered tasks. |
| 279 | **`porters-five-forces`** | Perform Porter's Five Forces analysis , competitive rivalry, supplier power, buyer power. |
| 280 | **`positioning-ideas`** | Brainstorm product positioning ideas differentiated from competitors. |
| 281 | **`postgres-patterns`** | PostgreSQL database patterns for query optimization, schema design, indexing, and security. |
| 282 | **`pre-mortem`** | Run a pre-mortem risk analysis on a PRD or launch plan. |
| 283 | **`prediction-market-oracle-research`** | Research prediction markets as data sources or oracle signals for products, agents, dashboards. |
| 284 | **`prediction-market-risk-review`** | Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality. |
| 285 | **`pricing-strategy`** | Analyze and design pricing strategies including pricing models, competitive pricing analysis. |
| 286 | **`prioritization-frameworks`** | Reference guide to 9 prioritization frameworks with formulas, when-to-use guidance, and templates, RICE, ICE. |
| 287 | **`prioritize-assumptions`** | Prioritize assumptions using an Impact × Risk matrix and suggest experiments for each. |
| 288 | **`prioritize-features`** | Prioritize a backlog of feature ideas based on impact, effort, risk. |
| 289 | **`prisma-patterns`** | Prisma ORM patterns for TypeScript backends , schema design, query optimization, transactions, pagination. |
| 290 | **`privacy-policy`** | Draft a detailed privacy policy covering data types, jurisdiction, GDPR and compliance considerations. |
| 291 | **`product-capability`** | Translate PRD intent, roadmap asks. |
| 292 | **`product-lens`** | Use this skill to validate the "why" before building, run product diagnostics. |
| 293 | **`product-name`** | Brainstorm 5 unique, memorable product names with rationale aligned to brand values and target audience. |
| 294 | **`product-strategy`** | Create a comprehensive product strategy using the 9-section Product Strategy Canvas , vision, segments, costs. |
| 295 | **`product-vision`** | Brainstorm an inspiring, achievable. |
| 296 | **`production-audit`** | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks. |
| 297 | **`production-scheduling`** | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimization. |
| 298 | **`project-flow-ops`** | Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work. |
| 299 | **`prompt-optimizer`** | Analyze raw prompts, identify intent and gaps, match ECC components (skills/commands/agents/hooks). |
| 300 | **`python-patterns`** | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient. |
| 301 | **`python-testing`** | Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization. |
| 302 | **`pytorch-patterns`** | PyTorch deep learning patterns and best practices for building robust, efficient. |
| 303 | **`quality-nonconformance`** | Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action. |
| 304 | **`quarkus-patterns`** | Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services. |
| 305 | **`quarkus-security`** | Quarkus Security best practices for authentication, authorization, JWT/OIDC, RBAC, input validation, CSRF. |
| 306 | **`quarkus-tdd`** | Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing, and JaCoCo. |
| 307 | **`quarkus-verification`** | Verification loop for Quarkus projects: build, static analysis, tests with coverage, security scans. |
| 308 | **`rails-patterns`** | Ruby on Rails framework patterns for Rails 7.1+ and 8.x apps. |
| 309 | **`ralphinho-rfc-pipeline`** | RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration. |
| 310 | **`react-native-patterns`** | React Native and Expo app patterns , Expo Router navigation, state separation (server/client/route/form). |
| 311 | **`react-patterns`** | React 18/19 patterns including hooks discipline, server/client component boundaries. |
| 312 | **`react-performance`** | React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best. |
| 313 | **`react-testing`** | React component testing with React Testing Library, Vitest/Jest, MSW for network mocking. |
| 314 | **`recsys-pipeline-architect`** | Design composable recommendation, ranking. |
| 315 | **`recursive-decision-ledger`** | Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search. |
| 316 | **`redis-patterns`** | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub. |
| 317 | **`regex-vs-llm-structured-text`** | Decision framework for choosing between regex and LLM when parsing structured text , start with regex. |
| 318 | **`release-notes`** | Generate user-facing release notes from tickets, PRDs, or changelogs. |
| 319 | **`remotion-video-creation`** | Best practices for Remotion - Video creation in React. |
| 320 | **`repo-scan`** | Bootstrap pointer that installs the external repo-scan skill from a pinned, reviewable commit. |
| 321 | **`request-completeness-sentinel`** | Enforces 100% complete fulfillment of all user requests, sub-tasks, and constraints without omission. |
| 322 | **`research-ops`** | Evidence-first current-state research workflow for ECC. |
| 323 | **`retro`** | Facilitate a structured sprint retrospective , what went well, what didn't. |
| 324 | **`returns-reverse-logistics`** | Codified expertise for returns authorization, receipt and inspection, disposition decisions, refund processing. |
| 325 | **`review-resume`** | Comprehensive PM resume review and tailoring against 10 best practices including XYZ+S formula. |
| 326 | **`rules-distill`** | Scan skills to extract cross-cutting principles and distill them into rules , append, revise. |
| 327 | **`rust-patterns`** | Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe. |
| 328 | **`rust-testing`** | Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking. |
| 329 | **`santa-method`** | Multi-agent adversarial verification with convergence loop. |
| 330 | **`scientific-db-pubmed-database`** | Direct PubMed and NCBI E-utilities search workflows for biomedical literature, MeSH queries, PMID lookup. |
| 331 | **`scientific-db-uspto-database`** | USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks. |
| 332 | **`scientific-pkg-gget`** | gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches. |
| 333 | **`scientific-thinking-literature-review`** | Systematic literature-review workflow for academic, biomedical, technical, and scientific topics. |
| 334 | **`scientific-thinking-scholar-evaluation`** | Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections. |
| 335 | **`search-first`** | Research-before-coding workflow. |
| 336 | **`security-and-hardening`** | Defensive code hardening implementation , input sanitization, cryptographic validation, memory safety. |
| 337 | **`security-bounty-hunter`** | Hunt for exploitable, bounty-worthy security issues in repositories. |
| 338 | **`security-review`** | Endpoint, API, and feature security audit, authentication flows, authorization checks, secret management. |
| 339 | **`security-scan`** | Scan your Claude Code configuration (.claude/ directory) for security. Use when auditing a . |
| 340 | **`sentiment-analysis`** | Analyze user feedback data to identify segments with sentiment scores, JTBD. |
| 341 | **`seo`** | Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data. |
| 342 | **`shipping-and-launch`** | Prepares production launches. |
| 343 | **`shipping-artifacts`** | The durable documentation set that makes an AI-built (vibe-coded) app reviewable before shipping. |
| 344 | **`skill-comply`** | Visualize whether skills, rules, and agent definitions are actually followed. |
| 345 | **`skill-scout`** | Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. |
| 346 | **`skill-stocktake`** | Use when auditing Claude skills and commands for quality. |
| 347 | **`social-graph-ranker`** | Weighted social-graph ranking for warm intro discovery, bridge scoring. |
| 348 | **`social-publisher`** | Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw. |
| 349 | **`source-driven-development`** | Grounds every implementation decision in official documentation. |
| 350 | **`spec-driven-development`** | Creates specs before coding. |
| 351 | **`springboot-patterns`** | Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing. |
| 352 | **`springboot-security`** | Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting. |
| 353 | **`springboot-tdd`** | Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. |
| 354 | **`springboot-verification`** | Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans. |
| 355 | **`sprint-plan`** | Plan a sprint with capacity estimation, story selection, dependency mapping, and risk identification. |
| 356 | **`sql-queries`** | Generate SQL queries from natural language descriptions. |
| 357 | **`stakeholder-map`** | Build a stakeholder map using a power/interest grid, identify communication strategies per quadrant. |
| 358 | **`startup-canvas`** | Generate a Startup Canvas combining Product Strategy (9 sections) and Business Model (costs + revenue). |
| 359 | **`strategic-compact`** | Suggests manual context compaction at logical intervals to preserve context through task phases rather. |
| 360 | **`strategy-red-team`** | Red-team a PRD, roadmap, or strategy by attacking its load-bearing assumptions before reality does. |
| 361 | **`summarize-interview`** | Summarize a customer interview transcript into a structured template with JTBD, satisfaction signals. |
| 362 | **`summarize-meeting`** | Summarize a meeting transcript into structured notes with date, participants, topic, key decisions. |
| 363 | **`swift-actor-persistence`** | Thread-safe data persistence in Swift using actors , in-memory cache with file-backed storage. |
| 364 | **`swift-concurrency-6-2`** | Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent. Use when adopting Swift 6. |
| 365 | **`swift-protocol-di-testing`** | Protocol-based dependency injection for testable Swift code , mock file system, network. |
| 366 | **`swiftui-patterns`** | SwiftUI architecture patterns, state management with @Observable, view composition, navigation. |
| 367 | **`swot-analysis`** | Perform a detailed SWOT analysis , strengths, weaknesses, opportunities. |
| 368 | **`system-repair-hero`** | Windows system file integrity, component store repair, and filesystem diagnostic skill. |
| 369 | **`taste`** | A creative-direction (taste) layer for music videos and short-form edits in the angelcore / cloud-trance. |
| 370 | **`taste-application`** | Generate new video against a distilled style pack and cut it into a finished piece . |
| 371 | **`taste-distillation`** | Measure a set of reference videos into a reusable style pack , colour grade as a 3D LUT. |
| 372 | **`tasteforge-video`** | Use for file-driven multimodal image, video, and 3D-asset discovery, taste interviews. |
| 373 | **`tdd-workflow`** | Full-lifecycle test automation framework, coverage gates (80%+ unit, integration, E2E). |
| 374 | **`team-agent-orchestration`** | Run team-based orchestration for agent squads using work items, ownership, agent Kanban, merge gates. |
| 375 | **`team-builder`** | Interactive agent picker for composing and dispatching parallel teams. |
| 376 | **`terminal-opener`** | Open an executable and its argument array in a visible terminal window through a reusable. |
| 377 | **`terminal-ops`** | Evidence-first repo execution workflow for ECC. |
| 378 | **`test-driven-development`** | Micro-level Red-Green-Refactor development loop for implementing isolated functions, verifying logic units. |
| 379 | **`test-scenarios`** | Create comprehensive test scenarios from user stories with test objectives, starting conditions, user roles. |
| 380 | **`theme-factory`** | Toolkit for styling artifacts with a theme. |
| 381 | **`tinystruct-patterns`** | Expert guidance for developing with the tinystruct Java framework. |
| 382 | **`token-budget-advisor`** | Offers the user an informed choice about how much response depth to consume before answering. |
| 383 | **`ui-demo`** | Record polished UI demo videos using Playwright. |
| 384 | **`ui-to-vue`** | Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components. |
| 385 | **`uncloud`** | Use when managing an Uncloud cluster , deploying services, configuring Caddy ingress. |
| 386 | **`unified-memory`** | Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode. |
| 387 | **`unified-notifications-ops`** | Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks. |
| 388 | **`user-personas`** | Create refined user personas from research data — 3 personas with JTBD, pains, gains, and unexpected insights. |
| 389 | **`user-segmentation`** | Segment users from feedback data based on behavior, JTBD, and needs. |
| 390 | **`user-stories`** | Create user stories following the 3 C's (Card, Conversation. |
| 391 | **`using-agent-skills`** | Discovers and invokes agent skills. |
| 392 | **`value-prop-statements`** | Generate value proposition statements for marketing, sales, and onboarding from existing value propositions. |
| 393 | **`value-proposition`** | Design a detailed value proposition using a 6-part JTBD template , Who, Why, What before, How, What after. |
| 394 | **`video-editing`** | AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. |
| 395 | **`video-intelligence-pilot`** | Equips agents and sub-agents to extract, transcribe, analyze, and execute tasks from video URLs (YouTube. |
| 396 | **`videodb`** | See, Understand, Act on video and audio. |
| 397 | **`visa-doc-translate`** | Translate visa application documents (images) to English and create a bilingual PDF with original and. |
| 398 | **`visual-asset-artisan`** | Specializes in high-fidelity AI image generation, asset optimization. |
| 399 | **`vite-patterns`** | Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode. |
| 400 | **`vue-patterns`** | Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management. |
| 401 | **`windows-desktop-e2e`** | E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC. |
| 402 | **`workspace-surface-audit`** | Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup. |
| 403 | **`wwas`** | Create product backlog items in Why-What-Acceptance format , independent, valuable. |
| 404 | **`x-api`** | X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. |


### 3D Procedural Modeling & Vision-in-the-Loop Assets (Kiln Engine)
* **`kiln-author-asset`**: Create procedural 3D assets with Kiln JavaScript, review camera views, and export game-ready GLB models.
* **`kiln-refine-asset`**: Apply anchored edits to 3D source code and inspect revisions without model transcription hallucinations.
* **`kiln-qa-asset`**: Automated 3D asset QA: triangle surface clearances, joint hierarchy checks, and GLTF compliance validation.
* **`kiln-compose-scene`**: Compose multi-asset 3D environments, stage props, and set lighting/camera configurations.
* **`kiln-batch-dispatch`**: Batch generation and clean-room evaluation for asset libraries and multi-model variations.
* **`kiln-setup-workspace`**: Bootstrap and configure a dedicated 3D procedural modeling workspace for Antigravity, Claude, or Codex.
