import speech_recognition as sp
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)

    engine.runAndWait()

def alexa_command():
    try:
        with sp.Microphone() as source:
            print("listening...")
            voice = listener.listen(source,phrase_time_limit=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command
def alexa_run():
    command = alexa_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please tell the command again')


while True:
    alexa_run()
