import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose female voice (optional)
engine.setProperty('rate', 150)  # Speech rate

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
        return ""
    return command

def run_assistant():
    command = listen()

    if "time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {current_time}")

    elif "search" in command:
        topic = command.replace("search", "").strip()
        talk(f"Searching for {topic}")
        pywhatkit.search(topic)

    elif "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "open notepad" in command:
        talk("Opening Notepad")
        os.system("notepad.exe")

    elif "exit" in command or "quit" in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Please say the command again.")

# Main loop
talk("Hi, how can I assist you today?")
while True:
    run_assistant()
