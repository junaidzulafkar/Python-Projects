# MAC OS PYTHON PROGRAM ROBOSPEAKER
'''import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.2 Created By Junaid")
    y = input("Enter What you want to speak: ")
    command = f"say {y}"
    os.system(command)
'''
'''os.system(f"{y}")
os.system("say 'junaid'")'''

# WINDOWS OS PYTHON PROGRAM OF ROBOSPEAKER
# "pip install pywin32"   Module

'''from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == '__main__':
    speak("Hello, Junaid")'''

# Through ROBOSPEAKER TEXT

from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.speak(str)

if __name__ == '__main__':
    speak("Welcome to RoboSpeaker 1.2 Created By Junaid")
    print("Welcome to RoboSpeaker 1.2 Created By Junaid")
    print("Exit Command press 'q' and Enter")
    while True:
     y = input("Enter What you want me to speak: ")
     if y == "q":
         speak("Ok Bye Bye User")
         break
     speak(y)