---
name: code-completeness-debugger
description: Pre-delivery audit for zero missing code or TODOs
---
# Pre-Delivery Code & Function Completeness Debugger (`code-completeness-debugger`)

The **Code Completeness Debugger** skill prevents delivering projects with missing code (`أكواد ناقصة`), missing functions (`دوال ناقصة`), or unimplemented stubs. Before any project is handed to the user, it enforces a complete structural and symbol-level audit alongside `loop-debug`.

---

## 1. Core Pre-Delivery Audit Mandates

### 1. Zero Missing or Undefined Functions (فحص وإكمال كافة الدوال الناقصة)
- Before concluding any coding task, inspect all created and modified files to ensure:
  1. **Every Called Function Exists**: Every function, method, class, callback, or event handler invoked in the code has a complete, valid definition in the file or its imported modules.
  2. **Every Required Feature Has Its Functions**: Every feature requested by the user is backed by actual working functions—never omit helper functions assuming they already exist.
  3. **Every Defined Function Is Wired**: Functions written for a feature must be properly exported, imported, and connected to the entry point, UI event, or manifest (`fxmanifest.lua`, `package.json`, router, or `main`).

### 2. Zero Truncated Code or Placeholders (حظر الأكواد المبتورة أو المختصرة)
- **Strict Ban on Stubs & Placeholders**: Never leave `// TODO`, `# TODO`, `// ... rest of code`, `pass` (in concrete functions), or empty function bodies `{}` in delivered files.
- **Full Implementation**: If any code block or function was abbreviated or partially written during editing, immediately write the complete logic before running final verification.

### 3. Cross-File Dependency & Syntax Integrity (تكامل الاستيراد والربط بين الملفات)
- Verify that all `import` / `require` / `#include` statements resolve to existing files and symbols.
- Confirm that brackets, quotes, blocks, and configuration files are 100% syntactically complete without truncation at the end of the file.

### 4. Seamless Integration with Existing Skills (التوافق التام بدون تعارض)
- **With `loop-debug`**: `code-completeness-debugger` verifies that all code and functions exist and are complete, while `loop-debug` executes the project live in the terminal (`Test -> Diagnose -> Fix -> Retest`) and outputs the final `Debug` confirmation.
- **With `request-completeness-sentinel`**: Guarantees both user-level requirements AND code-level functions/blocks are 100% complete.
- **With `concise-responder` & `bilingual-clean-layout`**: Runs 100% silently during execution; final user delivery remains 1-2 lines with strict `\n\n` isolation around English terms and links.
- **With `sub-agent`**: Read-only (`research`) sub-agents audit code completeness statically via `view_file` and report exact line numbers of any missing functions to the parent agent, while execution (`self`) sub-agents implement and verify them.
