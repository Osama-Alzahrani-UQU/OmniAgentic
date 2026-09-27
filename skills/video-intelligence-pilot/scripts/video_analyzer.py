"""
Video Intelligence Analyzer & Transcript Extractor.
Extracts:
1. Video metadata (Title, Author, Description) via oEmbed / web parsing.
2. Subtitles & Transcripts (Arabic, English, Auto-generated).
3. Code blocks, commands, and actionable steps mentioned in the video.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.parse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

def extract_youtube_id(url):
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
        r"youtube\.com\/shorts\/([0-9A-Za-z_-]{11})",
        r"youtube\.com\/embed\/([0-9A-Za-z_-]{11})"
    ]
    for p in patterns:
        match = re.search(p, url)
        if match:
            return match.group(1)
    return None

def fetch_oembed_metadata(url):
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={urllib.parse.quote(url)}&format=json"
        req = urllib.request.Request(oembed_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                return {
                    "title": data.get("title", ""),
                    "author_name": data.get("author_name", ""),
                    "author_url": data.get("author_url", ""),
                    "thumbnail_url": data.get("thumbnail_url", "")
                }
    except Exception:
        pass
    return {}

def fetch_transcript_api(video_id, languages=["ar", "en"]):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        
        # Try direct fetch with requested languages
        try:
            transcript = api.fetch(video_id, languages=languages)
            return [{"start": getattr(s, 'start', 0.0), "duration": getattr(s, 'duration', 0.0), "text": getattr(s, 'text', str(s))} for s in transcript], "success"
        except Exception:
            pass

        # Try listing transcripts
        try:
            transcript_list = api.list(video_id)
            for t in transcript_list:
                fetched = t.fetch()
                return [{"start": getattr(s, 'start', 0.0), "duration": getattr(s, 'duration', 0.0), "text": getattr(s, 'text', str(s))} for s in fetched], getattr(t, 'language_code', 'auto')
        except Exception as e:
            return None, str(e)
    except ImportError:
        return None, "youtube_transcript_api_not_installed"
    except Exception as e:
        return None, str(e)
    return None, "no_transcript_found"


def extract_code_and_commands(text):
    commands = []
    # Match CLI commands
    cli_patterns = [
        r"(?:^|\s)(npm\s+[^\n]+)",
        r"(?:^|\s)(pip\s+[^\n]+)",
        r"(?:^|\s)(git\s+[^\n]+)",
        r"(?:^|\s)(cargo\s+[^\n]+)",
        r"(?:^|\s)(docker\s+[^\n]+)",
        r"(?:^|\s)(python\s+[^\n]+)",
        r"(?:^|\s)(npx\s+[^\n]+)"
    ]
    for cp in cli_patterns:
        matches = re.findall(cp, text)
        for m in matches:
            clean_m = m.strip().strip(";\"'")
            if clean_m and clean_m not in commands:
                commands.append(clean_m)
    return commands

def analyze_video(url, languages=["ar", "en"]):
    video_id = extract_youtube_id(url)
    metadata = fetch_oembed_metadata(url)
    
    transcript_data = None
    transcript_status = "unsupported_or_non_youtube"
    
    if video_id:
        transcript_data, transcript_status = fetch_transcript_api(video_id, languages)
    
    full_transcript_text = ""
    if transcript_data and isinstance(transcript_data, list):
        full_transcript_text = " ".join(t.get("text", "") for t in transcript_data)
        
    extracted_commands = extract_code_and_commands(full_transcript_text + " " + metadata.get("title", ""))

    return {
        "status": "SUCCESS",
        "url": url,
        "video_id": video_id,
        "metadata": metadata,
        "transcript_available": bool(transcript_data),
        "transcript_status": transcript_status,
        "transcript_segments_count": len(transcript_data) if transcript_data else 0,
        "full_text_preview": full_transcript_text[:500] if full_transcript_text else "",
        "detected_commands": extracted_commands,
        "actionable_instructions": [
            "Use transcript and metadata to implement user's requested features.",
            "Verify dependencies and code snippets before executing in project."
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze video URLs and extract transcripts/metadata.")
    parser.add_argument("--url", required=True, help="Video URL to analyze (YouTube, etc.)")
    parser.add_argument("--lang", nargs="+", default=["ar", "en"], help="Preferred transcript languages")
    parser.add_argument("--out", help="Output JSON file path (optional)")
    
    args = parser.parse_args()
    
    result = analyze_video(args.url, args.lang)
    output_json = json.dumps(result, indent=2, ensure_ascii=False)
    
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output_json)
            
    print(output_json)

if __name__ == "__main__":
    main()
