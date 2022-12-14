import streamlit as st
from pytube import YouTube

#Input section
st.header("YouTube Downloader App")
link = st.text_input("Paste the YouTube Video Link here")

#Driver section
yt = YouTube(url=link)
st.title(yt.title)
st.image(yt.thumbnail_url)

video_res = [i.resolution for i in yt.streams.filter(adaptive=True,file_extension='mp4')]
video_res = set(video_res)

# video_fps = [i.fps for i in yt.streams.filter(adaptive=True,file_extension='mp4')]
# video_fps = set(video_fps)
# st.write(video_fps)

#Downloads section

#Download function
def Download(url, args):
    yt = YouTube(url)

    target = yt.streams.filter(adaptive=True).get_by_resolution(args)
    target.download()
#Download buttons
for i in video_res:
    try:
        st.download_button(label="Download quality "+i,on_click=Download(link,i))
    except:
        pass

