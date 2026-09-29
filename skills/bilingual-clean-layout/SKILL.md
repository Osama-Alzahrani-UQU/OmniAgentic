---
name: bilingual-clean-layout
description: Split & Continuation Rule for bilingual text
---
# Bilingual Clean Layout & BiDi Separation Protocol

The **Bilingual Clean Layout** protocol eliminates text scrambling and inverted reading flow caused by Unicode Bidirectional (BiDi) algorithms and Markdown line-collapse when mixing English (LTR) and Arabic (RTL).

---

## 1. Core Invariants & The Split & Continuation Rule

### 1. The Split & Continuation Rule (قاعدة الشطر والتكملة للنصوص ثنائية اللغة)
- **The Universal Mandate**: When an Arabic sentence contains ANY English word, technical term, button name, acronym, filename, or link (e.g. `DLSS 5`, `DirectX`, `Vulkan`, `ReShade`, `Add Emulator / EXE`, `OptiScaler`, `GEMINI.md`):
  1. **Arabic Text Before**: Write the preceding Arabic text on its own line (ending cleanly or with `:`).
  2. **English Text/Term**: Place the English segment on its own dedicated line, isolated by empty lines (`\n\n`).
  3. **Arabic Continuation**: Place the continuation of the Arabic sentence on the next line after an empty line (`\n\n`).
- **Zero Inline English Words**: It is strictly forbidden for ANY English word or Latin character to appear on the same line as Arabic text.
- **Forbidden Attached Prefixes**: Never attach Arabic prefixes to English words (e.g. ❌ `الـ DLSS`, ❌ `عبر الـ Host`, ❌ `للـ Tool`). Always isolate the English term on its own line or use the Arabic equivalent.

### 2. Mandatory Empty Line Separation (سطر فارغ إلزامي لمنع الانهيار)
- **The Markdown Collapse Hazard**: In Markdown, a single newline (`\n`) is rendered as a space, collapsing separate lines into a single line and triggering BiDi text scrambling.
- **Strict Rule**: You MUST separate Arabic lines, English terms, and links with an **EMPTY LINE** (`\n\n`).

### 3. Dedicated Paragraphs for Links & Filenames (عزل الروابط وأسماء الملفات كلياً)
- Every filename (e.g. `GEMINI.md`), link `[label](url)`, or path MUST sit on its own dedicated line surrounded by empty lines (`\n\n`).

### 4. Sub-Agent Technical Accuracy Carve-Out (عدم تقييد البيانات التقنية للوكيل الفرعي)
- While all Arabic prose and user-facing summaries must strictly obey the **Split & Continuation Rule**, internal sub-agent reports sent to the parent agent may include full fenced code blocks, stack traces, and exact file/line diagnostics so that zero technical precision is lost between agents.

---

## 2. Practical Examples: Split & Continuation in Action

### ❌ WRONG (Inline English causes severe BiDi inversion):
```text
لجميع ألعاب الكمبيوتر تم تفعيل تقنية DLSS 5 وحقن ملفات DirectX أو Vulkan داخل تطبيق DLSS 5 Swapper.
```

### ✅ CORRECT (Split & Continuation with Empty Lines):
```markdown
لجميع ألعاب الكمبيوتر تم تفعيل تقنية:

DLSS 5

وحقن ملفات:

DirectX

أو:

Vulkan

داخل تطبيق:

`DLSS 5 Swapper`
```

---

## 3. Negative Constraints (Strictly Forbidden)
- ❌ Do NOT mix English and Arabic on the same line under any circumstances.
- ❌ Do NOT leave English terms inside Arabic sentences; always split before and continue after.
- ❌ Do NOT use single newlines between Arabic and English; always use empty lines (`\n\n`).
- ❌ Do NOT prepend Arabic prefixes to English words (e.g. `الـ Sub-agent`, `للـ Tool`).
