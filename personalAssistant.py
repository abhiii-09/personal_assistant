import pyttsx3
import datetime
from pyttsx3 import driver
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#selenium setup
PATH = "C:\Program Files (x86)\chromedriver.exe"

#Assistant Voice setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
assistantName = "Charlie"
intro = "I am your personal Assistant" + assistantName

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir!")
    elif hour>=12 and hour<17:
        speak("Good afternoon Sir!")
    else:
        speak("Good evening Sir!")
    speak(intro)
    speak("How can I help you?")

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

# def sendWhatsApp(phoneNumber, message):
#     pywhatkit.sendwhatmsg_instantly(phoneNumber, message, 2)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Search Wikipedia
        if "who is" in query:
            speak("Searching in Wikipedia...")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipediaui")
            print(results)
            speak(results)

        #Open Youtube
        elif "open youtube" in query:
            speak("Sure sir...opening youtube")
            webbrowser.open("www.youtube.com")

        #Open Google
        elif "open google" in query:
             speak("Sure sir...opening google")
             webbrowser.open("www.google.com")

        #Open Hotstar
        elif "open hotstar" in query:
            speak("Sure sir...opening hotstar")
            webbrowser.open("www.hotstar.com")

        #Open Amazon Prime
        elif "open amazon prime" in query:
            speak("Sure sir...opening amazon prime")
            webbrowser.open("www.primevideo.com")

            #Open Gmail
        elif "open g mail" in query:
            speak("Sure sir...opening g mail")
            webbrowser.open("www.gmail.com")

        #Open Google Meet
        elif "open meet" in query:
            speak("Sure sir...opening google meet")
            webbrowser.open("https://meet.google.com/")

        #Time
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Currently the time is {strTime}")

        #Chords of
        elif "chords of" in query:
            song = query.replace("chords of", "")
            # if "by" in song:
            #     song = song.replace("by", "")
            # else:
            speak("Here are your chords sir!")
            driver = webdriver.Chrome(PATH)
            driver.get("https://chordseasy.com/")            
            search = driver.find_element_by_id("nav-search-bar")
            search.send_keys(song)
            search.send_keys(Keys.RETURN)
            run = driver.find_element_by_class_name("song-title")
            run.send_keys(Keys.RETURN)

        #Open VS Code
        elif "vs code" in query or "visual studio code" in query or "visual studio" in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        #Sending email
        # elif "email to abc" in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "abc@gmail.com"
        #         sendEmail(to, content)
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry! Couldn't send the email.")

        #play music in youtube     
        elif "play" in query:
            song = query.replace("play", "")
            speak("okay sir..playing" + song)
            pywhatkit.playonyt(song)

        #jokes
        elif "joke" in query:
            speak("Okay! Here's a funny one")
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            speak("hahaha")

        #info
        elif "what is" in query:
            search = query.replace("what is", "")
            speak("Here's what I found on Google")
            pywhatkit.search(search)

        #WhatsApp
        # elif "message" in query:
        #     speak("On what number should I send the message?")
        #     phone = takeCommand()
        #     phoneNumber = "+91"+phone
        #     speak("What should I write in the message?")
        #     message = takeCommand()
        #     speak("Alright! Sending message on WhatsApp")
        #     sendWhatsApp(phoneNumber, message)

        #quit
        elif "thank you" in query:
            print("Happy to help Sir!")
            speak("Happy to help Sir!")
            quit()

        #how are you?
        elif 'how are you' in query:
            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Sir")
            speak("How are you, Sir")
        elif 'I am fine' in query or "I am good" in query or "I'm fine" in query or "I'm good" in query:
            print("It's good to know that your fine")
            speak("It's good to know that your fine")

        #What is your name?
        elif "what's your name" in query or "What is your name" in query:
            toSpeak = "My friends call me" + assistantName
            speak(toSpeak)
            print("My friends call me", assistantName)

        #who made you?
        elif "who made you" in query or "who created you" in query:
            print("I have been created by Abhishek")
            speak("I have been created by Abhisheik")

        #who am I?
        elif "who am i" in query:
            print("If you talk, then definitely you are a human")
            speak("If you talk, then definitely you are a human")


        # #finding in google maps
        # elif "where is" in query:
        #             query = query.replace("where is", "")
        #             location = query
        #             speak("Locating")
        #             speak(location)
        #             webbrowser.open("https://www.google.nl / maps / place/" + location + "")




        
        


