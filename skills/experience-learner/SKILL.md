---
name: experience-learner
description: Consults and updates troubleshooting history
---
# Continuous Experience Learner & Issue Memory Protocol (`experience-learner`)

The **Experience Learner** skill transforms the assistant into a continuously learning system. It guarantees that every solved bug, roadblock, or configuration pitfall is permanently recorded along with its verified solution. Before executing any task or similar concept, the assistant consults past records so it **never repeats a known mistake**.

---

## 1. Core Operating Mandates

### 1. Pre-Implementation Experience Lookup (المراجعة الاستباقية للخبرات السابقة)
- Before implementing any user idea, feature, or bugfix, the assistant MUST check past issue records:
  - Global Store: `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md`
  - Project Store (if in a specific workspace): `.gemini/troubleshooting.md` or `troubleshooting.md`
- **Search Criteria**: Look for keywords matching the technology, libraries, paths, OS quirks, or concepts in the user's prompt (e.g., `DirectX`, `Vulkan`, `UAC`, `Junctions`, `BiDi`, `YAML`, `PowerShell`).
- If a past pitfall or broken approach is found, **STRICTLY PROHIBIT** repeating the failed method. Apply the proven, verified solution immediately.

### 2. Real-Time Problem-Solution Logging (التسجيل الفوري للمشاكل والحلول)
- Whenever an issue, runtime exception, path failure, permission obstacle, or configuration bug is encountered and solved (e.g., via `loop-debug` or `goal-verifier`):
  - Do NOT let the solution get lost when the session ends.
  - Record the solution into `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md` (and the project's local troubleshooting log if workspace-specific).
  - Use the standard entry template:
    ```markdown
    ### [ID/DATE] Title of the Issue
    - **Context / Tags**: `[Category]`, `[Tool/Tech]`, `[Component]`
    - **Problem & Error Symptom**: Exact error message, observed broken behavior.
    - **Root Cause**: Why it failed.
    - **Verified Solution**: The exact working code, command, setting, or architecture that solved it.
    - **Prevention Invariant**: What must never be done again when dealing with similar ideas.
    ```

### 3. Cross-Project & Cross-Conversation Continuity (الاستمرارية عبر كافة المحادثات)
- Because `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md` is global, solutions learned in conversation A (e.g., GTA San Andreas modding or Rockstar launcher quirks) are immediately accessible in conversation B, C, and all future sessions.

---

## 2. Standard Knowledge Stores

| Store Level | Location | Purpose |
| :--- | :--- | :--- |
| **Global Knowledge** | `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md` | Shared memory across all conversations, workspaces, and system tasks. |
| **Project-Specific** | `<workspace>/.gemini/troubleshooting.md` | Project-specific architecture gotchas, local database configs, or test quirks. |

---

## 3. CLI Helper: `experience_manager.py`

Search and append to the knowledge base automatically:

```powershell
# Search for past solutions by keyword
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" search --query "Vulkan DirectX"

# Record a new solved issue
python "C:\Users\goldl\.gemini\config\skills\experience-learner\scripts\experience_manager.py" add --title "UAC Elevation in PowerShell" --problem "Start-Process failed with request not supported" --cause "Executable has requireAdministrator manifest" --solution "Use Start-Process -Verb RunAs or elevated task" --tags "PowerShell,UAC,Windows"
```
