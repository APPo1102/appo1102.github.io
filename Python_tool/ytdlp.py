# -*- coding: utf-8 -*-
"""
YouTube 影片 / 音訊分離下載工具 (yt-dlp 版)

安裝:
    pip install -U yt-dlp

行為與原本的 pytubefix 版一致:
    影像(無聲, 1080p mp4) -> VIDEO_DIR
    音訊(m4a)             -> AUDIO_DIR
兩者檔名同為影片標題。

playlist 由 yt-dlp 自己處理, 單支失敗會跳過並繼續 (ignoreerrors)。
"""

import os
import sys

from yt_dlp import YoutubeDL

# ---------------- 設定 ----------------
VIDEO_DIR = r"F:\影片素材\影片"
AUDIO_DIR = r"F:\影片素材\聲音"

URL = "https://www.youtube.com/watch?v=eE9W6FotFKo"
PLAYLIST_URL = ""

MAX_HEIGHT = 1080          # 影像最高解析度

# 記錄已下載的影片 id, 重跑時自動跳過。不需要就設成 None
ARCHIVE_FILE = os.path.join(VIDEO_DIR, ".downloaded.txt")

# 遇到 "Sign in to confirm you're not a bot" 時, 從瀏覽器帶 cookie。
# 例如 "chrome" / "edge" / "firefox"; 不需要就留 None。
# 注意: Chrome 必須完全關閉, yt-dlp 才讀得到 cookie 資料庫。
COOKIES_FROM_BROWSER = None
# --------------------------------------


def base_opts(target_dir: str) -> dict:
    os.makedirs(target_dir, exist_ok=True)
    opts = {
        "paths": {"home": target_dir},
        "outtmpl": "%(title)s.%(ext)s",
        "windowsfilenames": True,      # 自動處理 \ / : * ? " < > | 等非法字元
        "trim_file_name": 120,
        "noplaylist": not bool(PLAYLIST_URL),
        "ignoreerrors": bool(PLAYLIST_URL),
        "continuedl": True,            # 支援斷點續傳
        "retries": 10,
        "fragment_retries": 10,
        "concurrent_fragment_downloads": 4,
        "quiet": False,
        "no_warnings": False,
        "consoletitle": False,
    }
    if ARCHIVE_FILE:
        opts["download_archive"] = ARCHIVE_FILE
    if COOKIES_FROM_BROWSER:
        opts["cookiesfrombrowser"] = (COOKIES_FROM_BROWSER,)
    return opts


def video_opts() -> dict:
    opts = base_opts(VIDEO_DIR)
    # bv* = 純影像軌(無聲)。優先 mp4/h264, 退而求其次任何容器。
    opts["format"] = (
        f"bv*[height<={MAX_HEIGHT}][ext=mp4]"
        f"/bv*[height<={MAX_HEIGHT}]"
        f"/bv*"
    )
    if ARCHIVE_FILE:
        # 影像與音訊各自記錄, 避免下完影像就把音訊當作已下載
        opts["download_archive"] = ARCHIVE_FILE.replace(".txt", "_video.txt")
    return opts


def audio_opts() -> dict:
    opts = base_opts(AUDIO_DIR)
    opts["format"] = "ba[ext=m4a]/ba"
    if ARCHIVE_FILE:
        opts["download_archive"] = os.path.join(AUDIO_DIR, ".downloaded_audio.txt")
    return opts


def download(url: str) -> int:
    print(f"=== 影像 -> {VIDEO_DIR}")
    with YoutubeDL(video_opts()) as ydl:
        rc_v = ydl.download([url])

    print(f"\n=== 音訊 -> {AUDIO_DIR}")
    with YoutubeDL(audio_opts()) as ydl:
        rc_a = ydl.download([url])

    return rc_v or rc_a


def main() -> None:
    target = PLAYLIST_URL or URL
    if not target:
        print("請先設定 URL 或 PLAYLIST_URL", file=sys.stderr)
        sys.exit(1)

    rc = download(target)
    print("\n完成" if rc == 0 else f"\n結束, 但有項目失敗 (code={rc})")
    sys.exit(rc)


if __name__ == "__main__":
    main()