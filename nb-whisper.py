from transformers import pipeline

# Load the model
asr = pipeline("automatic-speech-recognition", "NbAiLabBeta/nb-whisper-large", device="cuda")

asr("podcast.mp3", chunk_length_s=30, return_timestamps=True, generate_kwargs={'task': 'transcribe', 'language': 'no'})
