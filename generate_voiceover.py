import pyttsx3

def generate_voiceover(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'voiceover.mp3')  # Saves the voiceover to an MP3 file
    engine.runAndWait()

# Test the TTS with the selected fact
generate_voiceover("The first paper money was created in China 1,400 years ago.")
