import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#####print(voices[0].id) ### Not needed
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("I am jarvis sir. please tell me how may I help you")

def takecommand():
    "It takes micro phone input from user and returns string output"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        ##print(e)   It is not good to see error if it not listin properly

        print("Say that again please...")
        return "None"
    return query


#def sendEmail(to, content):
   # server = smtplib.SMTP('smntp.gmail.com',587)
    #server.ehlo()
    #server.starttls()
    #server.login('yourgmail','yourpassword')
    #server.sendmail('youremail',to,content)
    #server.close()




if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\Projects'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")

        ##elif 'open pycharm' in query:
            ##codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1\\bin\\pycharm64.exe"
            ##os.startfile(codepath)

        #elif 'email to chethan' in query:
           # try:
                #speak("What should i say?")
                #content = takecommand()
                #to = 'chethanbr2121@gmail.com'
               # sendEmail(to,content)
                #speak("Email has been sent")
            #except Exception as e:
                #print(e)
                #speak("sorry my friend chethan, I am not able to send this email")
