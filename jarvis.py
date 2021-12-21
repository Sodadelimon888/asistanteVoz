import speech_recognition as sr
import pyttsx3

#instancias
listener = sr.Recognizer()
engine = pyttsx3.init()

#motor de voz
engine.say("Buenos dias")
engine.runAndWait()
#elegir otra voz
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

try:
    with sr.Microphone() as source:
        print ("Escuchando consulta ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
except:
    pass
