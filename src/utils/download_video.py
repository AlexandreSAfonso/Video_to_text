import os
import re

#from pytube import YouTube
from pytubefix import YouTube
from pathlib import Path

class YoutubeDonwloader:
    def baixar_video(sefl, link='https://www.youtube.com/watch?v=nSKlgF7ilfM'):
        print(f'Download link: {link}')
        yt = YouTube(link)

        stream = yt.streams.get_highest_resolution()
        
        video_title = stream.title
        
        #stream = yt.streams.filter(only_audio=True).first
        #audio_stream = yt.streams.get_audio_only

        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        output_path = os.path.join(BASE_DIR, 'media/video')
        

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder create: "{output_path}"')
        
        title = re.sub(r'[<>:"/\\|?*]', '' ,video_title)
        title = title.replace("'", '')
        title = title.strip().replace(' ', '_')
        title = f'_{title}.mp4'

        video_path = stream.download(output_path,title)

        print(f'Dowload video {video_title} on {video_path}')
        
        video_path_return = f'{output_path}/{title}'
        print(f'Dowload video on {video_path_return}')
        
        return video_path_return


# move this to test
if __name__ == '__main__':
    yt = YoutubeDonwloader()
    # yt_link = 'https://www.youtube.com/watch?v=nSKlgF7ilfM'
    yt_link = 'https://www.youtube.com/watch?v=nSKlgF7ilfM'#'https://www.youtube.com/watch?v=cOpAm20ugjU'
    yt.baixar_video(yt_link)
