"""
Mouse and keyboard action controller for Desktop Automator.
Uses pyautogui with failsafe enabled and smooth human-like transitions.
"""
import argparse
import json
import sys
import time
import pyautogui

# Enable failsafe: moving mouse to (0,0) immediately aborts execution
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2  # Short pause after each action to ensure UI stability

def perform_click(x, y, button="left", clicks=1):
    pyautogui.click(x=x, y=y, button=button, clicks=clicks)
    return {"action": "click", "x": x, "y": y, "button": button, "clicks": clicks}

def perform_type(text, interval=0.03):
    pyautogui.write(text, interval=interval)
    return {"action": "type", "text": text}

def perform_hotkey(keys):
    key_list = [k.strip().lower() for k in keys.split(",") if k.strip()]
    pyautogui.hotkey(*key_list)
    return {"action": "hotkey", "keys": key_list}

def perform_drag(start_x, start_y, end_x, end_y, duration=0.5):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button="left")
    return {"action": "drag", "start": [start_x, start_y], "end": [end_x, end_y]}

def perform_scroll(clicks, x=None, y=None):
    if x is not None and y is not None:
        pyautogui.moveTo(x, y)
    pyautogui.scroll(clicks)
    return {"action": "scroll", "clicks": clicks, "x": x, "y": y}

def get_mouse_position():
    x, y = pyautogui.position()
    return {"action": "get_position", "x": x, "y": y}

def main():
    parser = argparse.ArgumentParser(description="Execute desktop mouse and keyboard actions")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Click
    click_p = subparsers.add_parser("click")
    click_p.add_argument("--x", type=int, required=True)
    click_p.add_argument("--y", type=int, required=True)
    click_p.add_argument("--button", choices=["left", "right", "middle"], default="left")

    # Double click
    dclick_p = subparsers.add_parser("double-click")
    dclick_p.add_argument("--x", type=int, required=True)
    dclick_p.add_argument("--y", type=int, required=True)

    # Right click
    rclick_p = subparsers.add_parser("right-click")
    rclick_p.add_argument("--x", type=int, required=True)
    rclick_p.add_argument("--y", type=int, required=True)

    # Type
    type_p = subparsers.add_parser("type")
    type_p.add_argument("--text", type=str, required=True)
    type_p.add_argument("--interval", type=float, default=0.03)

    # Hotkey
    hotkey_p = subparsers.add_parser("hotkey")
    hotkey_p.add_argument("--keys", type=str, required=True, help="Comma-separated keys, e.g. 'ctrl,s' or 'alt,tab'")

    # Drag
    drag_p = subparsers.add_parser("drag")
    drag_p.add_argument("--start-x", type=int, required=True)
    drag_p.add_argument("--start-y", type=int, required=True)
    drag_p.add_argument("--end-x", type=int, required=True)
    drag_p.add_argument("--end-y", type=int, required=True)
    drag_p.add_argument("--duration", type=float, default=0.5)

    # Scroll
    scroll_p = subparsers.add_parser("scroll")
    scroll_p.add_argument("--clicks", type=int, required=True, help="Positive scrolls up, negative down")
    scroll_p.add_argument("--x", type=int, default=None)
    scroll_p.add_argument("--y", type=int, default=None)

    # Position
    subparsers.add_parser("position")

    args = parser.parse_args()

    try:
        if args.command == "click":
            res = perform_click(args.x, args.y, button=args.button, clicks=1)
        elif args.command == "double-click":
            res = perform_click(args.x, args.y, button="left", clicks=2)
        elif args.command == "right-click":
            res = perform_click(args.x, args.y, button="right", clicks=1)
        elif args.command == "type":
            res = perform_type(args.text, interval=args.interval)
        elif args.command == "hotkey":
            res = perform_hotkey(args.keys)
        elif args.command == "drag":
            res = perform_drag(args.start_x, args.start_y, args.end_x, args.end_y, duration=args.duration)
        elif args.command == "scroll":
            res = perform_scroll(args.clicks, args.x, args.y)
        elif args.command == "position":
            res = get_mouse_position()
        else:
            res = {"status": "unknown_command"}

        res["status"] = "success"
        print(json.dumps(res, indent=2))
    except pyautogui.FailSafeException:
        print(json.dumps({
            "status": "aborted",
            "error": "PyAutoGUI FailSafe triggered: mouse moved to screen corner (0, 0)."
        }), file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(json.dumps({"status": "error", "error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
