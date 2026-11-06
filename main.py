import whisper
import moviepy.editor as mp
from docx import Document
import time

start_time = time.time()

directory = 'input_files'


video_file = '2024-08-16_video.mkv'
audio_file = '2024-08-16_audio.mp3'

video_clip = mp.VideoFileClip(video_file)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_file)

audio_clip.close()
video_clip.close()

model = whisper.load_model("large")
result = model.transcribe(audio_file, fp16=False, language='Czech')

transcribed_text = result["text"]
doc = Document()
doc.add_paragraph(transcribed_text)
doc.save("2024-08-16_large.docx")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total execution time: {elapsed_time:.2f} seconds")
