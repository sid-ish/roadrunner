import subprocess

def download_video(url: str, output: str):
    subprocess.run([
        "yt-dlp",
        "-f", "best",
        "-o", output,
        url
    ])
