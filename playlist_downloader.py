
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLvRfcAN-QbYncGDzMiG34xTdCdbIXEq2a')   # Enter playlist-url in place of url

for video in playlist.videos:
    print('Downloading : {} with url: {}'.format(video.title,video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
                download()
                
                    
        
