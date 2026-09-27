# Bilingual Text Formatting & BiDi Prevention Guide

This guide details the technical reasons behind Bidirectional (BiDi) text inversion in mixed Arabic/English content and defines the standard formatting rules to ensure maximum readability.

---

## 1. The BiDi Problem Explained

Unicode defines the Bidirectional Algorithm (UAX #9) to handle texts containing both Left-to-Right (LTR, e.g., English, code, numbers) and Right-to-Left (RTL, e.g., Arabic, Hebrew) scripts.

### Common Failure Scenarios in Chat UIs & Terminals:
1. **Embedded File Paths**:
   When an English path like `C:\Users\name\file.py` is surrounded by Arabic words, the backslashes and slashes are treated as neutral characters. The BiDi engine may flip path components: `file.py\Users\name\C:` or place the Arabic conclusion before the drive letter.
2. **Punctuation Flipping**:
   Periods, commas, colons, and parentheses adjacent to mixed scripts often jump from the end of the line to the beginning.
3. **Word Order Scrambling**:
   When English technical phrases (e.g. `npm install --save-dev`) sit between Arabic words, readers lose track of where the sentence starts and ends, especially when scanning code instructions.

---

## 2. The Line-Separation Solution

The simplest, most robust, and universally effective solution across ALL platforms (Web, VS Code, Terminals, PDF viewers, Markdown renderers) is **Line Separation**:

### Rule 1: Stacking Segments & Split-and-Continuation
When an Arabic sentence contains an English phrase, technical name, or button:
1. Write the preceding Arabic text on its own line.
2. Place the English phrase/button/term on its own dedicated line (surrounded by empty lines `\n\n`).
3. Place the Arabic continuation on the following line.

Instead of:
```text
ظ„ط¬ظ…ظٹط¹ ط£ظ„ط¹ط§ط¨ ط§ظ„ظƒظ…ط¨ظٹظˆطھط± طھظ… طھظپط¹ظٹظ„ طھظ‚ظ†ظٹط© DLSS 5 ظˆط­ظ‚ظ† ظ…ظ„ظپط§طھ DirectX ط£ظˆ Vulkan ط¯ط§ط®ظ„ طھط·ط¨ظٹظ‚ DLSS 5 Swapper.
```

Format as:
```text
ظ„ط¬ظ…ظٹط¹ ط£ظ„ط¹ط§ط¨ ط§ظ„ظƒظ…ط¨ظٹظˆطھط± طھظ… طھظپط¹ظٹظ„ طھظ‚ظ†ظٹط©:

DLSS 5

ظˆط­ظ‚ظ† ظ…ظ„ظپط§طھ:

DirectX

ط£ظˆ:

Vulkan

ط¯ط§ط®ظ„ طھط·ط¨ظٹظ‚:

`DLSS 5 Swapper`
```

### Rule 2: Sub-Agent Communication
Sub-agents must never serialize mixed English/Arabic JSON or raw text inline without structural separation:

```text
ط§ظ„ط­ط§ظ„ط©: ظ†ط§ط¬ط­
ط§ظ„ظ…ظ‡ظ…ط©:
Video Transcript Extraction
ط§ظ„ظ†طھظٹط¬ط©:
طھظ… ط§ط³طھط®ط±ط§ط¬ 61 ط¬ط²ط،ط§ظ‹ ظ†طµظٹط§ظ‹ ظˆط­ظپط¸ ط§ظ„ظ…ط®ط±ط¬ط§طھ ظپظٹ ط§ظ„ظ…ط³ط§ط± ط§ظ„ظ…ط­ط¯ط¯.
ط§ظ„ظ…ظ„ظپ:
file:///C:/Users/goldl/Desktop/antigravity_skills_pack.zip
```

### Rule 3: Fenced Code Blocks for Commands & Snippets
Any command or multi-token technical expression must be isolated in its own fenced code block or backticked line:

```bash
python -m py_compile script.py
```
ظ…طھط¨ظˆط¹ط§ظ‹ ط¨ط§ظ„ظ†طھظٹط¬ط© ط¨ط§ظ„ظ„ط؛ط© ط§ظ„ط¹ط±ط¨ظٹط© ظپظٹ ط³ط·ط± ظ…ط³طھظ‚ظ„.
