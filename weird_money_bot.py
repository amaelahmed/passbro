import random
import os
from gtts import gTTS
from moviepy.editor import *
from PIL import Image
import requests

def get_random_fact():
    with open("facts.txt", "r") as file:
        facts = file.readlines()
    return random.choice(facts).strip()

def generate_voiceover(text, output_file="voiceover.mp3"):
    tts = gTTS(text, lang="en")
    tts.save(output_file)
    return output_file

def download_background_image():
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Dollar_banknotes.jpg"
    image_path = "background.jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_path, "wb") as file:
            file.write(response.content)
    else:
        print("Failed to download background image.")
    return image_path

def create_video():
    fact = get_random_fact()
    print(f"Selected Fact: {fact}")
    voiceover_file = generate_voiceover(fact)
    
    # Ensure background image exists
    if not os.path.exists("background.jpg") or os.path.getsize("background.jpg") == 0:
        print("Downloading new background image...")
        download_background_image()
    
    # Load background image and audio
    image = ImageClip("background.jpg", duration=5)
    audio = AudioFileClip(voiceover_file)
    
    # Resize and set video properties
    image = image.resize(height=1280, width=720)
    image = image.set_audio(audio)
    
    # Export final video
    video_output = "money_fact.mp4"
    image.write_videofile(video_output, fps=24, codec='libx264')
    print(f"Video saved as {video_output}")

def main():
    create_video()

if __name__ == "__main__":
    main()

