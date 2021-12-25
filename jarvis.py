import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishes the user
def wish_me():
    hour = int(datetime.datetime.now().hour)
    # wishing according to the hour
    if hour >= 5 and hour < 12:
        speak("Good morning sir!")
    
    elif hour >= 12 and hour < 17:
        speak("Good afternoon sir!")
    
    else:
        speak("Good evening sir!")

    speak("How may I help you?")
    
if __name__ == "__main__":
    wish_me()                   # wishes the user first