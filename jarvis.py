import speech_recognition as sr
import pyttsx3

# nombre del asistente
name = 'samir'
#instancias
listener = sr.Recognizer()
engine = pyttsx3.init()

#motor de voz
def talk(text):
    engine.say(text)
    engine.runAndWait()

#elegir otra voz
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

try:
    with sr.Microphone() as source:
        print ("Escuchando consulta ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        rec = rec.lower()
        if name in rec:
            talk(rec)
except:
    pass
