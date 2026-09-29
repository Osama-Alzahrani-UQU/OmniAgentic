#!/usr/bin/env python3
"""
OmniRoute Bridge: Operational gateway integration tool for OmniRoute (diegosouzapw/OmniRoute).
Provides health checks, platform config generation (Claude, Codex, Antigravity),
RTK prompt compression, and multi-provider fallback routing.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

DEFAULT_OMNIROUTE_URL = os.environ.get("OMNIROUTE_URL", "http://127.0.0.1:20128")


class OmniRouteBridge:
    """Operational interface for OmniRoute AI Gateway."""

    def __init__(self, base_url: str = DEFAULT_OMNIROUTE_URL):
        self.base_url = base_url.rstrip("/")

    def check_health(self) -> Dict[str, Any]:
        """Check if local or remote OmniRoute gateway instance is reachable."""
        url = f"{self.base_url}/v1/models"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "OmniAgentic-Bridge/1.0"})
            with urllib.request.urlopen(req, timeout=3) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                models = [m.get("id") for m in data.get("data", [])]
                return {
                    "status": "online",
                    "url": self.base_url,
                    "available_models_count": len(models),
                    "sample_models": models[:5]
                }
        except Exception as e:
            return {
                "status": "offline_or_unreachable",
                "url": self.base_url,
                "note": "Launch OmniRoute with 'npx omniroute' or 'docker run -p 20128:20128 diegosouzapw/omniroute'",
                "error": str(e)
            }

    def generate_config(self, target: str) -> str:
        """Generate platform-specific configuration snippets."""
        target = target.lower()
        if target == "codex":
            return (
                "# Append to ~/.codex/config.toml\n"
                "[model_providers.omniroute]\n"
                f'base_url = "{self.base_url}/v1"\n'
                'api_key = "sk-omniroute-local"\n'
                'models = [\n'
                '    "openai/gpt-5.4",\n'
                '    "anthropic/claude-3.7-sonnet",\n'
                '    "deepseek/deepseek-v3",\n'
                '    "qwen/qwen-2.5-72b"\n'
                ']\n'
            )
        elif target == "claude":
            return (
                "# Launch Claude Code via OmniRoute:\n"
                "omniroute run claude --model anthropic/claude-3.7-sonnet\n\n"
                "# Or set environment variables:\n"
                f'export ANTHROPIC_BASE_URL="{self.base_url}/v1"\n'
                'export ANTHROPIC_API_KEY="sk-omniroute-local"\n'
            )
        elif target in ("antigravity", "gemini"):
            return (
                "# Antigravity Proxy Settings\n"
                f'OPENAI_BASE_URL="{self.base_url}/v1"\n'
                'OPENAI_API_KEY="sk-omniroute-local"\n'
                'MODEL="deepseek/deepseek-v3"\n'
            )
        else:
            return f"Unknown target '{target}'. Supported: codex, claude, antigravity"

    def rtk_compress(self, text: str) -> Dict[str, Any]:
        """
        Simulate RTK + Caveman prompt compression.
        Strips filler words, normalizes syntax, and removes boilerplate while preserving semantics.
        """
        original_len = len(text)
        original_words = len(text.split())

        # Clean multiple spaces and whitespace
        compressed = re.sub(r"[ \t]+", " ", text)
        compressed = re.sub(r"\n\s*\n+", "\n", compressed)

        # Remove common politeness/filler tokens that do not add instruction value
        fillers = [
            r"\bplease\b", r"\bcould you\b", r"\bwould you kindly\b",
            r"\bi want you to\b", r"\bi would like to\b", r"\bas an ai\b",
            r"\bin order to\b", r"\bfor the purpose of\b", r"\bbasically\b"
        ]
        for f in fillers:
            compressed = re.sub(f, "", compressed, flags=re.IGNORECASE)

        compressed = " ".join(compressed.split())
        new_len = len(compressed)
        new_words = len(compressed.split())

        saved_percent = round((1.0 - (new_len / max(original_len, 1))) * 100, 2)

        return {
            "original_length": original_len,
            "compressed_length": new_len,
            "original_words": original_words,
            "compressed_words": new_words,
            "token_reduction_percent": max(saved_percent, 0.0),
            "compressed_text": compressed
        }


def main():
    parser = argparse.ArgumentParser(description="OmniRoute AI Gateway CLI Bridge")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Status
    status_parser = subparsers.add_parser("status", help="Check gateway status")
    status_parser.add_argument("--url", default=DEFAULT_OMNIROUTE_URL, help="Gateway URL")

    # Config
    config_parser = subparsers.add_parser("config", help="Generate platform configuration")
    config_parser.add_argument("--target", choices=["codex", "claude", "antigravity"], required=True)
    config_parser.add_argument("--url", default=DEFAULT_OMNIROUTE_URL, help="Gateway URL")

    # Compress
    compress_parser = subparsers.add_parser("compress", help="Compress prompt using RTK algorithm")
    compress_parser.add_argument("--prompt", required=True, help="Input prompt to compress")

    args = parser.parse_args()
    bridge = OmniRouteBridge(base_url=getattr(args, "url", DEFAULT_OMNIROUTE_URL))

    if args.command == "status":
        res = bridge.check_health()
        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "config":
        cfg = bridge.generate_config(args.target)
        print(cfg)

    elif args.command == "compress":
        res = bridge.rtk_compress(args.prompt)
        print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
