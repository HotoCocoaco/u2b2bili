from __future__ import unicode_literals
import os
import sys
import youtube_dl


def down_video(urls):
    # 下载参数
    ydl_opts = {
        'outtmpl': '%(playlist_index)d-%(title)s.%(ext)s',
        'writesubtitles': True,
        'writethumbnail': True,
        'subtitleslangs': ['zh-CN']
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
    pass


def burn_subtitles(del_original_file=True):
    for i in os.listdir("./"):
        if os.path.splitext(i)[1] == ('.mp4' or '.mkv' or '.webp'):
            print(i)
            os.system('ffmpeg -y -i "%s" -vf "subtitles=%s" -c:v libx264 -preset slower -crf 24 -c:a aac -b:a 192k "%s.flv"' % (
                i, os.path.splitext(i)[0] + '.zh-CN.vtt', os.path.splitext(i)[0]))

    if del_original_file:
        for i in os.listdir("./"):
            if os.path.splitext(i)[1] == ('.mp4' or '.mkv' or '.webp'):
                os.remove(i)
                os.remove(os.path.splitext(i)[0] + '.zh-CN.vtt')
    pass


def main():
    # 未传递参数直接跳出
    if len(sys.argv) == 1:
        print('ERROR: 请至少输入一个URL')
        return
    down_video(sys.argv[1:])
    burn_subtitles()
    pass


if __name__ == '__main__':
    main()
