import os
import traceback
from yt_dlp import YoutubeDL

try:
    while True:
        video = input('\nVideo/Playlist URL or Video title: ')
        audio_only = input('Audio only? (y/N): ').lower() == 'y'
        out_dir = os.path.expanduser('~')+'/Desktop/'
        ydl_opts = {
            'outtmpl': out_dir+'%(title)s [%(id)s].%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'default_search': 'auto',
            'ignoreerrors': True,
            'cookiesfrombrowser': ('chrome',),
            'overwrites': False,
            'writethumbnail': audio_only,
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegMetadata'}
            ] if audio_only else [{'key': 'FFmpegMetadata'}],
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video])
except KeyboardInterrupt:
    quit(0)
except Exception:
    input('\n'+traceback.format_exc()+'Press Enter to exit...')