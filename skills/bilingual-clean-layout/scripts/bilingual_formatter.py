#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilingual Formatter & BiDi Cleaner Utility
Enforces clean line separation and empty-line paragraph isolation between English
technical terms/links/filenames and Arabic text to prevent Bidirectional (BiDi) text inversion
and Markdown line-collapse.
"""

import re
import sys
import argparse

# Reconfigure stdout to UTF-8 for Windows console safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
MARKDOWN_LINK_RE = re.compile(r"(\[[^\]]+\]\([^)]+\))")
FILENAME_RE = re.compile(r"(`?[a-zA-Z0-9_\-\\]+\.(?:md|py|json|zip|pdf|txt|ts|js|html|css|exe|dll|yaml|yml)`?)", re.IGNORECASE)
INLINE_CODE_RE = re.compile(r"(`[^`]+`)")
ENGLISH_PHRASE_RE = re.compile(r"([A-Za-z][A-Za-z0-9_./\\:+-]*(?:\s+[A-Za-z0-9_./\\:+-]+)*)")

# Common transliterated / prefixed English words in Arabic that should be purified
ARABIC_EN_PREFIX_RE = re.compile(r"\bالـ\s*([A-Za-z0-9_\-]+)\b")


def contains_arabic(text: str) -> bool:
    """Check if string contains any Arabic characters."""
    return bool(ARABIC_RE.search(text))


def contains_english(text: str) -> bool:
    """Check if string contains Latin alphabet characters."""
    return bool(re.search(r"[A-Za-z]", text))


def is_mixed_inline(line: str) -> bool:
    """
    Determine if a line contains mixed Arabic and English/filenames/links inline,
    which triggers BiDi rendering issues.
    """
    if not (contains_arabic(line) and contains_english(line)):
        return False
    return True


def format_subagent_report(status: str, task: str, result: str, path: str = "") -> str:
    """
    Format a subagent report with clean stacked line separation
    and mandatory empty lines to ensure zero BiDi inversion.
    """
    blocks = [
        f"الحالة: {status}",
        f"المهمة:\n{task.strip()}",
        f"النتيجة:\n{result.strip()}",
    ]
    if path:
        blocks.append(f"المسار:\n{path.strip()}")
    return "\n\n".join(blocks)


def separate_bilingual_line(line: str) -> list:
    """
    Recursively split a line containing inline English links, filenames, code paths,
    or technical terms into dedicated, cleanly stacked lines following the Split & Continuation rule:
    1. Arabic text before -> line
    2. English term/link -> dedicated line
    3. Arabic continuation -> line following it
    """
    # 1. Clean up "الـ [English]" prefixes
    line = ARABIC_EN_PREFIX_RE.sub(r"\1", line)

    # 2. Handle markdown links first
    link_match = MARKDOWN_LINK_RE.search(line)
    if link_match and contains_arabic(line):
        start, end = link_match.span()
        before = line[:start].strip()
        link = link_match.group(1).strip()
        after = line[end:].strip()
        result = []
        if before:
            result.extend(separate_bilingual_line(before))
        result.append(link)
        if after:
            result.extend(separate_bilingual_line(after))
        return result

    # 3. Handle backticked inline code / filenames
    code_match = INLINE_CODE_RE.search(line)
    if code_match and contains_arabic(line):
        start, end = code_match.span()
        before = line[:start].strip()
        code = code_match.group(1).strip()
        after = line[end:].strip()
        result = []
        if before:
            result.extend(separate_bilingual_line(before))
        result.append(code)
        if after:
            result.extend(separate_bilingual_line(after))
        return result

    # 4. Handle raw filenames without backticks
    file_match = FILENAME_RE.search(line)
    if file_match and contains_arabic(line):
        start, end = file_match.span()
        before = line[:start].strip()
        filename = file_match.group(1).strip()
        after = line[end:].strip()
        result = []
        if before:
            result.extend(separate_bilingual_line(before))
        result.append(filename)
        if after:
            result.extend(separate_bilingual_line(after))
        return result

    # 5. Handle any English word, technical term, or phrase (Split & Continuation Rule)
    en_match = ENGLISH_PHRASE_RE.search(line)
    if en_match and contains_arabic(line):
        start, end = en_match.span()
        before = line[:start].strip()
        en_phrase = en_match.group(1).strip()
        after = line[end:].strip()
        result = []
        if before:
            result.extend(separate_bilingual_line(before))
        result.append(en_phrase)
        if after:
            result.extend(separate_bilingual_line(after))
        return result

    return [line] if line.strip() else []


def format_text(text: str) -> str:
    """Format full text document ensuring clean empty-line separation between blocks."""
    formatted_blocks = []
    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue
        if is_mixed_inline(raw_line):
            separated = separate_bilingual_line(raw_line)
            formatted_blocks.extend(separated)
        else:
            formatted_blocks.append(raw_line)
    return "\n\n".join(formatted_blocks)


def main():
    parser = argparse.ArgumentParser(description="Bilingual Formatter & BiDi Cleaner")
    parser.add_argument("--test", action="store_true", help="Run self-test on sample mixed text")
    parser.add_argument("--text", type=str, help="Text to format")
    args = parser.parse_args()

    if args.test:
        sample = (
            "تم تحديث ملف GEMINI.md و ملف README.md بنجاح.\n"
            "يرجى زيارة [موقع المشروع](https://github.com/project) للاطلاع على تفاصيل config.json."
        )
        print("--- Original Text ---")
        print(sample)
        print("\n--- Formatted Text (Empty-Line Separated) ---")
        formatted = format_text(sample)
        print(formatted)
        print("\n--- Sub-agent Report Example ---")
        report = format_subagent_report(
            status="ناجح",
            task="File Separation and Layout Optimization",
            result="تم عزل أسماء الملفات والروابط بنجاح في أسطر مستقلة ومفصولة بأسطر فارغة لمنع أي تداخل.",
            path="C:\\Users\\goldl\\Desktop\\antigravity_skills_pack.zip",
        )
        print(report)
        return 0

    if args.text:
        print(format_text(args.text))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
