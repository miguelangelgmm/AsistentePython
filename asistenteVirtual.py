import datetime
import pyttsx3
import pywhatkit
import speech_recognition as sr
import keyboard
import time
import os
import wikipedia

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
    Permite escuchar por micrófono, retorna la frase escuchada si decimos el nomber de maria
    """
    audioTxt = ""
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
            else:
                audioTxt = ""
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


def reproducirYtbe(video):
    """
    @param video: reproduce el video dicho en youtube
    """
    cancion = video.replace("reproduce", "")
    hablar(video.replace("reproduce", "reproduciendo"))
    pywhatkit.playonyt(cancion)
    time.sleep(5)
    keyboard.send("space")


def decirHora():
    """
    Dice la hora en la que nos encontramos
    """
    hora = datetime.datetime.now().strftime("%I:%M %p")
    hablar("Son las: " + hora)


def buscarWiki(palabra):
    """
    Dice los dos primeros párrafos de una palabra en la wikipedia
    @param palabra: palabra buscada
    """
    palabra = palabra.replace("wikipedia", "")
    wikipedia.set_lang("es")
    informacion = wikipedia.summary(palabra, 2)
    hablar(informacion)


def decirDia():
    """
    Función que permite saber en que dia nos encontramos
    @return: Día de la semana
    """
    #obtenemos el dia actual de forma numérica
    dia = datetime.datetime.today().weekday() + 1
    #Creamos un diccionario con los dias de la mana
    semana = {1: 'Lunes', 2: 'Martes',
              3: 'Miercoles', 4: 'Jueves',
              5: 'Viernes', 6: 'Sábado',
              7: 'Domingo'}

    return semana[dia]


def accion():
    """
    Función que va a ejecutar una orden dependiendo de la opción solicitada
    """

    salida = True
    while salida:
        try:
            opcion = escuchar()
        except UnboundLocalError:
            continue
        if "reproduce" in opcion:
            reproducirYtbe(opcion)
        elif "hora" in opcion:
            decirHora()
        elif "wikipedia" in opcion:
            buscarWiki(opcion)
        elif "finaliza" in opcion:
            salida = False
            hablar("Espero que pase un buen dia")
        elif "apaga" in opcion:
            os.system("shutdown /s /t 60")
            hablar("El ordenador se apagara en un minuto")
        elif "cancela" in opcion:
            os.system("shutdown -a")
            hablar("Se ha cancelado el apagado")
        elif "día" in opcion:
            hablar("El día de la semana es " + decirDia())
        elif opcion == "":
            # Si el usuario no dice el nombre de maria no hacemos nada
            continue
        else:
            hablar("No te he entendido bien")


if __name__ == '__main__':
    hablar("Buenos dias yo soy maria tu asistenta personal")
    accion()
