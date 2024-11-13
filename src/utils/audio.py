import os

from moviepy.editor import *
from faster_whisper import WhisperModel

from dotenv import load_dotenv

load_dotenv()

class Audio:
    def extrair(video_path):
        print(f'Extract WAV audio from {video_path}')
        video_path = video_path.replace("'", "")

        output_path = os.path.dirname(video_path)
        output_path = output_path.replace('video', 'audio')
        print(f'Output audio path {output_path}')

        base_name = os.path.splitext(os.path.basename(video_path))[0]
        print(f'basename path {base_name}')

        audio_path = f'{output_path}/{base_name}.mp3'
        print(f'audio path {audio_path}')

        video = VideoFileClip(video_path)

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f'Folder create: "{output_path}"')

        video.audio.write_audiofile(audio_path)

        print(f'audio save on {audio_path}')

        return audio_path

    def transcribe(audio_path:str) -> str:
        print(f'Transcr WAV audio from {audio_path} to text')
        audio_path = audio_path.replace("'", "")

        model = WhisperModel('medium',device="cuda") #'cuda'

        result = model.transcribe(audio_path, language='pt')

        transcribe = ''
        for segment in result[0]:
            transcribe += segment.text + ' '

        output_path = os.path.dirname(audio_path)
        output_path = output_path.replace('audio', 'transc')
        print(f'Output transc path {output_path}')
        
        base_name = os.path.splitext(os.path.basename(output_path))[0]
        transcribe_path = f'{output_path}/{base_name}.md'
        
        if not os.path.exists(transcribe_path):
            os.makedirs(output_path)
            print(f'Folder create: "{transcribe_path}"')
        
        with open(transcribe_path, 'w', encoding='utf-8') as f:
            f.write(transcribe.strip())

        print(f'Save transcribe_path on: "{transcribe_path}"')

        return transcribe_path


# move this to test
if __name__ == '__main__':
    
    video_path = '/workspaces/Video_to_text/media/video/_Hamas_pede_o_fim_das_hostilidades.mp4'
    
    audio_path = Audio.extrair(video_path)
    
    adio_transcr = Audio.transcribe(audio_path)
