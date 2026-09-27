"""
Screen capture utility for Desktop Automator.
Captures full screen or a specified bounding box, saves to a temporary or specified directory,
and outputs image path and dimensions in JSON format.
"""
import argparse
import json
import os
import sys
import tempfile
import time
from PIL import ImageGrab

def capture_screen(output_path=None, bbox=None):
    if not output_path:
        temp_dir = os.path.join(tempfile.gettempdir(), "antigravity_screenshots")
        os.makedirs(temp_dir, exist_ok=True)
        filename = f"screenshot_{int(time.time() * 1000)}.png"
        output_path = os.path.join(temp_dir, filename)
    else:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Capture screen across all connected monitors
    screenshot = ImageGrab.grab(bbox=bbox, all_screens=True)
    screenshot.save(output_path, "PNG")

    width, height = screenshot.size
    result = {
        "status": "success",
        "file_path": os.path.abspath(output_path).replace("\\", "/"),
        "width": width,
        "height": height,
        "bbox": bbox
    }
    return result

def main():
    parser = argparse.ArgumentParser(description="Capture desktop screenshot")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output image file path")
    parser.add_argument("--bbox", type=int, nargs=4, default=None, help="Bounding box: left top right bottom")
    args = parser.parse_args()

    try:
        res = capture_screen(output_path=args.output, bbox=tuple(args.bbox) if args.bbox else None)
        print(json.dumps(res, indent=2))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
