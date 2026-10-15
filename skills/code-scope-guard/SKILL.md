---
name: code-scope-guard
description: Strict scope guard and anti-destruction shield
---

# Code Scope Guard & Anti-Destruction Shield (`code-scope-guard`)

The **Code Scope Guard** skill enforces strict boundaries on AI model code modifications. It protects codebases against AI hallucination, scope drift, accidental file deletions, symbol gutting (deleting functions or classes without authorization), and unintended mass deletions.

---

## 1. Core Protection Invariants

1. **Strict Scope Confinement (حظر التعديل خارج النطاق المطلوب)**:
   - The agent MUST confine edits strictly to the files explicitly targeted by the user's task or directly implicated in the bug/feature.
   - Touching, reformatting, or "refactoring" unrelated files or functions is strictly prohibited.

2. **Zero Unintentional Deletions (حظر حذف الأكواد أو الدوال القائمة نهائياً)**:
   - The agent MUST never delete existing functions, methods, classes, or files unless the user explicitly requested their removal or deprecation.
   - Any modification must preserve all existing, unrelated functionality in the modified files.

3. **Pre-Edit Baseline Locking & Backup (قفل خط الأساس وأخذ نسخة احتياطية)**:
   - Before applying complex or multi-file edits, lock a snapshot of the project baseline:
     ```bash
     python scripts/scope_guard.py --root . lock --allow-files src/target.py
     ```
   - This creates a cryptographic and symbol-level baseline in `.scope_guard/` and backs up files.

4. **Post-Edit Audit Loop (الفحص الإلزامي بعد التعديل)**:
   - Immediately after editing, run:
     ```bash
     python scripts/scope_guard.py --root . verify
     ```
   - If any out-of-scope modification, deleted file, gutted symbol, or suspicious line shrinkage is detected, the command exits with error code `1`.

5. **Instant Surgical Rollback (الاستعادة الفورية عند الخطأ أو الهلوسة)**:
   - If verification fails or unexpected changes are detected, restore the affected files instantly:
     ```bash
     # Restore a specific file
     python scripts/scope_guard.py --root . rollback src/target.py

     # Or restore all files to pristine state
     python scripts/scope_guard.py --root . rollback
     ```

---

## 2. CLI Tooling Reference (`scripts/scope_guard.py`)

The companion engine runs as a global command (`scope_guard` or `scope-guard`) or direct Python script.

### 1. Lock Baseline
```bash
# Lock the current project state and allow edits ONLY to specific files
scope_guard --root . lock --allow-files src/app.py src/utils.py

# Or run via local Python script:
# python scripts/scope_guard.py --root . lock --allow-files src/app.py

# Lock without restricting specific files (monitors for deletions and gutted symbols)
scope_guard --root . lock
```

### 2. Verify Modifications
```bash
# Run verification check against baseline
python scripts/scope_guard.py --root . verify

# Output machine-readable JSON format
python scripts/scope_guard.py --root . verify --json
```

### 3. Rollback Modifications
```bash
# Roll back all files to the locked baseline
python scripts/scope_guard.py --root . rollback

# Roll back a specific file only
python scripts/scope_guard.py --root . rollback src/app.py
```

### 4. Commit Baseline
```bash
# Release lock and finalize changes once verification passes
python scripts/scope_guard.py --root . commit
```

---

## 3. Scope Guard Verification Protocol

```
+-------------------------------------------------------------+
| 1. Lock Project Baseline                                    |
|    `python scripts/scope_guard.py lock --allow-files ...`    |
+-------------------------------------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 2. Perform Minimal Surgical Code Edit                       |
+-------------------------------------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 3. Run Scope Guard Audit                                    |
|    `python scripts/scope_guard.py verify`                   |
+-------------------------------------------------------------+
          |                                       |
    [VIOLATIONS]                               [CLEAN]
          v                                       v
+----------------------------------+   +----------------------+
| 4. Auto-Rollback or Fix          |   | 5. Commit Baseline   |
|    `scope_guard.py rollback`     |   |    `scope_guard.py   |
|    Diagnose & re-apply cleanly   |   |     commit`          |
+----------------------------------+   +----------------------+
```
