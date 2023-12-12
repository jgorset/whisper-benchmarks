# Transcription tests

## Installation

```bash
sudo apt install ffmpeg
```

```bash
pip install -r requirements.txt
```

## Benchmarks

### OpenAI Whisper Large v3 on podcast.mp3

```
$ whisper --model large --language Norwegian --device cuda podcast.mp3

File: ./benchmarks/podcast-openai-whisper-large-v3.srt
Time: 7 minutes 12 seconds
```

### NB Whisper Large on podcast.mp3

```
$ python nb-whisper.py

File: ./benchmarks/podcast-nb-whisper-large-v3.json
Time: 2 minutes 28 seconds
```
