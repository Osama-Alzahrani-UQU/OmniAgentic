# Continuous Experience Learning & Project Memory Reference Guide

This reference guide establishes the formal protocol for recording and leveraging technical experiences across individual projects and universal assistant memory.

---

## 1. The Core Lifecycle of Experience Learning

### Phase 1: Pre-Implementation Experience Retrieval
1. **Local Project Search**:
   - Inspect the current workspace for `<project_root>/troubleshooting.md`.
   - Read recent entries and Table of Contents to understand known project quirks, past architectural decisions, and previous regressions.
2. **Global Knowledge Base Search**:
   - Query `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md`.
   - If a similar library bug, OS quirk, or runtime error was previously encountered and solved, adopt the verified solution immediately without trial-and-error.

---

### Phase 2: Autonomous Root-Cause Diagnosis & Fix
1. Execute the `loop-debug` cycle: `Test -> Diagnose -> Fix -> Retest`.
2. Do not stop until automated tests or live verification confirm 100% pass (`Debug` verified).

---

### Phase 3: Exhaustive Project-Level Documentation
Immediately upon verification, log the experience:
1. **Auto-Initialize If Absent**:
   - If the project does not have a `troubleshooting.md` file, initialize it with a structured header and Table of Contents.
2. **Record Full Technical Details**:
   - Log all 7 mandatory sections:
     1. **Problem & Symptoms**: Verbatim error messages, symptoms, broken UI/behavior.
     2. **Trigger / Steps to Reproduce**: The exact condition that caused the fault.
     3. **Error Output / Stack Trace**: Unaltered error traces in code blocks.
     4. **Root Cause Analysis**: Why the system behaved this way at a deep technical level.
     5. **Verified Solution**: The exact code change, configuration, or patch that resolved it.
     6. **Verification & Test**: How the fix was validated with test command and output.
     7. **Prevention Invariant**: The strict rule or constraint to guarantee zero recurrence.
3. **Refresh Navigation**:
   - Update Table of Contents anchors and total issue counters automatically.

---

### Phase 4: Machine-Wide Global Synchronization
- Mirror the core lessons to `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md`.
- Ensure other projects, workspaces, and future conversations on this system benefit from the solution.

---

## 2. CLI Helper Integration

Agents can use `experience_manager.py` located at:
`C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py`

- `init`: Scaffolds `<project_root>/troubleshooting.md`.
- `add`: Logs an issue with all 7 technical fields, updates TOC, and syncs globally.
- `search`: Searches across both local project and global stores.
- `stats`: Displays counts and health status of local and global stores.
- `update-toc`: Rebuilds the markdown Table of Contents.
