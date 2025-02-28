
import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrsary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "2837df83-56ac-4c72-bc75-95afb1411dce"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):
    client = OpenAI(api_key="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")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content  


def processCommand(c):

    if "open google" in c.lower():
        webbrowser.open("http://www.google.com")
        speak("Opening browser")
    elif "open youtube" in c.lower():
        webbrowser.open("http://www.youtube.com")
        speak("Opening youtube")
    elif "open facebook" in c.lower():
        webbrowser.open("http://www.facebook.com")
        speak("Opening facebook")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://www.linkedin.com")
        speak("Opening linkedin")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrsary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}") 

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

    
    # ...additional command handling...

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    #listen for the wake word "Jarvis"
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)

        print("Recognizing...")
        try:
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

                    if "open browser" in command.lower():
                        webbrowser.open("http://www.google.com")
                        speak("Opening browser")
                    # ...additional command handling...
        except Exception as e:
            print("Error: {0}".format(e))
            speak("Sorry, I didn't catch that.")