import pyttsx3
import sys

#txt = sys.argv
engine = pyttsx3.init()
#engine.say(txt)
engine.say("This is Text-To-Speech Engine Pyttsx3")
engine.runAndWait()
engine.stop()
