from numpy import true_divide
import pywhatkit as kt
import pyautogui
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

keyword = {
    "search":"cerca",
    "name": "jarvis",
    "videoPlayer":"youtube"
}

started = False
engine = pyttsx3.init('sapi5')
print(engine.getProperty('rate'))
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
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
            audio=r.listen(source)
            try:
                statement = r.recognize_google(audio,language='it-IT')
                print(f"hai detto:{statement}\n")
            except  Exception as e:
                speak("Non ho capito....")
                return "None"
            return statement
    return "None"

def cleanRequest(type, statement):
    request = statement
    if(type == keyword['videoPlayer']):
        request = request.replace(keyword['search'],'')
        request = request.replace('su','')
        request = request.replace(keyword['videoPlayer'],'')
    elif type == 'google':
        request = request.replace(keyword['search'],'')
    return request

def adjustVolume(key,statement):
    result = statement
    if "del" in statement:
        result = result.replace('del','')
        if "%" in statement:
            result = result.replace('%','')
        if "per cento":
            result = result.replace('per cento','')
        if "x 100" in statement:
            result = result.replace('x 100','')
    if key == 'down':
        result = result.replace('abbassa il volume','')
        result = result.replace(" ","")
        for _ in range (int(int(result)/2)):
            pyautogui.press('volumedown')
    elif key == 'up':
        result = result.replace('alza il volume','')
        result = result.replace(" ","")
        for _ in range (int(int(result)/2)):
            pyautogui.press('volumeup')
    elif key == 'mute':
        pyautogui.press('volumemute')

speak("Signore..... mi sto avviando")

if __name__ == '__main__':
    speak("...Signore..... mi sto avviando")
    webbrowser.register('chrome',None)
    isMuted = False
    while True:
        initialize = startJarvis().lower()
        if(keyword["name"] in initialize):
            started = True
        while started:
            speak("Che cosa posso fare per te?")
            statement = takeCommand().lower()
            if statement == 0:
                continue
            if "basta" in statement or "annulla" in statement or "chiudi" in statement or "stop" in statement:
                speak('OK')
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
            if keyword['videoPlayer'] in statement:
                speak("Sto cercando su "+keyword['videoPlayer'])
                request = cleanRequest(keyword['videoPlayer'],statement)
                if request == "":
                     webbrowser.open_new_tab("https://www."+keyword['videoPlayer']+".com")
                else:
                    webbrowser.open_new_tab("https://www."+keyword['videoPlayer']+".com/results?search_query="+request)
                time.sleep(5)
                started = False
            elif 'cerca' in statement:
                speak("Sto cercando")
                request = cleanRequest('google',statement)
                kt.search(request)
                started = False
            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                started = False
            elif 'ore' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sono le. {strTime}")
                wishMe()
                started = False
            elif 'abbassa il volume' in statement:
                speak("Sto abbassando il volume")
                request = adjustVolume('down',statement)
                started = False
            elif 'alza il volume' in statement:
                speak("Sto alzando il volume")
                request = adjustVolume('up',statement)
                started = False
            elif 'zitto' in statement:
                if isMuted == False:
                    isMuted = True
                    speak("ok")
                    request = adjustVolume('mute',statement)
                    started = False
            elif 'puoi parlare' in statement or "parla" in statement:
                if isMuted:
                    isMuted = False
                    request = adjustVolume('mute',statement)
                    speak("va bene")
                    started = False