import speech_recognition as sr
import pyttsx3
import pywhatkit 


# nombre del asistente
name = 'samir'
#instancias
listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Buenos dias")
engine.runAndWait()

#motor de voz
def talk(text):
    engine.say(text)
    engine.runAndWait()

#elegir otra voz
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

def listen():
    try:
        with sr.Microphone() as source:
            print ("Escuchando consulta ...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            #reconoce el nombre en la grabacion
            if name in rec:
                #quita el nombre en la grabacion
                rec = rec.replace(name, "")
                print(rec)
    except:
        pass
    return rec

""" def run ():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace("reproduce", "")
        talk("Reproduciendo" + music)
        pywhatkit .playonyt(music)
run() """