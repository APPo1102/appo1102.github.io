from pytube import YouTube

url = "YouTube影片網址"
try:
    yt = YouTube(url)
    # 選擇要下載的影片流 (例如，選擇最高畫質的 mp4)
    stream = yt.streams.get_highest_resolution()
    # 下載影片
    stream.download()
    print("下載完成！")
except Exception as e:
    print(f"下載失敗: {e}")