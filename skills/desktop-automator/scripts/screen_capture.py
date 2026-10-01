"""
Screen capture and window inspection utility for Desktop Automator.
Captures full screen, specific bounding boxes, or targeted application windows.
Outputs image path and dimensions in JSON format for easy subagent consumption.
"""
import argparse
import ctypes
import json
import os
import sys
import tempfile
import time
from PIL import ImageGrab

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def attach_input_desktop():
    """Ensure current thread is attached to the active interactive input desktop."""
    if sys.platform == "win32":
        try:
            h_desk = ctypes.windll.user32.OpenInputDesktop(0, False, 0x01FF)
            if h_desk:
                ctypes.windll.user32.SetThreadDesktop(h_desk)
        except Exception:
            pass


def list_visible_windows(min_size=50):
    """Returns a list of all visible top-level application windows."""
    attach_input_desktop()
    windows = []

    try:
        import win32gui
        import win32process

        def enum_handler(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd).strip()
                rect = win32gui.GetWindowRect(hwnd)
                w = rect[2] - rect[0]
                h = rect[3] - rect[1]
                if title and w >= min_size and h >= min_size:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    windows.append({
                        "hwnd": hwnd,
                        "pid": pid,
                        "title": title,
                        "rect": [rect[0], rect[1], rect[2], rect[3]],
                        "width": w,
                        "height": h
                    })

        win32gui.EnumWindows(enum_handler, None)
    except ImportError:
        pass

    return windows


def find_window_by_title(query):
    """Finds the best matching visible window by title substring."""
    windows = list_visible_windows()
    query_lower = query.lower()

    # Exact or substring match
    matches = [w for w in windows if query_lower in w["title"].lower()]
    if matches:
        return matches[0]
    return None


def focus_window(hwnd):
    """Brings the target window to the foreground."""
    if sys.platform == "win32":
        try:
            import win32gui
            import win32con
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.15)
        except Exception:
            pass


def capture_screen(output_path=None, bbox=None, window_query=None, active_window=False):
    """Captures desktop or targeted window and returns JSON result."""
    attach_input_desktop()

    target_window_info = None

    if window_query:
        target_window_info = find_window_by_title(window_query)
        if not target_window_info:
            raise ValueError(f"No visible window found matching title: '{window_query}'")
        focus_window(target_window_info["hwnd"])
        bbox = tuple(target_window_info["rect"])

    elif active_window:
        try:
            import win32gui
            hwnd = win32gui.GetForegroundWindow()
            if hwnd:
                rect = win32gui.GetWindowRect(hwnd)
                title = win32gui.GetWindowText(hwnd).strip()
                target_window_info = {
                    "hwnd": hwnd,
                    "title": title,
                    "rect": list(rect)
                }
                bbox = rect
        except ImportError:
            pass

    if not output_path:
        temp_dir = os.path.join(tempfile.gettempdir(), "antigravity_screenshots")
        os.makedirs(temp_dir, exist_ok=True)
        filename = f"screenshot_{int(time.time() * 1000)}.png"
        output_path = os.path.join(temp_dir, filename)
    else:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Capture screen across all connected monitors or target bbox
    screenshot = ImageGrab.grab(bbox=bbox, all_screens=(bbox is None))
    screenshot.save(output_path, "PNG")

    width, height = screenshot.size
    result = {
        "status": "success",
        "file_path": os.path.abspath(output_path).replace("\\", "/"),
        "width": width,
        "height": height,
        "bbox": list(bbox) if bbox else None,
        "window": target_window_info
    }
    return result


def main():
    parser = argparse.ArgumentParser(description="Capture desktop screenshot or inspect windows")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output image file path")
    parser.add_argument("--bbox", type=int, nargs=4, default=None, help="Bounding box: left top right bottom")
    parser.add_argument("--window", "-w", type=str, default=None, help="Capture specific window by title substring")
    parser.add_argument("--active-window", "-a", action="store_true", help="Capture currently active/focused window")
    parser.add_argument("--list-windows", "-l", action="store_true", help="List all open visible application windows")
    args = parser.parse_args()

    if args.list_windows:
        wins = list_visible_windows()
        print(json.dumps({"status": "success", "count": len(wins), "windows": wins}, indent=2, ensure_ascii=False))
        return 0

    try:
        res = capture_screen(
            output_path=args.output,
            bbox=tuple(args.bbox) if args.bbox else None,
            window_query=args.window,
            active_window=args.active_window
        )
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
