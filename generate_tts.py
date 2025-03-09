from gtts import gTTS

# Read the fact
with open("money_fact.txt", "r") as file:
    fact = file.read().strip()

# Convert to speech
tts = gTTS(text=fact, lang="en")
tts.save("money_fact.mp3")

print("✅ Voiceover saved as 'money_fact.mp3'")
