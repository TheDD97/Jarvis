import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# not working import ecapture as ec
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
for voice in engine.getProperty('voices'):
    print(voice.id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Ciao, Buon giorno")
        print("Ciao, Buon giorno")
    elif hour >= 12 and hour < 18:
        speak("Ciao, Buon pomeriggio")
        print("Ciao, Buon pomeriggio")
    else:
        speak("Ciao, Buona sera")
        print("Ciao, Buona sera")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("In ascolto....")
        audio=r.listen(source)

        try:
            statement = r.recognize_google(audio,language='it-IT')
            print(f"hai detto:{statement}\n")
        except  Exception as e:
            speak("Mi dispiace ma non ho capito.... potresti ripetere?")
            return "None"
        return statement

print("Loading")
speak("Loading")
#speak("Signore..... mi sto avviando")
#wishMe()

if __name__ == '__main__':
    while True:
        speak("Che cosa posso fare per te?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5) 
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")