import os
import whisper
import json


model = whisper.load_model("large-v2")

audio_files = os.listdir("audios")

for audio in audio_files:
    title = audio.split(".")[0]

    result = model.transcribe(f"audios/{audio}", language = "en", task = "translate")

    chunks = []

    for segment in result["segments"]:
        chunks.append({"title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})

    chunks_with_metadata = {"title": title, "text": result["text"], "chunks": chunks}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata, f, indent= 4)