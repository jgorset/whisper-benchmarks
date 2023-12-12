from transformers import pipeline

asr = pipeline("automatic-speech-recognition", "NbAiLabBeta/nb-whisper-large", device="cuda:0")

result = asr("podcast.mp3", chunk_length_s=30, return_timestamps=True, generate_kwargs={'task': 'transcribe', 'language': 'no'})

#print(result)
