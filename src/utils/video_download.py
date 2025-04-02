import os
import re
import subprocess

from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

class YoutubeDonwloader:
    def baixar_video(sefl, url='https://www.youtube.com/watch?v=nSKlgF7ilfM'):
        print(f'Download link: {url}')
        yt = YouTube(url, on_progress_callback=on_progress)

        video_title = yt.title

        # resolucoes = yt.streams.all()

        # high_res_text =''
        # high_res = 0

        # for i in resolucoes: # displays the available resolutions
        #     temp_resolution = i.resolution
            
        #     if temp_resolution:
        #         temp_resolution = [int(num) for num in re.findall(r"\d+", temp_resolution)][0]
        #         if temp_resolution > high_res:
        #             high_res = temp_resolution
        #             high_res_text = re.findall(r"\w+", i.resolution)[0]

        stream = yt.streams.get_highest_resolution(False)

        #stream = yt.streams.filter(resolution=high_res_text, progressive=False, file_extension="mp4").first()

        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        output_path = os.path.join(BASE_DIR, 'media/video')
        

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder create: "{output_path}"')
        
        title = re.sub(r'[<>:"/\\|?*]', '' ,video_title)
        title = title.replace("'", '')
        title = title.strip().replace(' ', '_')
        title = f'_{title}.mp4'

#_____________________________

        # Check if the stream is adaptive
        if not stream.is_progressive:
            # Get the audio stream with the best quality
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            print(f"Selected audio stream: {audio_stream.abr}")

            if not audio_stream:
                raise Exception('No suitable audio stream found.')

            # Download the video and audio streams
            video_path = stream.download(output_path,filename=f'tmp_vd_{title}')
            print(f"Video stream downloaded: {video_path}")
            audio_path = audio_stream.download(output_path,filename=f'tmp_ad_{title}.mp4')
            print(f"Audio stream downloaded: {audio_path}")

            # Combine the video and audio streams with ffmpeg
            Final_file = f'{output_path}/{title}'
            subprocess.run([
                'ffmpeg',
                '-i', video_path,
                '-i', audio_path,
                '-c:v', 'copy',
                '-c:a', 'aac',
                '-strict', 'experimental',
                Final_file
            ])
            print(f"Combined video saved: {Final_file}")

            # Clean up temporary files
            os.remove(video_path)
            os.remove(audio_path)

            print("Download and combination completed!")
        else:
            # Download the progressive stream
            video_path = stream.download(output_path,title)
            # video_stream.download(filename="final_video.mp4")
            print("Download completed!")

#____________________________________________________________

        print(f'Download video {video_title} on {video_path}')
        
        video_path_return = f'{output_path}/{title}'
        print(f'Download video on {video_path_return}')
        
        return video_path_return

# move this to test
if __name__ == '__main__':
    yt = YoutubeDonwloader()
    # yt_link = 'https://www.youtube.com/watch?v=nSKlgF7ilfM' #original
    
    yt_link = 'https://www.youtube.com/watch?v=ydSHDo574wA'
    
    yt.baixar_video(yt_link)