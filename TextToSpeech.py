import pyttsx3

text_speech = pyttsx3.init()
text_speech.setProperty("rate", 150)
text_speech.say("Hello and welcome to the William State Lee College of Engineering at the University of North Carolina at Charlotte")
text_speech.runAndWait()