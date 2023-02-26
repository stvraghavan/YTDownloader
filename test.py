from pytube import YouTube

link = "https://youtu.be/MMuAqR_MjS8"
dwnpath = 'C:/Users/Tilak Vijayaraghavan/Downloads'

yt = YouTube(url=link)

video_res = [i.resolution for i in yt.streams.filter(file_extension='mp4')]
# video_fps = [i.fps for i in yt.streams.filter(file_extension='mp4')]

print(yt.streams.order_by("FramesPerSecond"))