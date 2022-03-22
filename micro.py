
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

names = sr.Microphone.list_microphone_names()

print(names)