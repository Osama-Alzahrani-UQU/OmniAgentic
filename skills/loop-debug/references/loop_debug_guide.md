# Loop Debug Reference Guide

This reference provides technical methodologies for autonomous iterative debugging across diverse runtime environments.

---

## 1. Loop Debug Workflow Across Stacks

### Python Environments
- **Trigger**: `python script.py` or `pytest -v`.
- **Diagnosis**: Inspect `Traceback (most recent call last):`. Check line numbers, `AttributeError`, `ImportError`, or `TypeError`.
- **Repair**: Use `replace_file_content` to fix null references, type mismatches, or missing parameters.
- **Verification**: Re-run until exit code `0` and clean stdout.

### Node.js / TypeScript
- **Trigger**: `npx tsc --noEmit` followed by `node script.js` or `npm test`.
- **Diagnosis**: Check TypeScript type errors (`TS2339`, `TS2322`), unhandled promise rejections, or missing packages.
- **Repair**: Fix types, add missing exports/imports, or install missing dependencies via `npm install <pkg>`.
- **Verification**: Re-run typecheck and test until zero errors.

### Compiled Languages (C / C++ / Rust / Go)
- **Trigger**: Build command (`cargo build`, `cmake --build`, `go build`).
- **Diagnosis**: Compiler diagnostics (borrow checker, undefined reference, linker errors).
- **Repair**: Fix memory semantics, include headers, or update build files.
- **Verification**: Rebuild and execute binary.

---

## 2. Best Practices for Autonomous Loop Iteration

1. **Incremental Patches**: Fix the primary root-cause exception first before attempting wholesale refactors.
2. **Log Enrichment**: If an error is opaque, insert temporary diagnostic prints (`print("[DEBUG] ...")`), re-run to inspect intermediate states, fix the issue, and clean up the prints.
3. **Environmental Checks**: Verify working directory (`Cwd`), active virtual environments, and file permissions if execution fails without code tracebacks.
