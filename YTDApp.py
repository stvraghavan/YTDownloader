import streamlit as st
from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm

#Input section
st.header("YouTube Video / Audio  Downloader App")



#Driver section
# dwnpath = st.text_input("Enter the download path / folder from t")

tab1, tab2 = st.tabs(['Video','Playlist'])
with tab1:
    try:
        link = st.text_input("Paste the YouTube Video Link here")
        yt = YouTube(url=link)
        st.title(yt.title)
        st.image(yt.thumbnail_url)
        video_res = yt.streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc()
        video_res = [i.resolution for i in video_res]
        audio_res = yt.streams.filter(only_audio=True).order_by('abr').desc()
        audio_res = [i.abr for i in audio_res]
        # st.write(audio_res+video_res)
        # video_fps = [i.fps for i in yt.streams.filter(adaptive=True,file_extension='mp4')]
        # video_fps = set(video_fps)
        # st.write(video_fps)

        #Downloads section
    
        option = st.selectbox("Select the Download type :",options=video_res+audio_res,help="Select the download format")

        if st.button("Download"):
            video_object = YouTube(link)
            if option in (video_res):
                video_object.streams.filter(resolution=option,progressive=True,file_extension="mp4").first().download()
            if option in (audio_res):
                video_object.streams.filter(abr=option,only_audio=True).first().download()
        if st.button("View"):
            st.video(link)
        #Download buttons
        # col1,col2 = st.columns(2)
        # with col1:
        #     st.header("Video Quality")
        #     for i in video_res:
        #         # st.write(i)
        #         if st.button("Download "+i.resolution):
        #             # st.write("It worked, sorta")
        #             try:
        #                 yt = YouTube(link)
        #                 yt.streams.filter(res=i,progressive=True,file_extension="mp4").first().download(output_path=dwnpath)
        #             except:
        #                 st.write("Failed")
        #         else:
        #             st.write("Didn't work") 
        # with col2:
        #     st.header("Audio Quality")
        #     for i in audio_res:
        #         # st.write(i)
        #         if st.button("Download "+i.abr):
        #             # st.write("It worked, sorta")
        #             yt = YouTube(link)
        #             # yt.streams.filter(abr=i,only_audio=True).first().download(output_path=dwnpath)
        #             yt.streams.get_audio_only().download()
        #         else:
        #             st.write("Didn't work")
    except:
        pass
with tab2:
    try:
        link = st.text_input("Paste the YouTube Channel Link here")
        yt = Playlist(url=link)
        st.title(yt.videos[0].title)
        st.image(yt.videos[0].thumbnail_url)
        video_res = yt.videos[0].streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc()
        video_res = [i.resolution for i in video_res]
        audio_res = yt.videos[0].streams.filter(only_audio=True).order_by('abr').desc()
        audio_res = [i.abr for i in audio_res]

        option = st.selectbox("Select the Download type :",options=video_res+audio_res,help="Select the download format")

        if st.button("Download"):
            video_object = Playlist(link)
            if option in (video_res):
                for video in video_object.videos:
                    video.streams.filter(resolution=option,progressive=True,file_extension="mp4").first().download()
            if option in (audio_res):
                for video in video_object.videos:
                    video.streams.filter(abr=option,only_audio=True,file_extension="mp3").first().download()
        # videos_list = [x.title for x in yt.videos]
        # video_dict = {item: i for i, item in enumerate([x.title for x in yt.videos])}
        # video_choice = st.selectbox("Select video to preview", options=videos_list)
        
        # st.write(video_dict)

        if st.button("Pre-View"):
            st.video(yt.video_urls[0])
            st.write(yt.playlist_url)
    except:
        pass