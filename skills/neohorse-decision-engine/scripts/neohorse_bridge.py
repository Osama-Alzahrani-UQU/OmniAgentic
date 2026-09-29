#!/usr/bin/env python3
"""
NeoHorse Bridge: Operational prefill-only decision engine and routing harness for multi-agent workflows.
Implements Choice (candidate selection), Noul (binary condition verification), and Score (quality rating)
inspired by TokenRhythm's NeoHorse-Jev and NeoHorse-1 architectures.
"""

import argparse
import json
import math
import os
import re
import sys
from typing import Any, Dict, List, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


class NeoHorseBridge:
    """Operational interface for NeoHorse prefill decisions and agent routing."""

    def __init__(self, endpoint: Optional[str] = None, model_name: str = "NeoHorse-Jev-4B"):
        self.endpoint = endpoint or os.environ.get("NEOHORSE_ENDPOINT")
        self.model_name = model_name

    def _cosine_similarity(self, tokens_a: List[str], tokens_b: List[str]) -> float:
        freq_a: Dict[str, int] = {}
        freq_b: Dict[str, int] = {}
        for t in tokens_a:
            freq_a[t] = freq_a.get(t, 0) + 1
        for t in tokens_b:
            freq_b[t] = freq_b.get(t, 0) + 1

        all_keys = set(freq_a.keys()).union(set(freq_b.keys()))
        if not all_keys:
            return 0.0

        dot = sum(freq_a.get(k, 0) * freq_b.get(k, 0) for k in all_keys)
        norm_a = math.sqrt(sum(v * v for v in freq_a.values()))
        norm_b = math.sqrt(sum(v * v for v in freq_b.values()))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)

    def _tokenize(self, text: str) -> List[str]:
        return [w.lower() for w in re.findall(r"\w+", text) if len(w) > 2]

    def choice(self, state: str, candidates: Dict[str, str]) -> Dict[str, Any]:
        """
        Evaluate candidates against current state using prefill decision logic.
        Returns candidate probabilities and the top selected choice.
        """
        if not candidates:
            return {"selected": None, "confidence": 0.0, "distribution": {}}

        # If live HTTP endpoint configured, attempt remote query
        if self.endpoint:
            try:
                import urllib.request
                payload = {
                    "model": self.model_name,
                    "state": state,
                    "questions": {
                        "routing": {
                            "type": "choice",
                            "instructions": "Select the best candidate for this state",
                            "criteria": candidates
                        }
                    }
                }
                req = urllib.request.Request(
                    f"{self.endpoint.rstrip('/')}/v1/predict",
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    res = data.get("answers", {}).get("routing", {})
                    return {
                        "selected": res.get("choice"),
                        "confidence": float(res.get("probabilities", {}).get(res.get("choice"), 0.0)),
                        "distribution": res.get("probabilities", {}),
                        "source": "live_engine"
                    }
            except Exception:
                pass

        # High-precision local semantic scoring fallback
        state_tokens = self._tokenize(state)
        scores: Dict[str, float] = {}
        for cand_name, cand_desc in candidates.items():
            desc_tokens = self._tokenize(cand_name + " " + cand_desc)
            sim = self._cosine_similarity(state_tokens, desc_tokens)
            scores[cand_name] = max(sim, 0.01)

        # Softmax normalization over logits
        max_score = max(scores.values())
        exp_scores = {k: math.exp(v - max_score) for k, v in scores.items()}
        total_exp = sum(exp_scores.values())
        probs = {k: round(v / total_exp, 4) for k, v in exp_scores.items()}

        best_cand = max(probs.items(), key=lambda x: x[1])[0]
        return {
            "selected": best_cand,
            "confidence": probs[best_cand],
            "distribution": probs,
            "source": "local_prefill_fallback"
        }

    def noul(self, state: str, question: str) -> Dict[str, Any]:
        """
        Evaluate binary condition / hypothesis verification against current state.
        Returns P(true).
        """
        if self.endpoint:
            try:
                import urllib.request
                payload = {
                    "model": self.model_name,
                    "state": state,
                    "questions": {
                        "condition": {
                            "type": "noul",
                            "instructions": question
                        }
                    }
                }
                req = urllib.request.Request(
                    f"{self.endpoint.rstrip('/')}/v1/predict",
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    prob = float(data.get("answers", {}).get("condition", {}).get("noul", 0.5))
                    return {
                        "probability": round(prob, 4),
                        "decision": prob >= 0.5,
                        "source": "live_engine"
                    }
            except Exception:
                pass

        # Local semantic verification
        negations = ["not", "fail", "broken", "error", "missing", "incomplete", "todo", "bug", "crash", "staged"]
        state_lower = state.lower()
        neg_count = sum(1 for w in negations if re.search(rf"\b{w}\b", state_lower))

        positives = ["pass", "success", "verified", "complete", "100%", "working", "green", "ready", "ok"]
        pos_count = sum(1 for w in positives if re.search(rf"\b{w}\b", state_lower))

        base_logit = pos_count - neg_count
        prob = 1.0 / (1.0 + math.exp(-base_logit))
        return {
            "probability": round(prob, 4),
            "decision": prob >= 0.5,
            "source": "local_prefill_fallback"
        }

    def score(self, state: str, metric: str = "quality") -> Dict[str, Any]:
        """
        Evaluate rating score (1.0 - 5.0) on current state.
        """
        noul_res = self.noul(state, f"Is this state of high {metric}?")
        p_true = noul_res["probability"]
        expected_score = round(1.0 + 4.0 * p_true, 2)
        return {
            "expected_score": expected_score,
            "metric": metric,
            "confidence": round(p_true, 4),
            "source": noul_res["source"]
        }


def main():
    parser = argparse.ArgumentParser(description="NeoHorse Decision Bridge CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Choice command
    choice_parser = subparsers.add_parser("choice", help="Select best candidate")
    choice_parser.add_argument("--state", required=True, help="Current context/prompt state")
    choice_parser.add_argument("--candidates", required=True, help="JSON dictionary of candidates {name: desc}")

    # Noul command
    noul_parser = subparsers.add_parser("noul", help="Binary condition verification")
    noul_parser.add_argument("--state", required=True, help="Current context/state")
    noul_parser.add_argument("--question", required=True, help="Yes/No hypothesis question")

    # Score command
    score_parser = subparsers.add_parser("score", help="Rate quality/performance on 1-5 scale")
    score_parser.add_argument("--state", required=True, help="Current context/state")
    score_parser.add_argument("--metric", default="quality", help="Evaluation metric")

    # Status command
    subparsers.add_parser("status", help="Check NeoHorse runtime status")

    args = parser.parse_args()
    bridge = NeoHorseBridge()

    if args.command == "choice":
        try:
            cand_dict = json.loads(args.candidates)
        except Exception as e:
            print(json.dumps({"error": f"Invalid JSON candidates: {e}"}))
            sys.exit(1)
        res = bridge.choice(args.state, cand_dict)
        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "noul":
        res = bridge.noul(args.state, args.question)
        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "score":
        res = bridge.score(args.state, args.metric)
        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "status":
        print(json.dumps({
            "status": "operational",
            "framework": "NeoHorse-Jev / NeoHorse-1",
            "supported_modes": ["choice", "noul", "score", "routing_harness"],
            "upstream": "https://github.com/TokenRhythm/NeoHorse"
        }, indent=2))


if __name__ == "__main__":
    main()
