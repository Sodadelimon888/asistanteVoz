import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Buenos dias")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print ("Escuchando consulta ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
except:
    pass
