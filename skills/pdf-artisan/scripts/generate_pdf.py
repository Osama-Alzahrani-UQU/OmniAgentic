"""
Universal PDF Generator for Windows.
Supports:
1. HTML-to-PDF via native Windows headless browser (Edge/Chrome) for modern CSS, Flexbox, and Arabic RTL.
2. Programmatic PDF generation with Arabic text shaping.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

def find_browser():
    """Finds Microsoft Edge or Chrome executable for native headless PDF printing."""
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        shutil.which("msedge"),
        shutil.which("chrome")
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None

def html_to_pdf_browser(html_path, output_pdf_path):
    browser = find_browser()
    if not browser:
        return {"status": "error", "message": "Neither Microsoft Edge nor Chrome found on system."}

    abs_html = os.path.abspath(html_path).replace("\\", "/")
    abs_pdf = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(abs_pdf), exist_ok=True)

    # Use native browser headless print-to-pdf
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html}"
    ]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 0:
            return {
                "status": "success",
                "engine": "headless_browser",
                "browser": browser,
                "input_html": abs_html,
                "output_pdf": abs_pdf.replace("\\", "/"),
                "file_size_bytes": os.path.getsize(abs_pdf)
            }
        else:
            return {"status": "error", "message": "PDF was not created or is empty", "stderr": res.stderr}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def shape_arabic(text):
    """Shapes Arabic letters and applies bidirectional algorithm if libraries are installed."""
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except ImportError:
        return text

def create_sample_reportlab_pdf(output_pdf, title="تقرير"):
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        os.makedirs(os.path.dirname(os.path.abspath(output_pdf)), exist_ok=True)
        c = canvas.Canvas(output_pdf, pagesize=letter)
        shaped_title = shape_arabic(title)
        c.drawString(100, 750, shaped_title)
        c.save()
        return {
            "status": "success",
            "engine": "reportlab",
            "output_pdf": os.path.abspath(output_pdf).replace("\\", "/")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Universal PDF Generator")
    parser.add_argument("--html", type=str, default=None, help="Path to input HTML file")
    parser.add_argument("--output", "-o", type=str, required=True, help="Path to output PDF file")
    parser.add_argument("--title", type=str, default=None, help="Title for sample reportlab PDF")
    args = parser.parse_args()

    if args.html:
        res = html_to_pdf_browser(args.html, args.output)
    else:
        res = create_sample_reportlab_pdf(args.output, title=args.title or "Document")

    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
