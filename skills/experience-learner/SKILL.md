---
name: experience-learner
description: Consults and updates troubleshooting history
---
# Continuous Experience Learner & Project Troubleshooting Protocol (`experience-learner`)

The **Experience Learner** skill transforms the assistant into a continuously learning engineering system. It guarantees that every solved bug, roadblock, runtime exception, or architectural pitfall is permanently recorded with **exhaustive technical details** in the active project and synchronized globally.

Before starting any task or implementing an idea, the assistant consults past records so it **never repeats a known mistake**.

---

## 1. Dual-Tier Knowledge Architecture

Memory operates across two distinct, complementary tiers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      DUAL-TIER EXPERIENCE SYSTEM                       │
├───────────────────────────────────┬────────────────────────────────────┤
│   TIER 1: PROJECT-LEVEL STORE     │    TIER 2: GLOBAL KNOWLEDGE BASE   │
│   <project_root>/troubleshooting.md │ ~/.gemini/knowledge/troubleshooting│
│                                   │                      _history.md   │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Created automatically in project│ • Persistent machine-wide memory   │
│ • Deep project-specific details   │ • Cross-project patterns & traps   │
│ • Exact files, diffs, stack traces│ • Universal solutions & invariants │
│ • Dynamic Table of Contents & TOC │ • Available across all sessions    │
└───────────────────────────────────┴────────────────────────────────────┘
```

| Store Level | Location | Purpose & Scope |
| :--- | :--- | :--- |
| **Project-Specific Store** | `<project_root>/troubleshooting.md` (or `.gemini/troubleshooting.md`) | Dedicated to the active project. Logs all project bugs, setup quirks, schema fixes, test failures, and exact code solutions with full details and dynamic TOC. |
| **Global Knowledge Base** | `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md` | Shared memory across all conversations, workspaces, and system tasks on the machine. |

---

## 2. Core Operating Mandates

### 1. Pre-Implementation Experience Lookup (المراجعة الاستباقية للخبرات السابقة)
Before writing or modifying any code, the agent MUST review past records:
1. **Check Local Store**: Look for `<project_root>/troubleshooting.md` in the current workspace.
2. **Check Global Store**: Query `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md` or run:
   ```powershell
   python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" search --query "<technology or error keywords>"
   ```
3. **Mandatory Invariant**: If a past pitfall, broken approach, or library conflict was previously recorded, the agent is **STRICTLY BARRED** from attempting that broken method again.

---

### 2. Automatic Project Scaffolding (الإنشاء التلقائي لملف المشروع)
- In any project where work is performed, the agent ensures `<project_root>/troubleshooting.md` exists.
- If the file does not exist, the agent or `experience_manager.py` creates it immediately with a standard structured header, metadata tracking, and a dynamic Table of Contents block:
  ```markdown
  # Project Troubleshooting & Learned Solutions History

  > **Project**: `<project_name>`  
  > **Initialized**: `YYYY-MM-DD HH:MM`  
  > **Last Updated**: `YYYY-MM-DD HH:MM`  
  > **Total Solved Issues**: `0`

  ## Table of Contents
  <!-- TOC_START -->
  _No issues recorded yet._
  <!-- TOC_END -->

  ---
  ```

---

### 3. Full-Detail Issue Logging Schema (التوثيق التقني الكامل للمشاكل والحلول)
Whenever an issue, runtime exception, permission glitch, or configuration obstacle is solved (via `loop-debug` or direct testing), the agent MUST record the entry with **all 7 technical sections** without omissions:

```markdown
### [YYYY-MM-DD HH:MM] Issue Title
- **Severity**: `Critical` | `Major` | `Minor` | **Status**: `Resolved` | **Tags**: `[Tag1]` `[Tag2]`
- **Affected Files**: `path/to/file1.ext`, `path/to/file2.ext`
- **Environment**: OS details, runtime versions, key package versions

#### 1. Problem & Symptoms
Detailed description of observed broken behavior, error messages, user feedback, or unexpected outputs.

#### 2. Trigger / Steps to Reproduce
Exact steps, input, or environment state that triggered the failure.

#### 3. Error Output / Stack Trace
```text
Exact error logs, stack traces, compiler errors, or shell exit codes.
```

#### 4. Root Cause Analysis
Deep technical breakdown of WHY the bug occurred (internal library behavior, race conditions, type mismatches, OS quirks).

#### 5. Verified Solution
The exact working code diff, configuration edit, or command that resolved the issue.

#### 6. Verification & Test
The exact test command executed, verification steps taken, and confirmation of 100% pass (e.g. `Debug` passed).

#### 7. Prevention Invariant & Lessons Learned
The golden rule or architecture guard to ensure this exact issue never happens again in this project or future projects.

---
```

---

## 3. Autonomous Loop-Debug Integration

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CONTINUOUS LEARNING FEEDBACK LOOP                    │
│                                                                        │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐           │
│   │  Test & Run  │ ──> │ Diagnose &   │ ──> │ Verify 100%  │           │
│   │   Command    │     │ Fix Solution │     │ Pass (Debug) │           │
│   └──────────────┘     └──────────────┘     └──────┬───────┘           │
│                                                    │                   │
│                                                    ▼                   │
│                                       ┌────────────────────────────┐   │
│                                       │ experience_manager.py add  │   │
│                                       ├────────────────────────────┤   │
│                                       │ 1. Project troubleshooting │   │
│                                       │ 2. Dynamic TOC Refresh     │   │
│                                       │ 3. Global Sync (~/.gemini) │   │
│                                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Autonomous Trigger**: Immediately after `loop-debug` verifies a fix, the agent records the solution.
2. **Zero Missing Information**: Never log incomplete summaries or placeholders. Include exact file paths, error traces, and working solutions.
3. **Dual Synchronization**: Changes are written to the local project's `troubleshooting.md` and concurrently appended to the global store so that future conversations benefit automatically.

---

## 4. Helper Utility CLI: `experience_manager.py`

Located at: `C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py`

### CLI Commands Reference

```powershell
# 1. Initialize troubleshooting.md in the current project or a target workspace
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" init --workspace "C:\path\to\project"

# 2. Add a fully detailed issue entry with automatic TOC and global sync
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" add `
  --workspace "C:\path\to\project" `
  --title "Missing Header in Auth Middleware" `
  --problem "API returned 500 when Authorization header was omitted." `
  --cause "Direct property access on undefined headers object." `
  --solution "Added optional chaining and nullish coalescing default." `
  --stack-trace "TypeError: Cannot read properties of undefined (reading split)" `
  --steps "Send GET /api/user without Authorization header." `
  --verification "Executed automated API test; passed with 200 OK." `
  --prevention "Always use strict input validation middleware on protected routes." `
  --files "src/middleware/auth.js" `
  --severity "Major" `
  --tags "Node,Auth,Security"

# 3. Search past solved issues across local project and global stores
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" search --query "Auth Middleware"

# 4. View statistics on recorded issues
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" stats --workspace "C:\path\to\project"

# 5. Refresh Table of Contents and counts manually
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" update-toc --workspace "C:\path\to\project"
```
