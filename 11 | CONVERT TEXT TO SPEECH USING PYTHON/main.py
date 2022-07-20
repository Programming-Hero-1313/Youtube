from gtts import gTTS

speech = gTTS(text="Hello Programmers", lang="en")

speech.save("speech.mp3")
