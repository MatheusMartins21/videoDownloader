from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "url"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Caso precise verificar as opções de Download
# for stream in yt.streams:
#     print(stream)

# Baixar alguma versão específica
# yt.streams.filter(res='1080p').download()

ys = yt.streams.get_highest_resolution()
ys.download()