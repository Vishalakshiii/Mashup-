import os
import sys
import argparse
import youtube_dl
from moviepy.editor import *

def download_videos(singer_name, num_videos):
    ydl_opts = {'outtmpl': 'video-%(id)s.%(ext)s', 'format': 'best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        query = singer_name + ' songs'
        search_results = ydl.extract_info('ytsearch%d:%s' % (num_videos, query), download=False)['entries']
        video_files = []
        for result in search_results:
            if result.get('duration') and result['duration'] <= 600:
                video_files.append('video-%s.mp4' % result['id'])
                ydl.download(['https://www.youtube.com/watch?v=%s' % result['id']])
    return video_files

def convert_to_audio(video_files):
    audio_files = []
    for video_file in video_files:
        video = VideoFileClip(video_file)
        audio = video.audio
        audio_file = 'audio-' + video_file.split('.')[0] + '.mp3'
        audio.write_audiofile(audio_file)
        audio_files.append(audio_file)
        video.close()
    return audio_files

def cut_audio(audio_files, duration):
    cut_audio_files = []
    for audio_file in audio_files:
        audio = AudioFileClip(audio_file)
        cut_audio = audio.subclip(0, duration)
        cut_audio_file = 'cut-audio-' + audio_file.split('.')[0] + '.mp3'
        cut_audio.write_audiofile(cut_audio_file)
        cut_audio_files.append(cut_audio_file)
        audio.close()
    return cut_audio_files

def merge_audio(audio_files, output_file):
    merged_audio = None
    for audio_file in audio_files:
        audio = AudioFileClip(audio_file)
        if merged_audio is None:
            merged_audio = audio
        else:
            merged_audio = concatenate_audioclips([merged_audio, audio])
        audio.close()
    merged_audio.write_audiofile(output_file)
    merged_audio.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download and mashup N videos of X singer from YouTube')
    parser.add_argument('singer_name', type=str, help='Name of the singer to download')
    parser.add_argument('num_videos', type=int, help='Number of videos to download')
    parser.add_argument('audio_duration', type=int, help='Duration of audio to cut from each file')
    parser.add_argument('output_file', type=str, help='Name of the output file')
    args = parser.parse_args()

    if args.num_videos < 10:
        print('Number of videos must be greater than or equal to 10.')
        sys.exit(1)

    if args.audio_duration <= 20:
        print('Duration of audio to cut must be greater than 20 seconds.')
        sys.exit(1)

    try:
        video_files = download_videos(args.singer_name, args.num_videos)
        audio_files = convert_to_audio(video_files)
        cut_audio_files = cut_audio(audio_files, args.audio_duration)
        merge_audio(cut_audio_files, args.output_file)
        print('Mashup created successfully.')
    except Exception as e:
        print('An error occurred: ', str(e))