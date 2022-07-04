import pyttsx3
import pywhatkit
import speech_recognition as sr
import keyboard
import time
# import datetime
# inicializamos el reconocimiento de voz
listener = sr.Recognizer()
# inicializamos pyttsx3
maria = pyttsx3.init()
# asignamos una velocidad
maria.setProperty('rate', 130)
# nombre de nuestro asistente
nombre = "maría"

def escuchar():
    """
    Permite escuchar por micrófono
    """
    try:
        # empezamos a escuchar por el micrófono
        with sr.Microphone() as micro:
            print("Escuchando...")
            # tomamos la lectura del micro
            audio = listener.listen(micro)
            # convertimos la lectura a estring
            audioTxt = listener.recognize_google(audio, language='es-ES')
            audioTxt = audioTxt.lower()
            #  print(audioTxt) descomentar para mostrar lo que escucha el micrófono
            # comprobamos si se ha llamado a nuestro asistente
            if nombre in audioTxt:
                audioTxt = audioTxt.replace(nombre, "")
                print(audioTxt)
    except:
        pass
    return audioTxt


def hablar(txt):
    """
    Función que va a permitir hablar a nuestro asistente
    @param txt: texto que va a decir nuestro asistente
    """
    maria.say(txt)
    maria.runAndWait()

def accion():
    """
    Función que va a ejecutar una orden dependiendo de la opción solicitada
    """
    opcion=escuchar()

    if "reproduce" in opcion:
        cancion= opcion.replace("reproduce", "")
        hablar(opcion.replace("reproduce", "reproduciendo"))
        pywhatkit.playonyt(cancion)
        time.sleep(5)
        keyboard.send("space")

accion()
"""""
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")

            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    engine.say(audio)

    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")


def Hello():
    speak("hello sir I am your desktop assistant. /
    Tell
    me
    how
    may
    I
    help
    you
    ")


def Take_query():
    Hello()

    while (True):

        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            webbrowser.open("www.geeksforgeeks.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue


        elif "bye" in query:
            speak("Bye. Check Out GFG for more exicting things")
            exit()

        elif "from wikipedia" in query:

            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Jarvis. Your deskstop Assistant")


if __name__ == '__main__':
    Take_query()
"""""
