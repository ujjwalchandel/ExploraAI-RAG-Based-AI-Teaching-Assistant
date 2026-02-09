import os
import whisper
import json

files = os.listdir("audios")

file = files[1]


model = whisper.load_model("large-v2")
result = model.transcribe(f"audios/sample.mp3", language = "en", task = "translate", word_timestamps= False)

chunks = []

for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

with open("output.json", "w") as f:
    json.dump(chunks, f)