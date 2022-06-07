import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import shutil
import warnings
import os
import pyaudio
def TakeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 50

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print('Recognizing')

            Query = r.recognize_google(audio, language= 'en')
            print('the command is printed=', Query)
        
        except Exception as e:
            print(e)
            print('Say that again')
            return None
        return Query

def Speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    engine.say(audio)

    engine.runAndWait()

def tellDate():
    day = datetime.datetime.today().weekday() + 1

    Day_dic = {1: 'Monday', 2: 'Tuesday',
               3: 'Wednesday', 4: 'Thursday',
               5: 'Friday', 6: 'Saturday',
               7: 'Sunday'}
    if day in Day_dic.keys():
        day_of_the_week = Day_dic[day]
        print(day_of_the_week)
        Speak('The day is ' + day_of_the_week)

def TellTime(self):
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    minute = time[14:16]
    Speak(self,'The time is sir' + hour  + 'hours and ' + minute + 'minutes')

def Hello():
    Speak("hello breana I am your Virtual assistant. Tell me how may I help you")

def username():
    Speak('What should i Call you? ')
    uname = TakeCommand()
    Speak('Weclome')
    Speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    Speak(f"How can i Help you, {uname}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak('Good Morning Sir!')

    elif hour >= 12 and hour < 18:
        Speak('Good afternoon sir!')

    else:
        Speak('Good Evening Sir!')


def TakeQuery():

    while(True):
        query = TakeCommand().lower()
        if 'open youtube' in query:
            Speak('Opening Youtube')

            webbrowser.open('www.youtube.com')
            continue
        elif 'open google' in query:
            Speak('Opening Google')
            webbrowser.open('www.google.com')

        elif 'what day is it' in query:
            tellDate()
            continue
        elif 'what time is it' in query:
            TellTime()
            continue

        elif 'bye' in query:
            Speak('Bye')
        
        elif 'from wikipedia' in query:
            Speak('checking wikipedia, hold on')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=5)
            Speak('According to Wikipedia')
            Speak(result)
            continue

        elif 'Tell me your name' in query:
            Speak('Demar did not gave me a name as yet but I am your virtual assistant')
            continue
        elif 'play music' in query or "play song" in query:
            Speak("Here you go with music")
            music_dir = "C:/Users/demar/Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
            continue
        elif "who made you" in query or "who created you" in query:
            Speak("I have been created by Demar.")
            continue
        
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    TakeQuery()
