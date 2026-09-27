"""
Loss Diagnostics and Training Curve Analyzer.
Detects training anomalies: NaN/Inf loss, loss spikes, overfitting, underfitting,
and learning rate stagnation from training log files (JSON/JSONL).
"""
import argparse
import json
import math
import os
import sys

def analyze_logs(log_file):
    if not os.path.exists(log_file):
        return {"status": "error", "message": f"Log file not found: {log_file}"}

    train_losses = []
    eval_losses = []
    steps = []

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                step = data.get("step") or data.get("current_step")
                if "loss" in data and data["loss"] is not None:
                    train_losses.append(float(data["loss"]))
                    if step is not None:
                        steps.append(step)
                if "eval_loss" in data and data["eval_loss"] is not None:
                    eval_losses.append(float(data["eval_loss"]))
            except json.JSONDecodeError:
                continue

    if not train_losses:
        return {"status": "error", "message": "No valid loss entries found in log file."}

    # Diagnostics checks
    issues = []
    recommendations = []

    # 1. Check for NaN or Inf
    has_nan = any(math.isnan(l) or math.isinf(l) for l in train_losses)
    if has_nan:
        issues.append("CRITICAL: Loss diverged to NaN or Inf.")
        recommendations.append("Reduce learning rate by 50%, switch to bf16 if using fp16, and check for zero-length sequences or division by zero.")

    # 2. Check for loss spikes
    spikes = 0
    for i in range(1, len(train_losses)):
        if train_losses[i] > train_losses[i - 1] * 2.5:
            spikes += 1
    if spikes > 0:
        issues.append(f"WARNING: Detected {spikes} severe loss spikes during training.")
        recommendations.append("Increase warmup_ratio (e.g. to 0.05 - 0.1), use gradient clipping (max_grad_norm=1.0), and inspect dataset for noisy samples.")

    # 3. Check for Overfitting
    if len(eval_losses) >= 3:
        # If train loss keeps dropping while eval loss rises in the last 2 checks
        if train_losses[-1] < train_losses[0] and eval_losses[-1] > eval_losses[-2] > eval_losses[-3]:
            issues.append("WARNING: Potential Overfitting detected (eval_loss is steadily rising while train_loss drops).")
            recommendations.append("Increase lora_dropout to 0.1, add weight_decay (0.01 - 0.1), or reduce the number of training epochs.")

    # 4. Check for Stagnation (Underfitting / Too low LR)
    if len(train_losses) >= 10:
        recent_loss_change = abs(train_losses[-1] - train_losses[-10])
        if recent_loss_change < 0.005 and train_losses[-1] > 1.5:
            issues.append("WARNING: Training loss has stagnated at a high value.")
            recommendations.append("Increase learning rate (e.g. from 1e-4 to 3e-4) or verify that training labels are not masked with -100 entirely.")

    status = "healthy" if not issues else ("critical" if has_nan else "warning")

    return {
        "status": status,
        "total_steps_recorded": len(train_losses),
        "initial_train_loss": round(train_losses[0], 4),
        "latest_train_loss": round(train_losses[-1], 4),
        "lowest_train_loss": round(min(train_losses), 4),
        "latest_eval_loss": round(eval_losses[-1], 4) if eval_losses else None,
        "issues_detected": issues,
        "actionable_recommendations": recommendations
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze AI model training logs")
    parser.add_argument("--log-file", type=str, required=True, help="Path to JSON/JSONL training log file")
    args = parser.parse_args()

    result = analyze_logs(args.log_file)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
