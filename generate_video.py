from moviepy.editor import *

# Load the voiceover audio
audio = AudioFileClip("money_fact.mp3")

# Create a text clip for the title
text = TextClip("Weird Money Fact!", fontsize=70, color="white", font="Arial-Bold")\
    .set_position("center")\
    .set_duration(audio.duration)

# Load the background image
image = ImageClip("background.jpg").set_duration(audio.duration).resize((1080, 1920))

# Overlay the text on the image
video = CompositeVideoClip([image, text])

# Set the audio for the video
video = video.set_audio(audio)

# Save the final video file
video.write_videofile("money_fact_video.mp4", fps=30, codec="libx264")

print("✅ Video saved as 'money_fact_video.mp4'")

