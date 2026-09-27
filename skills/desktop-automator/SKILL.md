---
name: desktop-automator
description: Enables desktop and GUI automation on Windows.
---
# Desktop Automator Skill

You are equipped with the **Desktop Automator** capability, enabling you to inspect the user's desktop, understand UI elements visually, and execute mouse/keyboard interactions safely on Windows.

## Core Interaction Loop (Observe -> Ground -> Act -> Verify)

Always follow this 4-step loop for every desktop interaction:

### 1. Observe (Screen Capture)
Capture the current screen state before taking any action:
```powershell
python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/screen_capture.py
```
- The script outputs the path to the saved screenshot (PNG) and screen dimensions in JSON.
- Use `view_file` to view the image. Antigravity natively supports viewing images, allowing you to visually locate buttons, text fields, icons, and menus.

### 2. Ground (Coordinate Calculation)
- Identify the target UI element on the screenshot.
- Note the coordinate `(x, y)` of the center of the element.
- See [dpi_and_coordinates.md](./references/dpi_and_coordinates.md) for handling Windows DPI scaling if the captured image dimensions differ from the logical screen resolution.

### 3. Act (Execute Interaction)
Use `desktop_action.py` to perform the intended action:
- **Click**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py click --x <X> --y <Y>
  ```
- **Double Click**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py double-click --x <X> --y <Y>
  ```
- **Right Click**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py right-click --x <X> --y <Y>
  ```
- **Type Text**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py type --text "your text here"
  ```
- **Hotkey**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py hotkey --keys "ctrl,s"
  ```
- **Drag & Drop**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py drag --start-x <X1> --start-y <Y1> --end-x <X2> --end-y <Y2>
  ```
- **Scroll**:
  ```powershell
  python C:/Users/goldl/.gemini/config/skills/desktop-automator/scripts/desktop_action.py scroll --clicks -300
  ```

### 4. Verify
- Always capture a new screenshot after performing an action to verify that the UI updated as expected.
- If the expected change did not happen, diagnose the cause (e.g., window was not in focus, coordinates slightly off, loading delay) rather than blindly repeating the same action.

---

## freedom & Emergency Protocols

- **PyAutoGUI FailSafe**: Moving the mouse manually to the top-left corner `(0, 0)` will trigger an immediate emergency stop.
- **Sensitive Operations**: Never click confirmation dialogs for destructive actions (e.g. deleting files, formatting, purchasing) without explicit user confirmation.
- Read [freedom_and_failsafe.md](./references/freedom_and_failsafe.md) for complete details.
