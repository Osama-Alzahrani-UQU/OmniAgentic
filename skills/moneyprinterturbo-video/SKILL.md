---
name: moneyprinterturbo-video
description: Generate automated short-form videos, reels, and voice-over content from prompts, scripts, and footage using MoneyPrinterTurbo.
compatibility: Requires an AI agent with terminal, network, filesystem, and long-running command support. Supports macOS and Windows and uses uv exclusively.
metadata:
  origin: upstream
  author: harry0703@hotmail.com
  version: 1.3.2
  upstream: https://github.com/harry0703/MoneyPrinterTurbo
---

# MoneyPrinterTurbo Video Generation

The user only needs to provide a video topic or script. Complete installation, configuration reuse, generation, waiting, and final MP4 delivery automatically. Do not stop after giving instructions or commands.

## Required Behavior

1. Ask the user only for required API credentials that are missing, rejected, or unusable. Combine all required credentials into one request.
2. Do not ask for confirmation before installing, generating, waiting, using defaults, or returning the result.
3. Do not create or repeatedly update a detailed plan for a standard generation request. Send one short progress update and execute.
4. Run the helper as one foreground command with a timeout of at least 20 minutes.
5. Never poll with `sleep`, `echo`, `ps`, repeated `ls`, or repeated `tail`. If the terminal returns a resumable session ID, continue waiting on that same session.
6. Do not read the full log after success. Read only the short reported error or the relevant log tail after failure.
7. Never print API keys, tokens, the full `config.toml`, or credential-bearing configuration fragments.

## Defaults

Unless the user requests otherwise, generate one `9:16` portrait video with stock footage, default Edge TTS voice, subtitles, and background music. MoneyPrinterTurbo is installed at `C:\Users\goldl\MoneyPrinterTurbo`.

## Execution

### 1. Locate the helper

Resolve `SKILL_DIR` from this `SKILL.md` file. The helper is the adjacent `mpt_agent.py`. Set the terminal tool's working directory to `SKILL_DIR` and invoke the helper by its relative filename.

### 2. Run the helper

Use this command with `workdir=SKILL_DIR`:

```bash
uv run --no-project --python 3.11 python mpt_agent.py --subject "<video topic>"
```

Or invoke the global CLI:

```bash
mpt cli --video-subject "<video topic>" --video-aspect 9:16
```

WebUI is accessible via:

```bash
mpt
```

## Exit Handling

### Exit code 0: deliver the result

Successful output has this form:

```text
MPT_RESULT
VIDEO_FILE=<absolute path>/final-1.mp4
TASK_DIR=<absolute path>/storage/tasks/<task_id>
LOG_FILE=<absolute path>/run-<task_id>.log
RESULT_FILE=<absolute path>/latest-result.json
```

`mpt_agent.py` emits `VIDEO_FILE` only after confirming that the file exists and is non-empty. Return the absolute video path and a concise description.

### Exit code 10: request credentials once

If API keys are needed, ask the user only for the required keys.

```text
MPT_LLM_PROVIDER
MPT_LLM_API_KEY
MPT_PEXELS_API_KEY
```

### Exit code 1: repair or report

Use `MPT_ERROR` and `LOG_FILE` to repair a recoverable problem and retry once.
