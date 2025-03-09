from gtts import gTTS
import os

# Step 1: Create a short script
script = "Did you know? The first paper money was created in China over 1,000 years ago!"

# Step 2: Generate voiceover using gTTS (Google Text-to-Speech)
tts = gTTS(text=script, lang='en')

# Save the audio as a file
audio_file = "voiceover.mp3"
tts.save(audio_file)

print(f"Voiceover saved as {audio_file}")
