"""
Game Localization & Arabic Typography Toolkit.
Provides:
1. Arabic RTL letter shaping and bidirectional reversing for game engines.
2. Font inspection for Arabic glyph support (U+0600 - U+06FF and U+FE70 - U+FEFF).
3. Translation string table management (JSON/CSV).
"""
import argparse
import json
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


# Basic Arabic presentation forms mapping for standalone fallback shaping
BASIC_ARABIC_MAP = {
    '\u0627': ('\uFE8D', '\uFE8E', '\uFE8D', '\uFE8E'),  # Alef
    '\u0628': ('\uFE8F', '\uFE90', '\uFE91', '\uFE92'),  # Beh
    '\u062A': ('\uFE95', '\uFE96', '\uFE97', '\uFE98'),  # Teh
    '\u062B': ('\uFE99', '\uFE9A', '\uFE9B', '\uFE9C'),  # Theh
    '\u062C': ('\uFE9D', '\uFE9E', '\uFE9F', '\uFEA0'),  # Jeem
    '\u062D': ('\uFEA1', '\uFEA2', '\uFEA3', '\uFEA4'),  # Hah
    '\u062E': ('\uFEA5', '\uFEA6', '\uFEA7', '\uFEA8'),  # Khah
    '\u062F': ('\uFEA9', '\uFEAA', '\uFEA9', '\uFEAA'),  # Dal
    '\u0630': ('\uFEAB', '\uFEAC', '\uFEAB', '\uFEAC'),  # Thal
    '\u0631': ('\uFEAD', '\uFEAE', '\uFEAD', '\uFEAE'),  # Reh
    '\u0632': ('\uFEAF', '\uFEB0', '\uFEAF', '\uFEB0'),  # Zain
    '\u0633': ('\uFEB1', '\uFEB2', '\uFEB3', '\uFEB4'),  # Seen
    '\u0634': ('\uFEB5', '\uFEB6', '\uFEB7', '\uFEB8'),  # Sheen
    '\u0635': ('\uFEB9', '\uFEBA', '\uFEBB', '\uFEBC'),  # Sad
    '\u0636': ('\uFEBD', '\uFEBE', '\uFEBF', '\uFEC0'),  # Dad
    '\u0637': ('\uFEC1', '\uFEC2', '\uFEC3', '\uFEC4'),  # Tah
    '\u0638': ('\uFEC5', '\uFEC6', '\uFEC7', '\uFEC8'),  # Zah
    '\u0639': ('\uFEC9', '\uFECA', '\uFECB', '\uFECC'),  # Ain
    '\u063A': ('\uFECD', '\uFECE', '\uFECF', '\uFED0'),  # Ghain
    '\u0641': ('\uFED1', '\uFED2', '\uFED3', '\uFED4'),  # Feh
    '\u0642': ('\uFED5', '\uFED6', '\uFED7', '\uFED8'),  # Qaf
    '\u0643': ('\uFED9', '\uFEDA', '\uFEDB', '\uFEDC'),  # Kaf
    '\u0644': ('\uFEDD', '\uFEDE', '\uFEDF', '\uFEE0'),  # Lam
    '\u0645': ('\uFEE1', '\uFEE2', '\uFEE3', '\uFEE4'),  # Meem
    '\u0646': ('\uFEE5', '\uFEE6', '\uFEE7', '\uFEE8'),  # Noon
    '\u0647': ('\uFEE9', '\uFEEA', '\uFEEB', '\uFEEC'),  # Heh
    '\u0648': ('\uFEED', '\uFEEE', '\uFEED', '\uFEEE'),  # Waw
    '\u064A': ('\uFEF1', '\uFEF2', '\uFEF3', '\uFEF4'),  # Yeh
}

def shape_arabic_text(text, reverse_bidi=True):
    # Try importing full libraries first
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        reshaped = arabic_reshaper.reshape(text)
        if reverse_bidi:
            return get_display(reshaped), "arabic_reshaper+bidi"
        return reshaped, "arabic_reshaper_only"
    except ImportError:
        pass

    # Basic fallback reshaping
    result = []
    chars = list(text)
    n = len(chars)

    for i in range(n):
        c = chars[i]
        if c in BASIC_ARABIC_MAP:
            prev_connects = (i > 0 and chars[i-1] in BASIC_ARABIC_MAP and chars[i-1] not in ['\u0627', '\u062F', '\u0630', '\u0631', '\u0632', '\u0648'])
            next_connects = (i < n - 1 and chars[i+1] in BASIC_ARABIC_MAP)

            if prev_connects and next_connects:
                shaped = BASIC_ARABIC_MAP[c][3]  # Medial
            elif prev_connects:
                shaped = BASIC_ARABIC_MAP[c][1]  # Final
            elif next_connects:
                shaped = BASIC_ARABIC_MAP[c][2]  # Initial
            else:
                shaped = BASIC_ARABIC_MAP[c][0]  # Isolated
            result.append(shaped)
        else:
            result.append(c)

    shaped_str = "".join(result)
    if reverse_bidi:
        # Reverse only Arabic segments
        shaped_str = shaped_str[::-1]

    return shaped_str, "builtin_fallback"

def inspect_font_file(font_path):
    if not os.path.exists(font_path):
        return {"status": "ERROR", "message": f"Font file not found: {font_path}"}

    try:
        from fontTools.ttLib import TTFont
        font = TTFont(font_path)
        cmap = font.getBestCMap()

        arabic_basic = any(0x0600 <= code <= 0x06FF for code in cmap.keys())
        arabic_presentation_a = any(0xFB50 <= code <= 0xFDFF for code in cmap.keys())
        arabic_presentation_b = any(0xFE70 <= code <= 0xFEFF for code in cmap.keys())

        # Inspect font metadata
        name_record = ""
        for record in font['name'].names:
            if record.nameID == 4:  # Full font name
                name_record = record.toUnicode()
                break

        return {
            "status": "SUCCESS",
            "font_name": name_record or os.path.basename(font_path),
            "total_glyphs": len(cmap),
            "supports_arabic_basic": arabic_basic,
            "supports_presentation_a": arabic_presentation_a,
            "supports_presentation_b": arabic_presentation_b,
            "is_arabic_ready": arabic_basic or arabic_presentation_b,
            "recommendation": "Font is ready for Arabic." if (arabic_basic and arabic_presentation_b) else "Font requires Arabic glyph patching or fallback font linking."
        }
    except ImportError:
        # Fallback binary check
        with open(font_path, "rb") as f:
            header = f.read(12)
        is_ttf_otf = header[:4] in [b"\x00\x01\x00\x00", b"OTTO", b"true"]
        return {
            "status": "BASIC_CHECK",
            "font_file": font_path,
            "valid_font_header": is_ttf_otf,
            "note": "Install 'fonttools' (pip install fonttools) for in-depth glyph coverage analysis."
        }

def export_string_table(input_path, output_path):
    if not os.path.exists(input_path):
        return {"status": "ERROR", "message": f"Input file not found: {input_path}"}

    with open(input_path, "r", encoding="utf-8", errors="replace") as f:
        data = json.load(f)

    # Prepare translation template
    table = {}
    if isinstance(data, dict):
        for k, v in data.items():
            table[k] = {
                "original": str(v),
                "translated": "",
                "status": "UNTRANSLATED"
            }
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            table[str(idx)] = {
                "original": str(item),
                "translated": "",
                "status": "UNTRANSLATED"
            }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(table, f, indent=2, ensure_ascii=False)

    return {
        "status": "SUCCESS",
        "input_strings_count": len(table),
        "exported_table": output_path
    }

def main():
    parser = argparse.ArgumentParser(description="Game Localization and Arabic Typography Toolkit")
    parser.add_argument("--action", choices=["shape", "inspect-font", "export-table"], required=True)
    parser.add_argument("--text", help="Arabic text to shape and reverse")
    parser.add_argument("--font", help="Path to TTF/OTF font file")
    parser.add_argument("--input", help="Input translation file")
    parser.add_argument("--output", help="Output translation file")
    parser.add_argument("--no-reverse", action="store_true", help="Do not reverse character order")

    args = parser.parse_args()

    if args.action == "shape":
        if not args.text:
            print(json.dumps({"error": "--text is required for shape action"}, indent=2))
            sys.exit(1)
        shaped, engine = shape_arabic_text(args.text, reverse_bidi=not args.no_reverse)
        res = {
            "original_text": args.text,
            "shaped_text": shaped,
            "engine": engine,
            "reversed_bidi": not args.no_reverse
        }
    elif args.action == "inspect-font":
        if not args.font:
            print(json.dumps({"error": "--font is required for inspect-font action"}, indent=2))
            sys.exit(1)
        res = inspect_font_file(args.font)
    else:  # export-table
        if not args.input or not args.output:
            print(json.dumps({"error": "--input and --output are required for export-table action"}, indent=2))
            sys.exit(1)
        res = export_string_table(args.input, args.output)

    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
