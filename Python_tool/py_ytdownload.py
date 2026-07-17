from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
import translators as ts

#url = "url"
#playlist_url = "YOUR_PLAYLIST_URL_HERE"
url = "https://www.youtube.com/watch?v=js2syT4l9lc"
playlist_url = ""

if playlist_url == "":
    yt = YouTube(url, on_progress_callback=on_progress)
    #video = yt.streams.get_highest_resolution()
    video = yt.streams.filter(res="1080p").order_by('resolution').asc().first()
    video.download(output_path="F:\影片素材\影片",filename=yt.title+".mp4")

    voice = yt.streams.get_audio_only()
    voice.download(output_path="F:\影片素材\聲音",filename=yt.title+".m4a")
else:
    pl = Playlist(playlist_url)
    for yt in pl.videos:
        try:
            # Print the title of the video

            print(yt.title)

            # Download the video (optional: specify output_path)
            # ys.download(output_path="path/to/save/videos")            
            video = yt.streams.filter(res="1080p").order_by('resolution').asc().first()
            video.download(output_path="F:\影片素材\影片",filename=yt.title+".mp4")

            voice = yt.streams.get_audio_only()
            voice.download(output_path="F:\影片素材\聲音",filename=yt.title+".m4a")

        except Exception as e:
            print(f"Error processing video: {yt.title} - {e}")