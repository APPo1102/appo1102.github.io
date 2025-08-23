from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
import translators as ts

#url = "url"
#playlist_url = "YOUR_PLAYLIST_URL_HERE"
url = "https://www.youtube.com/watch?v=y-GlQ8nCBCk"
playlist_url = "https://www.youtube.com/playlist?list=PLefDhv8lUwC8f4goHA3oQc90CK-m9QPPx"

if playlist_url == "":
    yt = YouTube(url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video.download(output_path="D:\影片素材\新手教學\影片",filename=ts.translate_text(yt.title,translator='google',from_language="ko",to_language="zh")+".mp4")

    voice = yt.streams.get_audio_only()
    voice.download(output_path="D:\影片素材\新手教學\聲音",filename=ts.translate_text(yt.title,translator='google',from_language="ko",to_language="zh")+".m4a")
else:
    pl = Playlist(playlist_url)
    for yt in pl.videos:
        try:
            # Print the title of the video

            print(ts.translate_text(yt.title,translator='google',from_language="ko",to_language="zh"))

            # Download the video (optional: specify output_path)
            # ys.download(output_path="path/to/save/videos")            
            video = yt.streams.filter(res="1080p").order_by('resolution').asc().first()
            video.download(output_path="D:\影片素材\新手教學\影片",filename=ts.translate_text(yt.title,translator='google',from_language="ko",to_language="zh")+".mp4")

            voice = yt.streams.get_audio_only()
            voice.download(output_path="D:\影片素材\新手教學\聲音",filename=ts.translate_text(yt.title,translator='google',from_language="ko",to_language="zh")+".m4a")

        except Exception as e:
            print(f"Error processing video: {yt.title} - {e}")