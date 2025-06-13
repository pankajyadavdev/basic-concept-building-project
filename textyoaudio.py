from gtts import gTTS
import os

text = "Your text goes here."
tts = gTTS(text=text, lang='en')  # Change 'en' to other languages (e.g., 'es', 'fr')
tts.save("output.mp3")
os.system("start output.mp3")  # Plays the file automatically (Windows)