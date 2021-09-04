import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit as kit 
import os
import smtplib
from requests import get
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir.............88")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Gideon Sir. Please tell me how may I help you.......")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} ")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('deshmukhomkar900@gmail.com', 'o.m.k.a.r.@.00')
    server.sendmail('deshmukhomkar900@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open notepad' in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'chrome' in query:
            npath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(npath)

        elif 'play music' in query:
            music_dir = "C:\\Users\\OMKAR DESHMUKH\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'ip address' in query:
            ip = get("https://api.ipify.org")
            speak(f"your ip address is {ip}")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open whatsapp' in query:
            webbrowser.open("www.whatsapp.com")

        elif "open google" in query:
            speak("what should i search on google...")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919881065496", "hey Dad",2,58)

        elif "play song on youtube" in query:
            speak("which song should i play")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

    elif "email to DaD" in query:
        try:
            speak("what should i say..")
            content = takeCommand().lower()
            to = "aumenterprises@gmail.com"
            sendEmail(to,content)
            speak("email has been send to DaD")

        except Exception as e:
            print(e)
            speak("soory sir, i am not able to send this mail to DaD")

    elif "no thanks" in query:
        speak("thanks foe using me sir, have a good day.")
        sys.exit()


    speak("sir, do you have any other work")
