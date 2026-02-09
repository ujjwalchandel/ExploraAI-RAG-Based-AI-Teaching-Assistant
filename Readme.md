# How to use this RAG AI Teaching assistant on your own

## Step 1: Collect you video lectures
Move all your video content inside the `videos` folder

## Step 2: installing and configure "ffmpeg" 
- download "ffmpeg.exe" zip file - "https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2026-01-29-13-00/ffmpeg-N-122586-g2a0a32c42b-win64-gpl-shared.zip"

- Extract the zip file and go inside, copy all files and folder inside it including `bin`

- Move to C drive on your pc inside Program Files folder, create a new folder named `ffmpeg` and paste all the copied files and folder inside it.

- Paste all extracted files inside ffmpeg folder and copy the path of bin folder inside it.

- Now in environment variable select path and edit, click on new option and paste the path there and save the setting.

- For installion you can watch the video - "https://youtu.be/c8pp1CF5jhM?si=9UhJGXNnsaeixDpI"

## Step 3: Install all dependencies
Install using:

```
pip install -r requirements.txt
```

## Step 4: Convert video into mp3
Convert all the video into mp3 audio by running `video_into_audio.py` file. 
It will convert and store all mp3 files inside `audios` folder.

## Step 5: Convert all audios into json
Run `audio_to_JSON.py`
It will convert all mp3 files into text and process it into json format inside `jsons` folder.

## Step 6: Convert the json file to vectors
Run `text_to_embedding.py` 
It will convert json files into DataFrame with embeddings and save it as a joblib pickle file

## Step 7: Inference
Load the joblib file and create a relevant prompt using the data as per the user query and feed it to the local LLM and give you response.

# Ollama Installation (Recommended before Inference)

This guide explains how to install **Ollama** on Windows and how to download and run the **LLaMA 3.2** model using Ollama.

---

## Prerequisites

- Windows 10 or Windows 11 (64-bit)
- Minimum 8 GB RAM (16 GB recommended)
- Stable internet connection

---

## Step 1: Download and Install Ollama

1. Visit the official Ollama website:

"https://ollama.com/download"

2. Click on **Download for Windows**.

3. Run the downloaded installer (`OllamaSetup.exe`).

4. Follow the installation Steps (default settings are fine).

5. Once installed, **restart your system** (recommended).

---

## Step 2: Verify Ollama Installation

1. Open **Command Prompt** or **PowerShell**
2. Run the following command:
```
ollama --version
```

## Step 3: Install Llama 3.2 Model

Use the following command to download and install the Llama 3.2 model:

```
ollama pull llama3.2
```
