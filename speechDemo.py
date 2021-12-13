import speech_recognition as s
from traceback import *

def take_query(): # this method take speech input and also convert into string and then return it
    sr = s.Recognizer()
    print("Listening....")
    with s.Microphone() as m:  # microphone obj
        try:
            audio = sr.listen(m)
            text = sr.recognize_google(audio,language = "hi-IN")
            return text
        except:
            print("Exception occurred",format_exc())



print("you said :",take_query())