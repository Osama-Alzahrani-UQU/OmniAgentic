---
name: omniroute-gateway
description: OmniRoute AI gateway for 350+ providers
metadata:
  origin: upstream
  author: Diego Souza
  version: 3.8.50
  upstream: https://github.com/diegosouzapw/OmniRoute
---

# OmniRoute: The Unified AI Gateway & Free Tier Router

**OmniRoute** is an open-source, self-hosted AI gateway that aggregates **350+ AI providers** and **1,300+ models** behind a single OpenAI-compatible endpoint. It provides quota-aware auto-fallback across 150+ free tiers (~1.62B tokens/month) and features stacked **RTK + Caveman prompt compression** saving 15% to 95% of tokens.

---

## 1. Quick Start & Execution

### Option A: Via NPX (Node.js)
```bash
npx --yes omniroute
```

### Option B: Via Docker
```bash
docker run -d -p 20128:20128 --name omniroute diegosouzapw/omniroute
```

### Dashboard & API Access
- **Web Dashboard**: `http://localhost:20128`
- **OpenAI Compatible Endpoint**: `http://localhost:20128/v1`
- **Models Endpoint**: `http://localhost:20128/v1/models`

---

## 2. Platform Integrations

### Antigravity & OpenAI Codex CLI
In `~/.codex/config.toml`:
```toml
[model_providers.omniroute]
base_url = "http://127.0.0.1:20128/v1"
api_key = "sk-omniroute-local"
models = ["openai/gpt-5.4", "deepseek/deepseek-v3", "glm/glm-5.2", "qwen/qwen-2.5-72b"]
```

### Claude Desktop & Claude Code
Launch directly through OmniRoute:
```bash
omniroute run claude --model openai/gpt-5.4
omniroute run codex  --model glm/glm-5.2
```

Or configure via interactive wizard:
```bash
omniroute configure claude
omniroute configure codex
omniroute configure antigravity
```

---

## 3. Quota-Aware Auto-Fallback Cascade

OmniRoute monitors provider rate limits (429) and server outages (5xx), seamlessly routing incoming agent requests across prioritized tiers:

1. **Tier 1 (Fast Free Tiers)**: Groq (Llama 3.3 70B), Cerebras, Mistral Free API.
2. **Tier 2 (High-Capacity Community Pools)**: DeepSeek-V3, Qwen 2.5 72B, Kimi/Moonshot.
3. **Tier 3 (Premium / Flagship Fallback)**: Claude 3.7 Sonnet, OpenAI GPT-5.4, Gemini 2.5 Pro.

---

## 4. Using the CLI Helper (`omniroute_bridge.py`)

The suite includes an operational bridge located at:
`scripts/omniroute_bridge.py`

### Check Gateway Health
```bash
python scripts/omniroute_bridge.py status
```

### Generate Platform Configs
```bash
# Generate Codex config snippet
python scripts/omniroute_bridge.py config --target codex

# Generate Claude Code config snippet
python scripts/omniroute_bridge.py config --target claude
```

### Simulate RTK Prompt Compression
```bash
python scripts/omniroute_bridge.py compress --prompt "Please analyze this large file and extract all functions..."
```
