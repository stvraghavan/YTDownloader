# import the libraries
import pytube
import requests

# enter the video URL
url = 'https://youtu.be/9kxTOxDGLqs'

# create a YouTube object
yt = pytube.YouTube(url)

# get the streams
streams = yt.streams.filter(progressive=True, file_extension='mp4')

# get the video length
video_length = yt.length

# calculate the part length
part_length = video_length / 10

# get the stream URL
stream_url = streams.first().url

# download the video parts
start_byte = 0
end_byte = part_length * 1e6
for i in range(10):
    part = requests.get(stream_url, headers={'Range': f'bytes={start_byte}-{end_byte}'})
    with open(f'part_{i+1}.mp4', 'wb') as f:
        f.write(part.content)
    start_byte = end_byte
    end_byte += part_length * 1e6
