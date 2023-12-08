# Transcription tests

## Usage

Build the image:

```bash
docker build -t openai-whisper .
```

Run a shell in the image:

```bash
docker run --rm -it --gpus all --entrypoint bash openai-whisper
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
