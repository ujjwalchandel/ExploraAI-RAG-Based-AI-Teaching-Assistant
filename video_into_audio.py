# Convert the videos into mp3 audio
import os
import subprocess

files = os.listdir("videos")

for file in files:
    file_name = file.split(".")[0]
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{file_name}.mp3"], shell=True, check=True)