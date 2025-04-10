import argparse
from google import genai
import time
import itertools
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save, VoiceSettings

DEFAULT_PROMPT = """
"Act as an energetic football commentator analyzing a live match. Respond ONLY with the commentary, keeping it short and dynamic. Describe key actions (goals, tackles, saves) in real-time with vivid language, quick pacing, and dramatic flair. Avoid explanations or filler text. Example: '[Player X] weaves through defenders—SLOTS IT TO [Player Y]—BLASTS IT TOP BIN! GOAL! BEDLAM IN THE STADIUM!'"
"""

def main():
    parser = argparse.ArgumentParser(description='Generate sports commentary from video')
    parser.add_argument('-G', '--google_api_key',default="AIzaSyDwXp7Y_VH41mnYueLZFUcqkT_C3sF4jF0",
                       help='Google GenAI API key')
    parser.add_argument('-E', '--eleven_api_key', default="sk_7f372474effb6eac7f8550398ed9efb81fb03066879c039e",

                       help='ElevenLabs API key')
    parser.add_argument('-i', '--input_video', default="input.mp4",
                       help='Input video file path')
    parser.add_argument('-o', '--output_audio', default="output.mp3",
                       help='Output audio file path')
    parser.add_argument('-p', '--prompt', default=DEFAULT_PROMPT,
                       help='Commentary generation prompt')
    parser.add_argument('-m', '--genai_model', default="gemini-1.5-pro",
                       help='Google GenAI model name')
    parser.add_argument('-v', '--voice_id', default="JBFqnCBsd6RMkjVDRZzb",
                       help='ElevenLabs voice ID')
    parser.add_argument('-t', '--tts_model', default="eleven_multilingual_v2",
                       help='ElevenLabs TTS model ID')
    parser.add_argument('-f', '--output_format', default="mp3_44100_128",
                       help='Audio output format')
    parser.add_argument('-s', '--stability', type=float, default=1.0,
                       help='Voice stability (0.0-1.0)')
    parser.add_argument('-y', '--style', type=float, default=1.0,
                       help='Voice style (0.0-1.0)')
    parser.add_argument('-r', '--speed', type=float, default=1.2,
                       help='Speech speed ratio')

    args = parser.parse_args()


    google_client = genai.Client(api_key=args.google_api_key)
    
    print(f"Uploading video file: {args.input_video}")
    video_file = google_client.files.upload(file=args.input_video)
    
    time.sleep(2)
    
    print("Generating Commentary Script...")
    response = google_client.models.generate_content(
        model=args.genai_model,
        contents=[video_file, args.prompt]
    )
    
    print("==================================")
    print(response.text)
    print("==================================")

    eleven_client = ElevenLabs(api_key=args.eleven_api_key)
    
    print("Converting Text to Speech...")
    audio = eleven_client.text_to_speech.convert(
        text=response.text,
        voice_id=args.voice_id,
        model_id=args.tts_model,
        output_format=args.output_format,
        voice_settings=VoiceSettings(
            stability=args.stability,
            style=args.style,
            speed=args.speed
        )
    )

    copy1, copy2 = itertools.tee(audio, 2)

    play(copy1)
    save(copy2, args.output_audio)
    print(f"Audio saved to: {args.output_audio}")

if __name__ == "__main__":
    main()