---
name: smart-code-memory
description: Fast working memory and targeted code symbol map
---

# Smart Code Memory & Fast Symbol Retrieval (`smart-code-memory`)

The **Smart Code Memory** skill equips AI models with a fast, lightweight working memory index. It eliminates the fatal flaw of forgetting context across prompts, which forces models to repeatedly re-read entire multi-thousand-line files from start to finish, causing hallucination, token exhaustion, and context degradation.

---

## 1. Core Operating Principles

1. **Index-First Targeted Navigation (البحث الموجه بدلاً من القراءة الكاملة المهدورة)**:
   - Before reading an entire file, query the local working memory index using `python scripts/code_memory.py lookup <path> <symbol>` or `outline <path>`.
   - The engine returns the exact file path, function/class name, signature, and precise line range (`start_line` to `end_line`).
   - Call `view_file` strictly on that targeted line range (`StartLine`, `EndLine`), saving 90%+ of tokens and preserving model focus.

2. **Explicit Fallback Protocol (المراجعة الشاملة عند عدم العثور على المشكلة)**:
   - **القاعدة الإلزامية**: إذا لم يجد النموذج سبب المشكلة أو العطل داخل النطاق المستهدف المحدد، أو إذا لم يكن الرمز مفهرساً:
     - **يُمنع التخمين أو التوقف**: ينتقل النموذج فوراً وتلقائياً لمراجعة الكود البرمجي بالكامل (`view_file` لكامل الملف أو السياق المحيط) للتأكد من تفاصيل التنفيذ والربط الشامل.

3. **Persistent Scratchpad Working Memory (الذاكرة المرجعية السريعة)**:
   - Store critical session facts, active bug root causes, target files, and user preferences in the lightweight memory scratchpad:
     ```bash
     python scripts/code_memory.py note set <key> "<val>"
     python scripts/code_memory.py note get <key>
     ```
   - On subsequent turns, query the scratchpad first instead of re-discovering previously analyzed logic.

---

## 2. CLI Tooling Reference (`scripts/code_memory.py`)

The companion Python engine requires zero external dependencies and runs on Python 3.10+.

### 1. Indexing & Scanning
```bash
# Scan a directory or single file (generates .code_memory/index.json)
python scripts/code_memory.py --root . scan

# Force re-scan on file modification
python scripts/code_memory.py --root . scan --force
```

### 2. Symbol Lookup
```bash
# Locate function, class, or method line numbers in milliseconds
python scripts/code_memory.py --root . lookup calculate_total

# Output as machine-readable JSON
python scripts/code_memory.py --root . lookup authenticate --json
```

### 3. File Outline & Structure Skeleton
```bash
# View complete outline of a file with line numbers
python scripts/code_memory.py --root . outline src/controllers/user.py
```

### 4. Working Memory Notes
```bash
# Save an active finding
python scripts/code_memory.py --root . note set bug_root_cause "Off-by-one error at lines 142-145"

# Retrieve an active finding
python scripts/code_memory.py --root . note get bug_root_cause

# List all stored notes
python scripts/code_memory.py --root . note list
```

---

## 3. Agent Execution Workflow

```
+-------------------------------------------------------------+
| User Request Received                                       |
+-------------------------------------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 1. Query Code Memory (`code_memory.py lookup <symbol>`)      |
+-------------------------------------------------------------+
          |                                       |
     [Found]                                 [Not Found]
          v                                       v
+----------------------------------+   +----------------------+
| 2. Read exact line range         |   | Fallback: Read full  |
| (`view_file(StartLine, EndLine)`)|   | file or grep keyword |
+----------------------------------+   +----------------------+
          |                                       |
          +-------------------+-------------------+
                              v
+-------------------------------------------------------------+
| 3. Problem resolved within range?                           |
|    - YES -> Apply surgical edit                             |
|    - NO  -> Fallback to reading full file & related modules |
+-------------------------------------------------------------+
                              v
+-------------------------------------------------------------+
| 4. Update memory index & note findings                      |
+-------------------------------------------------------------+
```
