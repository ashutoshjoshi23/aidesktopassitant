import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hey Ashutosh Sir! I am Charlie. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com/in/")

        elif 'open github' in query:
            webbrowser.open("https://github.com/ashutoshjoshi23")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")

        elif 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")

        elif 'open photos' in query:
            webbrowser.open("https://photos.google.com/")

        elif 'play song' in query:
            music_dir = "C:\\Users\\abhij\\OneDrive\\Desktop\\Ashutosh\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\abhij\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open tableau' in query:
            codePath = "C:\\Program Files\\Tableau\\Tableau Public 2020.3\\bin\\tabpublic"
            os.startfile(codePath)

        elif 'open shutdown' in query:
            codePath = "C:\\Windows\\System32\\SlideToShutDown.exe"
            os.startfile(codePath)

        elif 'open series' in query:
            codePath = "D:\\Series"
            os.startfile(codePath)
