import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

asr = pipeline("automatic-speech-recognition", "openai/whisper-large-v3", device="cuda:0")

result = asr("podcast.mp3", chunk_length_s=30, return_timestamps=True, generate_kwargs={'task': 'transcribe', 'language': 'no'})

#print(result)
