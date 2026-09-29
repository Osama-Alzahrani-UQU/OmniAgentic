---
name: ai-model-trainer
description: Training and fine-tuning AI models (LLMs, VLMs
---
# AI Model Training & Fine-Tuning Protocol

You are equipped with the **AI Model Trainer** protocol. As an agent or sub-agent, you have specialized capabilities in designing, executing, debugging, and evaluating model training pipelines across LLMs, VLMs, and specialized AI architectures.

---

## 5-Phase Model Training Lifecycle

### Phase 1: Resource & Hardware Budgeting
Before writing or running training code:
1. Run `estimate_vram.py` to calculate memory footprint:
   ```powershell
   python C:/Users/goldl/.gemini/config/skills/ai-model-trainer/scripts/estimate_vram.py --params 8 --precision 4bit --batch-size 1 --seq-len 2048 --lora-r 16
   ```
2. Choose the appropriate training regime based on available GPU VRAM:
   - **VRAM < 12 GB**: Must use **QLoRA (4-bit)** + Gradient Checkpointing + Batch Size 1 + Gradient Accumulation.
   - **VRAM 16 - 24 GB**: Can use **LoRA (16-bit)** for small models (up to 7B/8B) or **QLoRA** for 14B models.
   - **Multi-GPU / Cloud**: Use DeepSpeed ZeRO-2/3 or FSDP for full fine-tuning or 70B models.

### Phase 2: Hyperparameter Selection
Consult [hyperparameter_cheatsheet.md](./references/hyperparameter_cheatsheet.md):
- **Learning Rate**:
  - Full fine-tuning: `1e-5` to `5e-5`
  - LoRA (16-bit): `1e-4` to `3e-4`
  - QLoRA (4-bit): `2e-4` to `5e-4`
- **Scheduler**: `cosine` with `warmup_ratio=0.03` to `0.05`.
- **Optimizer**: `paged_adamw_8bit` (for memory savings) or `adamw_torch_fused`.
- **Target Modules**: For LLMs/VLMs, target all linear layers (`q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`) to maximize learning capacity without full fine-tuning cost.

### Phase 3: Dataset Hygiene & Formatting
- Ensure proper tokenization and chat template alignment (`tokenizer.apply_chat_template`).
- Mask prompt/instruction tokens in loss computation (`DataCollatorForCompletionOnlyLM` or setting prompt labels to `-100`) so the model only learns to predict the completion, not re-memorize instructions.
- Shuffle training data, set a fixed seed (e.g. `seed=42`), and hold out 5â€“10% for validation.

### Phase 4: Training Diagnostics & Self-Healing
During and after training, monitor loss using `loss_diagnostics.py`:
```powershell
python C:/Users/goldl/.gemini/config/skills/ai-model-trainer/scripts/loss_diagnostics.py --log-file ./training_logs.json
```
- **OOM Error**: Reduce `per_device_train_batch_size`, increase `gradient_accumulation_steps`, lower `max_seq_length`, or enable `gradient_checkpointing=True`.
- **Loss = NaN / Inf**: Lower learning rate by 2x, switch from `fp16` to `bf16`, or check for corrupted zero-length inputs.
- **Loss Spikes**: Increase warmup steps or check dataset for outliers/bad tokens.
- Consult [troubleshooting_training.md](./references/troubleshooting_training.md) for detailed remedies.

### Phase 5: Evaluation & Export
- Never consider training complete without evaluating on held-out validation data.
- Merge LoRA adapter (`model.merge_and_unload()`) if deploying for high-throughput inference (vLLM, Ollama, GGUF).
- Export tokenizer and chat template configuration alongside model weights.
