import streamlit as st
from pytube import YouTube

#Input section
st.header("YouTube Downloader App")
link = st.text_input("Paste the YouTube Video Link here")

#Driver section
yt = YouTube(url=link)
st.title(yt.title)
st.image(yt.thumbnail_url)

# st.write(yt.streams.filter(adaptive=True))

video_res = [i.resolution for i in yt.streams.filter(adaptive=True,file_extension='mp4')]
video_res = set(video_res)


st.write(video_res)
# for i in yt.streams.filter(adaptive=True,file_extension='mp4'):
#     st.write(str(i),"\n")

#Downloads section