"""
Educational Exercise and Code Verification Utility.
Runs student code against test cases and generates constructive pedagogical hints
instead of raw cryptic error dumps.
"""
import argparse
import json
import os
import subprocess
import sys

def verify_code(code_file, expected_output=None, timeout=10):
    if not os.path.exists(code_file):
        return {"status": "error", "message": f"Code file not found: {code_file}"}

    try:
        res = subprocess.run(
            [sys.executable, code_file],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout
        )
        stdout = res.stdout.strip()
        stderr = res.stderr.strip()
        code = res.returncode
    except subprocess.TimeoutExpired:
        return {
            "status": "failed",
            "verdict": "TIMEOUT",
            "hint": "Your code took too long to run. Check if you have an infinite loop (e.g. a while loop whose condition never changes)."
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

    # Generate pedagogical feedback
    if code != 0:
        hint = "There is a runtime error in your code."
        if "SyntaxError" in stderr:
            hint = "Check for missing parentheses, unclosed quotes, or missing colons ':' at the end of if/for/def statements."
        elif "IndentationError" in stderr:
            hint = "Look at the indentation (spaces/tabs). In Python, all code inside a block must be indented consistently."
        elif "NameError" in stderr:
            hint = "You are trying to use a variable or function that hasn't been defined yet, or there is a spelling typo."
        elif "TypeError" in stderr:
            hint = "Check the data types being passed. You might be trying to combine incompatible types (like adding a string to an integer)."
        elif "IndexError" in stderr:
            hint = "You are trying to access an item at an index that doesn't exist. Check if your list/sequence is empty or shorter than expected."

        return {
            "status": "failed",
            "verdict": "RUNTIME_ERROR",
            "stderr_summary": stderr.splitlines()[-1] if stderr else "",
            "pedagogical_hint": hint
        }

    if expected_output:
        if expected_output.strip() in stdout:
            return {
                "status": "passed",
                "verdict": "CONGRATULATIONS",
                "message": "Exercise completed successfully! Your output matches the expected result.",
                "output": stdout
            }
        else:
            return {
                "status": "needs_revision",
                "verdict": "OUTPUT_MISMATCH",
                "expected": expected_output.strip(),
                "actual_output": stdout,
                "pedagogical_hint": "Your code ran without errors, but the output did not match the expected result. Compare the output carefully."
            }

    return {
        "status": "passed",
        "verdict": "EXECUTED_SUCCESSFULLY",
        "output": stdout
    }

def main():
    parser = argparse.ArgumentParser(description="Verify student programming exercise")
    parser.add_argument("--code-file", type=str, required=True, help="Path to student code file")
    parser.add_argument("--expected", type=str, default=None, help="Expected output string")
    parser.add_argument("--timeout", type=int, default=10, help="Max execution timeout")
    args = parser.parse_args()

    result = verify_code(args.code_file, expected_output=args.expected, timeout=args.timeout)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
