#102017189
#Vishalakshi
#CS8
import os
import sys
import re
import random
import urllib.request
import pandas as pd
from pytube import YouTube
from pydub import AudioSegment
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

def downloader(singer,num_videos):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+ singer)
    video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    for i in range(num_videos):
      print("Song ",str(i+1)," is downloading ")
      songs = YouTube("https://www.youtube.com/watch?v=" + video_id[i])
      audio_file = songs.streams.filter(only_audio = True).first().download(filename = 'SONG-'+ str(i)+'.mp3')
    print("\n Audios Extracted and Downloaded")

def mashup(num_videos,duration):
  sound = AudioSegment.empty()
  for i in range(num_videos):
     audio_file = str(os.getcwd()) + "/SONG_" + str(i)+".mp3"
     try:
       file = AudioSegment.from_file(audio_file)
       sound += file[:duration*1000]
     except:
       f = AudioSegment.from_file(audio_file,format="mp4")
       sound += file[:duration*1000]
  
  return sound


def main():
    if len(sys.argv) == 5:
        singer = sys.argv[1]
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
        output = sys.argv[4]
    else:
        print("Wrong Number of Parameters Entered")
    
    print("Creating Mashup of ",singer,"'s ",num_videos," videos with duration",duration," each")

    singer = singer.replace(" ", "")+"latestsongs"

    downloader(singer,num_videos)
    final = mashup(num_videos,duration)
    final.export(output,format ="mp3")

    print("MASHUP HERE!!!!!")


if __name__ == '__main__':
   main()