---
name: video-intelligence-pilot
description: Video and audio analysis and multimodal pipelines
---
# Video Intelligence Pilot: Ingestion, Analysis & Execution Protocol

This skill enables agents and sub-agents to ingest video URLs provided by the user, extract transcripts and metadata, analyze technical tutorials or walkthroughs, and execute the user's instructions based on the video's content with 100% fidelity.

---

## 1. Operating Protocol

### 1. Ingestion & Multi-Source Extraction (ط§ط³طھط®ط±ط§ط¬ ط¨ظٹط§ظ†ط§طھ ظˆطھط±ط¬ظ…ط© ط§ظ„ظپظٹط¯ظٹظˆ)
When the user provides a video link:
1. **Identify Platform & Format**:
   - **YouTube**: Standard watch URLs (`youtube.com/watch?v=...`), short URLs (`youtu.be/...`), or Shorts (`youtube.com/shorts/...`).
   - **Direct Video / Other Platforms**: MP4, WebM, Vimeo, Twitter/X, TikTok.
2. **Extract Transcripts / Subtitles**:
   - Run `video_analyzer.py` to fetch official or auto-generated transcripts.
   - Support multilingual captions (Arabic, English, and auto-translated tracks).
3. **Extract Chapters & Metadata**:
   - Parse video title, description, timestamped chapters, and referenced links/repositories.

### 2. Analysis & Intent Mapping (طھظپظƒظٹظƒ ط§ظ„ط´ط±ط­ ظˆط±ط³ظ… ط®ط·ط© ط§ظ„طھظ†ظپظٹط°)
- **Tutorial / How-To Videos**:
  - Identify the tools, libraries, dependencies, and commands demonstrated in the video.
  - Extract code snippets, configuration files, and architectural patterns.
- **Verification & Modernization**:
  - If the video is older (e.g. from 2021) and uses deprecated syntax, modernize the implementation to current stable standards while preserving the tutorial's logic.
- **Direct Execution**:
  - Do NOT merely summarize the video and stop; **EXECUTE** the code or task the user asked for directly into their project workspace.

---

## 2. Video Analyzer Helper Script

Use `video_analyzer.py` to extract transcripts, chapters, and metadata from any video link:

```powershell
python "C:\Users\goldl\.gemini\config\skills\video-intelligence-pilot\scripts\video_analyzer.py" --url "https://www.youtube.com/watch?v=EXAMPLE_ID" --lang ar en
```

Outputs:
- Video title, author, duration, and description.
- Timestamped transcript segments (`[{ "start": 0.0, "duration": 4.5, "text": "..." }]`).
- Extracted code blocks and command candidates.
- Actionable steps list.

---

## 3. References

- [Video Extraction Methods Guide](file:///C:/Users/goldl/.gemini/config/skills/video-intelligence-pilot/references/video_extraction_methods.md): In-depth tools and commands for YouTube API, `yt-dlp`, Whisper, and frame sampling.
- [Tutorial to Code Execution Guide](file:///C:/Users/goldl/.gemini/config/skills/video-intelligence-pilot/references/tutorial_to_code_execution_guide.md): Standard operating procedure for turning tutorial videos into working codebases.
