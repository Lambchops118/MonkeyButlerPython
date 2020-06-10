#Function: Listens for user given voice command, parses the string of the command, then acts accordingly if a special keyword is found in the string. Then outputs voice.
from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from playsound import playsound

def userCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ready for input.")
        r.puase_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower() #turns into string in lower case
        print("You Said: " + command + '\n')
    
    except sr.UnknownValueError:
        #print("That input could not be processed")
        command = userCommand()

    return command

def voiceAssistant(command):
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + "r/" + subreddit
        webbrowser.open(url)
        print("Task Completed.")
        playsound('voice/openReddit.mp3')
    
    elif 'open robin hood' in command:
        reg_ex = re.search('open robinhood (.*)', command)
        url = 'https://www.robinhood.com/'
        webbrowser.open(url)
        print("Task Completed.")
        playsound('voice/openRobinhood.mp3')

    elif 'ben wrote' or 'ben road' or 'ben roat' in command:
        print("Task Completed.")
        playsound('voice/roatLine.mp3')

    elif 'turn on the lights' or 'lights on' in command:
        playsound('voice/lightsOn.mp3')

    elif 'weather' in command:
        None
    
    elif 'temperature' in command:
        None
    
    elif 'humidity' in command:
        None

    else:
        None
    
#print("Ready for another order.")

#while True:
    #voiceAssistant(userCommand())
