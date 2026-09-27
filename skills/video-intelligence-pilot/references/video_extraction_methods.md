# Video Extraction & Ingestion Methods Guide

This reference details the tools, APIs, and techniques for extracting transcripts, metadata, audio, and visual frames from online video platforms.

---

## 1. YouTube Extraction Architecture

### A. Subtitle & Transcript APIs
1. **`youtube-transcript-api` (Python)**:
   - Fetches official and auto-generated transcripts without requiring a YouTube Data API v3 key or browser automation.
   - Supports Arabic (`ar`), English (`en`), and auto-translated tracks (`tlang`).
2. **`yt-dlp` CLI**:
   - Universal media extractor supporting YouTube and 1000+ streaming sites.
   - Command to download subtitles without downloading video:
     ```cmd
     yt-dlp --skip-download --write-auto-sub --sub-lang "ar,en" --sub-format vtt -o "transcript" "<VIDEO_URL>"
     ```

---

## 2. Direct Video & Other Platforms (Vimeo, Twitter, MP4)

When a video does not have native subtitles:
1. **Audio Extraction via `ffmpeg`**:
   ```cmd
   ffmpeg -i "input_video.mp4" -vn -ar 16000 -ac 1 -c:a pcm_s16le "audio.wav"
   ```
2. **Local Speech-to-Text (Whisper / Faster-Whisper)**:
   - Transcribe audio locally using OpenAI Whisper:
     ```python
     import whisper
     model = whisper.load_model("base")
     result = model.transcribe("audio.wav")
     print(result["text"])
     ```

---

## 3. Keyframe Extraction for Visual Inspection

If a video tutorial demonstrates a UI layout or configuration setting that is not spoken in the audio:
- Extract 1 frame every 10 seconds:
  ```cmd
  ffmpeg -i "input_video.mp4" -vf "fps=1/10" "frames/frame_%04d.png"
  ```
- Inspect specific frames using image analysis tools.
