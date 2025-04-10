Here's a short and clear `README.md` file for your project:

---

# ⚽ AI Sports Commentator

Generate dynamic, real-time-style football commentary from video clips using Google GenAI and ElevenLabs TTS.

## 🎯 Features

- Uploads a video and generates lively sports commentary
- Uses Google GenAI (Gemini) to create vivid, fast-paced analysis
- Converts text to energetic speech using ElevenLabs
- Outputs a playable and savable MP3 file

## 🛠 Requirements

- Python 3.8+
- Google GenAI API key
- ElevenLabs API key

Install required packages:

```bash
pip install google-generativeai elevenlabs
```

## 🚀 Usage

```bash
python commentator.py -i input.mp4 -o output.mp3
```

### Optional Flags

| Flag              | Description                          | Default                     |
|-------------------|--------------------------------------|-----------------------------|
| `-G` / `--google_api_key` | Google GenAI API key                | *(replace with your key)*   |
| `-E` / `--eleven_api_key` | ElevenLabs API key                  | *(replace with your key)*   |
| `-p` / `--prompt`         | Custom GenAI prompt                 | Pre-set football style      |
| `-m` / `--genai_model`    | GenAI model name                    | `gemini-1.5-pro`            |
| `-v` / `--voice_id`       | ElevenLabs voice ID                 | `JBFqnCBsd6RMkjVDRZzb`      |
| `-t` / `--tts_model`      | ElevenLabs TTS model                | `eleven_multilingual_v2`    |
| `-f` / `--output_format`  | Output audio format                 | `mp3_44100_128`             |
| `-s` / `--stability`      | Voice stability (0.0–1.0)           | `1.0`                       |
| `-y` / `--style`          | Voice style (0.0–1.0)               | `1.0`                       |
| `-r` / `--speed`          | Speech speed multiplier             | `1.2`                       |

