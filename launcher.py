import platform
import os
print("running")
print(platform.system())
if(platform.system() == "Windows"):
    print("win")
    os.system('cmd /k "pip install --upgrade setuptools numpy SpeechRecognition pyttsx3 datetime wikipedia ecapture wolframalpha package-name pipwin pyaudio google pywhatkit flask pycaw -U scikit-image"')
