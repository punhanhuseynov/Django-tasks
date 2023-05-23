from pytube import YouTube
from mo
# YouTube videosunu indirin
yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
yt.streams.filter(only_audio=True).first().download()

from moviepy.editor import *

# MP4 dosyasını yükleyin
clip = AudioFileClip("video.mp4")

# MP3 dosyasını oluşturun
clip.write_audiofile("audio.mp3")