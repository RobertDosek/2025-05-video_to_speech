import whisper
import moviepy.editor as mp
from docx import Document
import time
import os
import shutil

script_start_time = time.time()

input_dir = 'input_files'
output_sound_dir = 'output_sound_files'
output_doc_dir = 'output_documents'

model = whisper.load_model("large")


def process_file(input_video):
    file_start_time = time.time()

    video_file = f"{input_dir}/{input_video}"
    print(f"Processing file: {video_file}")
    audio_file = f"{input_video.split('.')[0]}.mp3"
    doc_file = f"{input_video.split('.')[0]}.doc"

    video_clip = mp.VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file)

    audio_clip.close()
    video_clip.close()

    result = model.transcribe(audio_file, fp16=False, language='Czech')

    transcribed_text = result["text"]
    doc = Document()
    doc.add_paragraph(transcribed_text)
    doc.save(doc_file)

    shutil.move(audio_file, os.path.join(output_sound_dir, audio_file))
    shutil.move(doc_file, os.path.join(output_doc_dir, doc_file))
    os.remove(video_file)

    file_end_time = time.time()
    file_elapsed_time = file_start_time - file_end_time
    print(f"File execution time: {file_elapsed_time:.2f} seconds")
    time.sleep(900)


for file in os.listdir(input_dir):
    process_file(file)

script_end_time = time.time()
elapsed_time = script_start_time - script_end_time
print(f"Total execution time: {elapsed_time:.2f} seconds")
