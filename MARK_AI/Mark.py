import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import pyautogui
import pyjokes
from pytube import YouTube


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mark' in command:
                command = command.replace('mark', '')
    except:
        pass
    return command


def run_Mark():
    command = take_command()
    print(command)
    if "hello" in command or "hi" in command or "hey" in command:
            hour=datetime.datetime.now().hour
            if hour>=0 and hour<12:
                print("Hello,Good Morning")
                speak("Hello,Good Morning sir how can I help you")
            elif hour>=12 and hour<18:
                print("Hello,Good Afternoon")
                speak("Hello,Good Afternoon sir how can I help you")
            else:
                print("Hello,Good Evening")
                speak("Hello,Good Evening sir how can I help you")


    elif 'screenshot' in command:
        speak("And the file name would be...")
        name = input("[MARK] File Name ~: ")
        pyautogui.screenshot(f"{name}.png")
        speak("The screenshot has been taken sir, check this out")
        print(name)
        os.startfile(f"{name}.png")


    elif 'time' in command:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")


    elif "open" in command :
        try :
            website = command.split(' ')
            webbrowser.open("https://"+website[website.index("open")+1]+".com")
            speak(website[website.index("open")+1] + "is Opened ")
        except Exception as e :
            speak("i can't see it")


    elif 'joke' in command:
        speak(pyjokes.get_joke())

    
    elif 'wikipedia' in command:
            try:
                speak('Searching Wikipedia...')
                command =command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences=3)
                print("According to Wikipedia")
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                s = random.choice(e.options)
                print(s)
                speak(s)
            except wikipedia.exceptions.WikipediaException as e:
                print('Search not include, try again wikipedia and your search')
  
    elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            print("Youtube is open now")
            speak("youtube is open now")
                

    elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            print("Google chrome is open now")
            speak("Google chrome is open now")
                

    elif 'open gmail' in command:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                print("Google Mail open now")
                speak("Google Mail open now")


    elif "open discord" in command:
        os.system(f"C:\\Users\\USER\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
        speak("Opening Discord") 



    elif "download video" in command:
        speak("Put The URL Link")
        link = input("[MARK] Url ~$ ")
        if link:
            video = YouTube(link)
            print("[MARK] Downloading..")
            speak("OK, Sir Iam Downloading The Video" + video.title)
            stream = video.streams.get_highest_resolution()
            stream.download()



while True:
    run_Mark()
