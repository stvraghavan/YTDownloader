import streamlit as st
from pytube import YouTube
from tqdm import tqdm

#Input section
st.header("YouTube Video / Audio  Downloader App")
link = st.text_input("Paste the YouTube Video Link here")



#Driver section
try:
    yt = YouTube(url=link)
    st.title(yt.title)
    st.image(yt.thumbnail_url)

    video_res = set([i.resolution for i in yt.streams.filter(progressive=True,file_extension='mp4')])
    st.write(video_res)
    audio_res = set([i.abr for i in yt.streams.filter(only_audio=True)])
    st.write(audio_res)

    #Downloads section


    #Download function
    def dwl(file_type,quality):
        st.write(file_type)

    st.header("Available download formats")
    st.form:
    
    
    for i in tqdm(video_res):
        try:
            if(st.button(label="Download quality "+i,key = "video")):
                dwl("video",i)
        except:
            pass
    for i in tqdm(audio_res):
        try:
            if(st.button(label="Download quality "+i,key = "video")):
                dwl("audio",i)
        except:
            pass
except:
    pass
