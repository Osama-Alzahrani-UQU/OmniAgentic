#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Debug Loop Runner Utility
Executes commands in an automated test-and-evaluate loop.
Captures stdout/stderr, evaluates exit codes, and reports status.
"""

import sys
import subprocess
import argparse
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def run_debug_iteration(command: str, timeout: int = 30) -> tuple:
    """Run a single command iteration and capture exit code, stdout, stderr."""
    try:
        proc = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace"
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return -1, "", f"Command timed out after {timeout} seconds."
    except Exception as e:
        return -2, "", str(e)


def main():
    parser = argparse.ArgumentParser(description="Autonomous Debug Loop Runner")
    parser.add_argument("--cmd", type=str, required=True, help="Command to execute for verification")
    parser.add_argument("--expect", type=str, default="", help="Expected substring in output")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout in seconds per run")
    args = parser.parse_args()

    print(f"=== [LOOP-DEBUG] Executing: {args.cmd} ===")
    returncode, stdout, stderr = run_debug_iteration(args.cmd, timeout=args.timeout)

    print(f"Exit Code: {returncode}")
    if stdout.strip():
        print(f"--- Standard Output ---\n{stdout.strip()}")
    if stderr.strip():
        print(f"--- Standard Error ---\n{stderr.strip()}")

    # Evaluation
    is_success = (returncode == 0)
    if args.expect and args.expect not in stdout:
        is_success = False
        print(f"[GATE FAILED] Expected pattern '{args.expect}' not found in stdout.")

    if is_success:
        print("\n>>> [GATE PASSED] Verification succeeded 100% error-free. Exit loop permitted. <<<")
        sys.exit(0)
    else:
        print("\n>>> [GATE BLOCKED] Errors or failures detected. Assistant must diagnose, patch, and re-loop. <<<")
        sys.exit(1)


if __name__ == "__main__":
    main()
