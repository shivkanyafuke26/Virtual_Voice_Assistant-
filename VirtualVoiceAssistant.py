import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening")

    speak("I am Doraemon sir. please tell me how may i help you")    


def takeCommand():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"        
    return query
if __name__ == "__main__":
    wishMe()
    if 1:
       query=takeCommand().lower()  

       if 'wikipedia' in query:
           speak("searching wikipedia... ")
           query=query.replace("wikipedia", "")
           results=wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'how are you' in query:
           speak("am good, how you doing sir")    
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'who are you' in query:
           speak("am your assistant Doraemon")                                                                                               
       elif 'open google' in query:
           webbrowser.open("google.com") 
       elif 'open whatsapp' in query:
           webbrowser.open("whatsapp.com")                                                                                           
       elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is {strTime}") 

       elif 'open code' in query:
           codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)   

       elif 'play music' in query:
           musicDir="C:\\Program Files\\iTunes\\iTunes.exe"
           os.startfile(musicDir)  
       elif 'open facebook' in query:
           webbrowser.open("facebook.com") 
       elif 'open twitter' in query:
           webbrowser.open("twitter.com")
       elif 'open instagram' in query:
           webbrowser.open("instagram.com") 
       elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Shivu.")
        