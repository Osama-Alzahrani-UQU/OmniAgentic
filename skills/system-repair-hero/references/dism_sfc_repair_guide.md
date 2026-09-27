# Windows DISM, SFC & System Repair Guide

A technical reference for repairing corrupted Windows component stores, missing system files, and filesystem damage.

---

## 1. Why the Order Matters: DISM First, SFC Second

```
Windows Update / Source Image
           â”‚
           â–¼
Windows Component Store (WinSxS)  <--- Repaired by DISM
           â”‚
           â–¼
Active System Files (System32)     <--- Repaired by SFC
```

- **SFC (System File Checker)** compares system files against the local Component Store (`C:\Windows\WinSxS`).
- If the Component Store itself is corrupted, SFC cannot repair damaged files because its source is corrupted.
- Therefore, **DISM must always run before SFC** when doing a full system restoration.

---

## 2. DISM Command Reference

### CheckHealth (Instant)
Checks if an existing corruption flag is present in the component store:
```cmd
dism /online /cleanup-image /checkhealth
```

### ScanHealth (Thorough, 5-10 minutes)
Scans the entire component store to detect hidden corruption:
```cmd
dism /online /cleanup-image /scanhealth
```

### RestoreHealth (Repair)
Downloads healthy replacement files from Windows Update and repairs WinSxS:
```cmd
dism /online /cleanup-image /restorehealth
```

---

## 3. SFC Command Reference

### Scannow (Repair)
Scans and repairs all protected operating system files:
```cmd
sfc /scannow
```

### Log File Analysis
Detailed SFC logs are stored in:
`C:\Windows\Logs\CBS\CBS.log`

To extract only the SFC repair entries:
```cmd
findstr /c:"[SR]" %windir%\Logs\CBS\CBS.log > "%userprofile%\Desktop\sfc_results.txt"
```

---

## 4. CHKDSK Online Scan

To check for filesystem corruption without rebooting or unmounting the drive:
```cmd
chkdsk C: /scan
```
If errors are found that require offline fixing:
```cmd
chkdsk C: /f /r
```
(Requires restart confirmation).
