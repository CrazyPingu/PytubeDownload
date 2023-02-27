import os
import PySimpleGUI as sg
from yt_dlp import YoutubeDL

sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.
layout = [  [sg.Text('Video/Playlist URL or Video title:')],
            [sg.InputText()],
            [sg.Text('Audio only?')],
            [sg.Button('Yes'), sg.Button('No')],
            [sg.Text('Where do you want to save it?')],
            [sg.Text(os.path.expanduser('~')+'/Desktop/'),
            sg.FolderBrowse(initial_folder=os.path.expanduser('~')+'/Desktop/')],
        ]

# Create the Window
window = sg.Window('PytubeDownload', layout)

event, values = window.read()
if event == 'Yes':
    audio_only = True
if event == 'No':
    audio_only = False
video = values[0]
out_dir = values["Browse"] + "/" if values["Browse"] else os.path.expanduser('~')+'/Desktop/'
ydl_opts = {
    'outtmpl': out_dir+'%(title)s [%(id)s].%(ext)s',
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'default_search': 'auto',
    'ignoreerrors': True,
    'cookiesfrombrowser': ('brave',),
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

window.close()
