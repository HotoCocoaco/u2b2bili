from __future__ import unicode_literals

import os
import sys

import youtube_dl

ydl_opts = {
    'outtmpl': '%(playlist_index)02d-%(title)s.%(ext)s',
    'writesubtitles': True,
    'writethumbnail': False,
    'subtitleslangs': ['zh-CN']
}
ffmpeg_command = 'ffmpeg -y -i "%(video_file_name)s" -vf "subtitles=%(sub_file_name)s" -c:v libx264 -preset %(' \
                 'preset)s -crf %(crf)d -c:a aac -b:a %(audio_bit_rate)dk "%(output_file_name)s.%(output_format)s" '
ffmpeg_opts = {
    'preset': 'slower',
    'crf': 24,
    'audio_bit_rate': 128,
    'output_format': 'flv'
}


def down_video(urls):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
    pass


def burn_subtitles(del_original_file=True):
    exts = ['.mp4', '.mkv', 'webm']
    for i in os.listdir("./"):
        if os.path.splitext(i)[1] in exts:
            ffmpeg_opts['video_file_name'] = i
            ffmpeg_opts['sub_file_name'] = os.path.splitext(i)[0] + '.' + ydl_opts['subtitleslangs'][0] + '.vtt'
            ffmpeg_opts['output_file_name'] = os.path.splitext(i)[0]
            os.system(ffmpeg_command % ffmpeg_opts)
            if del_original_file:
                os.remove(ffmpeg_opts['video_file_name'])
                os.remove(ffmpeg_opts['sub_file_name'])
    pass


def main():
    if len(sys.argv) == 1:
        print('ERROR: 请至少输入一个URL')
        return
    down_video(sys.argv[1:])
    burn_subtitles()
    pass


if __name__ == '__main__':
    main()
