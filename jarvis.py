'''
Pausing this to first focus on the basics
'''


import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def speak(audio):
    '''
    Enables Jarvis to speak
    '''
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    '''
    Greets the user according to the hour
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good morning sir!")
    
    elif hour >= 12 and hour < 17:
        speak("Good afternoon sir!")
    
    else:
        speak("Good evening sir!")

    speak("How may I help you?")
    
def take_command():
    '''
    Takes micorphone input from the user and converts it into a string
    '''
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1   # changing the pause threshold to 1 second
        audio = r.listen(source)

    try:
        print("On it...")
        query = r.recognize_google(audio, language="en-in")     # using the google speech recognition API
        print("{query}\n")

    except Exception as e:
        print("Could you say that again, please...")            
        return("None")

    return(query)

if __name__ == "__main__":
    wish_me()                   # wishes the user first
    take_command()