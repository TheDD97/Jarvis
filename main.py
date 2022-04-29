from numpy import true_divide
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

started = False
engine = pyttsx3.init('sapi5')
print(engine.getProperty('rate'))
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[3].id)
for voice in engine.getProperty('voices'):
    print(voice.id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    morning = "Buon giorno"
    afternoon = "Buon pomeriggio"
    evening = "Buona sera"
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak(morning)
        print(morning)
    elif hour >= 12 and hour < 18:
        speak(afternoon)
        print(afternoon)
    else:
        speak(evening)
        print(evening)

def startJarvis():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Eccomi sir....")
        audio=r.listen(source)
        try:
            initialize = r.recognize_google(audio,language='it-IT')
            print(f"hai detto:{initialize}\n ditemi")
        except  Exception as e:
            return "None"
        return initialize

def takeCommand():
    if(started):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("In ascolto....")
            audio=r.listen(source, timeout=5)
            try:
                statement = r.recognize_google(audio,language='it-IT')
                print(f"hai detto:{statement}\n")
            except  Exception as e:
                speak("Non ho capito.... potresti ripetere?")
                return "None"
            return statement
    return "None"

speak("...Signore..... mi sto avviando")

if __name__ == '__main__':
    while True:
        initialize = startJarvis().lower()
        if("jarvis" in initialize):
            started = True
        while started:
            speak("Che cosa posso fare per te?")
            statement = takeCommand().lower()
            if statement == 0:
                continue
            if "basta" in statement or "annulla" in statement or "chiudi" in statement or "stop" in statement:
                speak('OK')
                print('your personal assistant G-one is shutting down,Good bye')
                started = False
                break
            # if 'wikipedia' in statement:
            #     speak('lo cerco su Wikipedia...')
            #     statement = statement.replace("wikipedia", "")
            #     results = wikipedia.summary(statement, sentences=3)
            #     speak("According to Wikipedia")
            #     print(results)
            #     speak(results)
            # el
            if 'youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Avvio Youtube")
                time.sleep(5)
                started = False
            elif 'apri google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Sto aprendo Google Chrome")
                time.sleep(5)
                started = False
            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5) 
                started = False
            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sono le. {strTime}")
                wishMe()
                started = False