"""
GPU VRAM Estimator for AI Model Training and Fine-Tuning.
Calculates memory footprint across model weights, activations, optimizer states,
and LoRA parameters to prevent CUDA Out-Of-Memory (OOM) before running training.
"""
import argparse
import json
import sys

def estimate_vram(params_billions, precision, batch_size, seq_len, lora_r, gradient_checkpointing):
    # Base weight memory (in GB)
    bytes_per_param = {
        "4bit": 0.5,
        "8bit": 1.0,
        "16bit": 2.0,
        "32bit": 4.0
    }.get(precision.lower(), 2.0)

    model_weights_gb = params_billions * bytes_per_param

    # LoRA parameters memory overhead
    # LoRA typically adds < 1-2% parameters
    lora_overhead_gb = (params_billions * 0.01) * 2.0 if lora_r > 0 else 0.0

    # Optimizer state memory
    # QLoRA with paged 8-bit AdamW: optimizer state is only for trainable (LoRA) params
    if lora_r > 0:
        optimizer_gb = lora_overhead_gb * 4.0  # 8-bit / 16-bit optimizer states for LoRA weights
    else:
        # Full fine-tuning with 16-bit AdamW: ~8 to 12 bytes per parameter
        optimizer_gb = params_billions * 8.0

    # Activation memory (roughly proportional to batch_size * seq_len)
    # Gradient checkpointing drastically reduces activation memory by ~4x to 6x
    activation_factor = 0.25 if gradient_checkpointing else 1.0
    base_activation_gb = (batch_size * (seq_len / 2048.0) * (params_billions / 7.0)) * 2.5
    activation_gb = base_activation_gb * activation_factor

    # CUDA context and PyTorch overhead buffer
    cuda_overhead_gb = 1.2

    total_vram_gb = model_weights_gb + lora_overhead_gb + optimizer_gb + activation_gb + cuda_overhead_gb

    # Hardware recommendation
    if total_vram_gb <= 8.0:
        tier = "Consumer Entry (RTX 3060/4060 8GB / Colab Free T4)"
    elif total_vram_gb <= 12.0:
        tier = "Consumer Mid (RTX 3060 12GB / RTX 4070 12GB)"
    elif total_vram_gb <= 16.0:
        tier = "Consumer High (RTX 4080 16GB / T4 16GB)"
    elif total_vram_gb <= 24.0:
        tier = "Workstation / Flagship (RTX 3090/4090 24GB)"
    elif total_vram_gb <= 48.0:
        tier = "Data Center Mid (A40 48GB / A6000 48GB)"
    else:
        tier = "Data Center High (A100 / H100 80GB or Multi-GPU)"

    return {
        "model_parameters_billions": params_billions,
        "precision": precision,
        "batch_size": batch_size,
        "sequence_length": seq_len,
        "lora_rank": lora_r,
        "gradient_checkpointing": gradient_checkpointing,
        "breakdown_gb": {
            "model_weights": round(model_weights_gb, 2),
            "lora_overhead": round(lora_overhead_gb, 2),
            "optimizer_states": round(optimizer_gb, 2),
            "activations": round(activation_gb, 2),
            "cuda_runtime_overhead": round(cuda_overhead_gb, 2)
        },
        "total_estimated_vram_gb": round(total_vram_gb, 2),
        "recommended_gpu_tier": tier
    }

def main():
    parser = argparse.ArgumentParser(description="Estimate GPU VRAM for model training")
    parser.add_argument("--params", type=float, default=7.0, help="Model parameters in billions (e.g. 7.0, 8.0, 14.0)")
    parser.add_argument("--precision", choices=["4bit", "8bit", "16bit", "32bit"], default="4bit", help="Base model precision")
    parser.add_argument("--batch-size", type=int, default=1, help="Per-device batch size")
    parser.add_argument("--seq-len", type=int, default=2048, help="Max sequence length")
    parser.add_argument("--lora-r", type=int, default=16, help="LoRA rank r (0 for full fine-tuning)")
    parser.add_argument("--no-grad-checkpointing", action="store_true", help="Disable gradient checkpointing")
    args = parser.parse_args()

    result = estimate_vram(
        params_billions=args.params,
        precision=args.precision,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        lora_r=args.lora_r,
        gradient_checkpointing=not args.no_grad_checkpointing
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
