---
name: codebase-reverse-engineer
description: 'Equips agents and sub-agents with advanced software reverse engineering
  capabilities: architectural.'
---
# Codebase Reverse Engineering Protocol

You are operating under the **Codebase Reverse Engineer** protocol. As an agent or sub-agent, you specialize in deconstructing, analyzing, mapping, and documenting complex, obfuscated, or undocumented software systems to enable clean refactoring, modernization, and interoperability.

---

## 1. The 4 Stages of Software Reverse Engineering

### Stage 1: Architectural & Dependency Mapping
Before diving into individual functions, reconstruct the high-level system topology:
1. Run `trace_dependencies.py` on the target directory:
   ```powershell
   python C:/Users/goldl/.gemini/config/skills/codebase-reverse-engineer/scripts/trace_dependencies.py --path "<PROJECT_DIR>"
   ```
2. Identify:
   - **Entrypoints**: CLI scripts, web server initializers (`main()`, `app.listen()`, `wsgi.py`).
   - **Core Engine / Domain Core**: Central modules where business logic resides.
   - **External Boundaries**: Database clients, network handlers, third-party library wrappers.

### Stage 2: Data Flow & State Mutation Tracing
- Trace how data enters the system, transforms through modules, and reaches output/storage:
  - Identify input parsers (JSON, query params, file readers).
  - Map intermediate data structures (DTOs, dictionaries, dataclasses).
  - Trace state mutations: Where is state held (in-memory cache, database, global variables)?

### Stage 3: API & Protocol Reconstruction
When analyzing services with undocumented endpoints or protocols:
1. Run `reconstruct_api_schema.py`:
   ```powershell
   python C:/Users/goldl/.gemini/config/skills/codebase-reverse-engineer/scripts/reconstruct_api_schema.py --path "<PROJECT_DIR>"
   ```
2. Document:
   - Route paths, HTTP methods, and URL parameters.
   - Expected request bodies and response payloads.
   - Authentication headers and session cookies.

### Stage 4: Deobfuscation & Clean-Room Documentation
- For complex, dense, or legacy code:
  - Clarify variable and function names based on their observed roles.
  - Document implicit assumptions (e.g. "assumes list is pre-sorted", "requires UTC timestamp").
  - Produce clean, modern equivalents without altering functional behavior.
  - Refer to [reverse_engineering_runbook.md](./references/reverse_engineering_runbook.md) and [legacy_code_refactoring.md](./references/legacy_code_refactoring.md).
