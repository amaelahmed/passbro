import os
import random
import requests
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image

def get_random_fact():
    facts = [
        "In Canada, $1 million in $1 coins would weigh about 17 tons.",
        "The largest bill ever printed by the U.S. was a $100,000 note.",
        "A penny costs more to produce than it is worth.",
        "Monopoly has printed more money than the U.S. Treasury.",
        "The world's first paper money was created in China over 1,400 years ago."
    ]
    return random.choice(facts)

def download_background():
    url = "https://upload.wikimedia.org/wikipedia/commons/4/4d/Dollar_banknotes.png"
    response = requests.get(url)
    if response.status_code == 200:
        with open("background.jpg", "wb") as file:
            file.write(response.content)
    else:
        print("Failed to download background image.")

def create_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save("audio.mp3")

def create_video():
    if not os.path.exists("background.jpg") or os.path.getsize("background.jpg") == 0:
        download_background()
    
    image = Image.open("background.jpg")
    image = image.resize((1280, 720))  # Corrected resize function
    image.save("resized_background.jpg")
    
    image_clip = ImageClip("resized_background.jpg", duration=10)
    audio_clip = AudioFileClip("audio.mp3")
    
    final_clip = image_clip.set_audio(audio_clip)
    final_clip.write_videofile("output.mp4", fps=24, codec='libx264', audio_codec='aac')

def main():
    fact = get_random_fact()
    print("Selected Fact:", fact)
    create_audio(fact)
    create_video()
    print("Video creation completed!")

if __name__ == "__main__":
    main()

