import sys
import os
from yt_dlp import YoutubeDL

def download_video(url, audio_only=False, output_dir="downloads"):
    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    }

    if audio_only:
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
    else:
        ydl_opts.update({"format": "best"})

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python simpyou.py download <url> [--audio]")
        sys.exit(1)

    command = sys.argv[1]
    url = sys.argv[2]

    if command == "download":
        audio_only = "--audio" in sys.argv
        download_video(url, audio_only)
    else:
        print("❌ Unknown command.")

if __name__ == "__main__":
    main()
