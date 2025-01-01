import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("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")

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(audio_file)
        print("Transcript:", transcript)

# Replace 'path_to_your_audio_file.wav' with the actual path to your audio file
transcribe_audio("C:\Users\abhiy\Downloads\Projects\AI Voice Assistant\ai.wav")
