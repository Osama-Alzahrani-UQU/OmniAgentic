---
name: neohorse-decision-engine
description: Prefill-only decision inference, multi-agent routing harness, and Choice/Noul/Score evaluation using NeoHorse-Jev.
metadata:
  origin: upstream
  author: TokenRhythm
  version: 1.0.0
  upstream: https://github.com/TokenRhythm/NeoHorse
---

# NeoHorse Decision Engine & Routing Harness

The **NeoHorse Decision Engine** leverages TokenRhythm's open-weight **NeoHorse-Jev** and **NeoHorse-1** frameworks to execute structured decisions via **prefill-only inference** without autoregressive generation latency. It provides ultra-fast evaluation for multi-agent workflows, tool selection, condition gating, and recursive self-improvement (RSI) routing harnesses.

---

## 1. Core Decision Modalities

NeoHorse-Jev operates over three distinct decision primitives:

1. **Choice (Which One?)**:
   - Evaluates a set of user-defined candidates (e.g., candidate subagents, routing paths, or tools) against current application state.
   - Returns probability distributions over candidates: `P(candidate_i | state)`.
   - Used for immediate, zero-latency task routing and tool dispatching.

2. **Noul (Is It True?)**:
   - Evaluates binary conditions, hypothesis verification, and completion criteria.
   - Returns a single scalar probability: `P(true | state)`.
   - Used for pre-delivery verification gates, safety filters, and bug detection.

3. **Score (How Good?)**:
   - Evaluates ordered ratings or multi-level quality scores (e.g., 1 to 5 stars, low/medium/high quality).
   - Computes expected score value: `E[score] = sum(p_i * val_i)`.
   - Used for multi-agent output ranking and response arbitration.

---

## 2. Using the CLI Helper (`neohorse_bridge.py`)

The suite includes an operational bridge located at:
`scripts/neohorse_bridge.py`

### Route Tasks to Agents (`choice`)
```bash
python scripts/neohorse_bridge.py choice \
  --state "Fix a NullReferenceException in Unity URP renderer feature" \
  --candidates '{"unity-developer": "Unity C# scripting and engine bugs", "python-reviewer": "Python code reviews", "doc-updater": "Updating documentation"}'
```

### Verify Conditions (`noul`)
```bash
python scripts/neohorse_bridge.py noul \
  --state "All unit tests pass and code compiles with zero warnings" \
  --question "Is the project ready for delivery?"
```

### Score Outputs (`score`)
```bash
python scripts/neohorse_bridge.py score \
  --state "Code has full test coverage, robust typing, and zero stubs" \
  --metric "code_quality"
```

---

## 3. Python Integration

```python
from neohorse_bridge import NeoHorseBridge

bridge = NeoHorseBridge()

# 1. Routing via Choice
route_result = bridge.choice(
    state="Trace memory leak in PyTorch training loop",
    candidates={
        "pytorch-specialist": "PyTorch deep learning and memory optimization",
        "web-developer": "Frontend web development",
        "sql-expert": "Database query optimization"
    }
)
selected_agent = route_result["selected"]
confidence = route_result["confidence"]

# 2. Gate Verification via Noul
gate = bridge.noul(
    state="Repository contains TODO items on lines 45 and 89",
    question="Is the codebase complete without stubs?"
)
if gate["probability"] < 0.8:
    print("Action blocked: Incomplete code detected")
```

---

## 4. Recursive Self-Improvement (RSI) Routing Harness

NeoHorse-1 implements a routing harness that:
- Assigns incoming tasks to a heterogeneous model pool.
- Records trajectory execution steps, tool interactions, and final outcomes.
- Measures capability demand across sub-domains.
- Feeds high-value trajectories into on-policy distillation and routing-guided curriculum SFT for continuous agent enhancement.
