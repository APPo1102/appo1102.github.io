# -*- coding: utf-8 -*-
"""
YouTube 影片 / 音訊分離下載工具 (pytubefix)

需求: pytubefix >= 10.11.0   ->   pip install -U pytubefix
      該版本會自帶 nodejs-wheel-binaries, client='WEB' 時自動產生 poToken。

修正重點:
1. 只使用「能真正下載」的 client:
   - WEB (自動 poToken) 優先
   - 其餘用 require_po_token=False 的 client (ANDROID_VR / TV / MEDIA_CONNECT ...)
   - 不用 MWEB、ANDROID、IOS: 這些需要 poToken, 拿得到標題但下載會 403
2. 選定 client 後先對串流網址做 Range 探測, 確認不是 403 才開始下載
3. Windows 路徑 raw string、檔名去非法字元
4. 1080p 為 adaptive stream(無聲), 明確取 mp4 純影像軌 + fallback
"""

import os
import re
import sys
import urllib.error
import urllib.request

from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

# ---------------- 設定 ----------------
VIDEO_DIR = r"F:\影片素材\影片"
AUDIO_DIR = r"F:\影片素材\聲音"

URL = "https://www.youtube.com/watch?v=XDy_bL1VhMM"
PLAYLIST_URL = ""

TARGET_RES = "1080p"

# 依序嘗試。WEB 需要 pytubefix >= 10.11 才會自動產生 poToken。
CLIENTS = ["WEB", "ANDROID_VR", "TV", "TV_EMBED", "MEDIA_CONNECT", "WEB_CREATOR"]

# 上述全失敗時, 是否改用手動 poToken (會提示貼上 visitorData / poToken)
USE_MANUAL_PO_TOKEN = True
# 再失敗時, 是否用 OAuth 登入 (會出現裝置授權碼; 有帳號風險)
USE_OAUTH_FALLBACK = False
# --------------------------------------


def safe_filename(name: str, max_len: int = 120) -> str:
    """移除 Windows 檔名非法字元。"""
    name = re.sub(r'[\\/:*?"<>|\r\n\t]', "_", name)
    name = re.sub(r"\s+", " ", name).strip().rstrip(". ")
    return name[:max_len] or "video"


def url_is_playable(url: str) -> bool:
    """對串流網址要 2 bytes, 確認不是 403 / 410。"""
    req = urllib.request.Request(url, headers={"Range": "bytes=0-1"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status in (200, 206)
    except urllib.error.HTTPError as e:
        print(f"       串流網址探測失敗: HTTP {e.code}")
        return False
    except Exception as e:
        print(f"       串流網址探測失敗: {type(e).__name__}: {e}")
        return False


def pick_video_stream(yt: YouTube):
    """優先取指定解析度的 mp4 純影像串流, 取不到就退而求其次。"""
    s = yt.streams.filter(res=TARGET_RES, mime_type="video/mp4",
                          only_video=True).first()
    if s:
        return s
    s = (yt.streams.filter(mime_type="video/mp4", only_video=True)
         .order_by("resolution").desc().first())
    if s:
        print(f"       找不到 {TARGET_RES}, 改用 {s.resolution}")
        return s
    print("       沒有 adaptive 影像軌, 改用 progressive 最高畫質")
    return yt.streams.get_highest_resolution()


def try_client(url: str, **kwargs):
    """
    建立 YouTube 物件並挑好影音串流, 全部驗證通過才回傳。
    回傳 (yt, video_stream, audio_stream) 或 None。
    """
    yt = YouTube(url, on_progress_callback=on_progress, **kwargs)
    _ = yt.streams                      # 觸發 check_availability()

    video = pick_video_stream(yt)
    audio = yt.streams.get_audio_only()
    if video is None or audio is None:
        raise RuntimeError("找不到影像或音訊串流")

    if not url_is_playable(video.url):
        raise RuntimeError("影像串流網址無法存取 (多半是缺 poToken)")
    if not url_is_playable(audio.url):
        raise RuntimeError("音訊串流網址無法存取 (多半是缺 poToken)")

    return yt, video, audio


def resolve(url: str):
    last_err = None

    for client in CLIENTS:
        try:
            print(f"[..]   client={client}")
            result = try_client(url, client=client)
            print(f"[OK]   client={client}")
            return result
        except Exception as e:
            last_err = e
            print(f"[FAIL] client={client}: {type(e).__name__}: {e}")

    if USE_MANUAL_PO_TOKEN:
        try:
            print("[..]   WEB + 手動 poToken (依提示貼上 visitorData / poToken)")
            result = try_client(url, client="WEB", use_po_token=True)
            print("[OK]   WEB + 手動 poToken")
            return result
        except Exception as e:
            last_err = e
            print(f"[FAIL] WEB + poToken: {type(e).__name__}: {e}")

    if USE_OAUTH_FALLBACK:
        try:
            print("[..]   OAuth 登入")
            result = try_client(url, use_oauth=True, allow_oauth_cache=True)
            print("[OK]   OAuth")
            return result
        except Exception as e:
            last_err = e
            print(f"[FAIL] OAuth: {type(e).__name__}: {e}")

    raise RuntimeError(f"所有方式都無法取得可下載的串流, 最後錯誤: {last_err}")


def download_one(url: str) -> None:
    yt, video, audio = resolve(url)
    title = safe_filename(yt.title)
    print(f"標題: {yt.title}")

    os.makedirs(VIDEO_DIR, exist_ok=True)
    os.makedirs(AUDIO_DIR, exist_ok=True)

    print(f"影像: {video.resolution} / {video.mime_type}")
    video.download(output_path=VIDEO_DIR, filename=f"{title}.mp4",
                   skip_existing=True)

    print(f"音訊: {audio.abr} / {audio.mime_type}")
    audio.download(output_path=AUDIO_DIR, filename=f"{title}.m4a",
                   skip_existing=True)

    print("完成\n")


def main() -> None:
    if not PLAYLIST_URL:
        download_one(URL)
        return

    pl = Playlist(PLAYLIST_URL)
    print(f"播放清單: {pl.title}")
    for video_url in pl.video_urls:
        try:
            download_one(video_url)
        except Exception as e:
            print(f"[ERROR] {video_url} -> {type(e).__name__}: {e}\n",
                  file=sys.stderr)


if __name__ == "__main__":
    main()