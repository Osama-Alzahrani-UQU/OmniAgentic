"""
Windows System Integrity & Component Store Repair Orchestrator.
Automates and coordinates:
1. DISM Component Store Health Check and Repair (CheckHealth / RestoreHealth)
2. SFC (System File Checker) integrity verification (verifyonly / scannow)
Produces structured JSON diagnostic summaries.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime

def run_command_safe(cmd_list, timeout_sec=300):
    try:
        proc = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            errors="replace"
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out."
    except Exception as e:
        return -1, "", str(e)

def parse_sfc_output(output):
    if "did not find any integrity violations" in output:
        return "CLEAN", "Windows Resource Protection did not find any integrity violations."
    elif "found corrupt files and successfully repaired them" in output:
        return "REPAIRED", "Windows Resource Protection found corrupt files and successfully repaired them."
    elif "found corrupt files but was unable to fix some of them" in output:
        return "CORRUPTED_UNFIXED", "Windows Resource Protection found corrupt files but was unable to fix some of them."
    return "UNKNOWN", output[:300] if output else "No output"

def parse_dism_output(output):
    if "No component store corruption detected" in output:
        return "HEALTHY", "No component store corruption detected."
    elif "The component store is repairable" in output:
        return "REPAIRABLE", "Component store corruption detected, repairable via RestoreHealth."
    elif "The restore operation completed successfully" in output:
        return "RESTORED", "The restore operation completed successfully."
    return "STATUS", output[:300] if output else "No output"

def run_check():
    results = {}

    # 1. DISM CheckHealth
    code, stdout, stderr = run_command_safe(["dism", "/online", "/cleanup-image", "/checkhealth"], timeout_sec=60)
    dism_status, dism_msg = parse_dism_output(stdout)
    results["dism_check"] = {
        "status": dism_status,
        "details": dism_msg,
        "exit_code": code
    }

    # 2. SFC VerifyOnly
    code_sfc, stdout_sfc, stderr_sfc = run_command_safe(["sfc", "/verifyonly"], timeout_sec=300)
    sfc_status, sfc_msg = parse_sfc_output(stdout_sfc)
    results["sfc_verify"] = {
        "status": sfc_status,
        "details": sfc_msg,
        "exit_code": code_sfc
    }

    overall = "HEALTHY" if dism_status == "HEALTHY" and sfc_status == "CLEAN" else "ATTENTION_NEEDED"

    return {
        "timestamp": datetime.now().isoformat(),
        "action": "check",
        "overall_status": overall,
        "results": results,
        "recommendation": "System files intact." if overall == "HEALTHY" else "Run with '--action restore' to repair corrupted components."
    }

def run_restore():
    results = {}

    # 1. DISM RestoreHealth
    code, stdout, stderr = run_command_safe(["dism", "/online", "/cleanup-image", "/restorehealth"], timeout_sec=600)
    dism_status, dism_msg = parse_dism_output(stdout)
    results["dism_restore"] = {
        "status": dism_status,
        "details": dism_msg,
        "exit_code": code
    }

    # 2. SFC Scannow
    code_sfc, stdout_sfc, stderr_sfc = run_command_safe(["sfc", "/scannow"], timeout_sec=600)
    sfc_status, sfc_msg = parse_sfc_output(stdout_sfc)
    results["sfc_scannow"] = {
        "status": sfc_status,
        "details": sfc_msg,
        "exit_code": code_sfc
    }

    return {
        "timestamp": datetime.now().isoformat(),
        "action": "restore",
        "results": results,
        "summary": "DISM and SFC repair sequence completed."
    }

def main():
    parser = argparse.ArgumentParser(description="Windows System Integrity & Repair Orchestrator")
    parser.add_argument("--action", choices=["check", "restore"], default="check", help="Action to perform (check / restore)")
    args = parser.parse_args()

    if args.action == "check":
        report = run_check()
    else:
        report = run_restore()

    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
