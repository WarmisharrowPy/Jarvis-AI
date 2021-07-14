import speech_recognition as jarvis
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = jarvis.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()



def take_command():
    try:
      with jarvis.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'jarvis' in command:

                    print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A,%B,%D')
        talk('current date is' + date)
        print(date)
    elif'find' in command:
        find = command.replace('find', '')
        find = take_command()
        url = 'https://google.com/search?q=' + find
        webbrowser.get().open(url)
        print('here is what i for for ' + find)
    elif 'search' in command:
        search = command.replace('search', '')
        info = wikipedia.summary(search, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokes =  talk(pyjokes.get_joke())
        print(jokes)
    elif 'google' in command:
        webbrowser.open('https://google.com')
    elif 'thank you' in command:
        talk('its my duty sir ')
    elif 'how are you' in command:
        talk('i am good')
        talk('how about you?')
    elif 'i am good' in command:
        talk('good to hear')
    elif 'exit' in command:
        exit()


while True:
    run_jarvis()