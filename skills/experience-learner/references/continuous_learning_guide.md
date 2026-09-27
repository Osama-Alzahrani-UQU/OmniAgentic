# Continuous Experience Learning Reference Guide

This guide details how coding agents maintain cross-session and cross-project memory of errors, bugfixes, and architecture pitfalls.

---

## 1. The Core Lifecycle of Experience Learning

1. **Query Before Starting**:
   - Check `C:\Users\goldl\.gemini\knowledge\troubleshooting_history.md` for past experiences relevant to the current user prompt.
   - If a similar failure happened previously, adopt the verified solution directly.

2. **Diagnose and Fix**:
   - Resolve issues autonomously using `loop-debug` and `goal-verifier`.

3. **Log the Resolution**:
   - Run `experience_manager.py add` or append directly to the troubleshooting file.
   - Provide the exact error symptom, root cause, working solution, and prevention invariant.

4. **Never Repeat**:
   - Once a failure mode is recorded, the assistant is permanently barred from attempting that same broken strategy in future conversations.
