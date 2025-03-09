                                                                                                                                                                                                                                           
┌──(venv)─(root㉿kali)-[/home/kali]
└─# import random
import pyttsx3
import cv2
import numpy as np
from instabot import Bot
import os

# Step 1: Generate a random weird money fact
facts = [
    "The first paper money was created in China during the Tang Dynasty.",
    "The US once had a $100,000 bill featuring Woodrow Wilson.",
    "The word 'dollar' comes from the German word 'thaler'.",
    "In 2008, Zimbabwe printed a 100 trillion dollar note."
]
fact = random.choice(facts)

# Step 2: Convert fact to voiceover
engine = pyttsx3.init()
engine.save_to_file(fact, 'voiceover.mp3')
engine.runAndWait()

# Step 3: Create a video with OpenCV and overlay the text
frame_width = 1920  # Width of the video
frame_height = 1080  # Height of the video
fps = 30  # Frames per second

# Create a VideoWriter object to save the video
out = cv2.VideoWriter('final_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Create a black image for the background
background = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

# Set font style and size for overlay text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # White color
thickness = 2
text_size = cv2.getTextSize(fact, font, font_scale, thickness)[0]
text_x = (frame_width - text_size[0]) // 2  # Center the text horizontally
text_y = (frame_height + text_size[1]) // 2  # Center the text vertically

# Add the text to the video for 5 seconds (adjustable duration)
for _ in range(fps * 5):
    frame = background.copy()
    cv2.putText(frame, fact, (text_x, text_y), font, font_scale, font_color, thickness)
    out.write(frame)

# Release the VideoWriter object
out.release()

# Step 4: Post video to Instagram
bot = Bot()
bot.login(username="stynraey", password="Hollycrapps.1#")
bot.upload_video("final_video.mp4", caption=fact)

print("Video created and uploaded successfully!")

