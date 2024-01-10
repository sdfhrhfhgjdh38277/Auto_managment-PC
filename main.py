import sys
import webbrowser

import pyttsx3 as pt
import speech_recognition as sr


def listen(word: str):
    engine = pt.init()
    engine.say(word)
    engine.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Я вас слушаю.")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio).lower()
        print(f"Вы сказали: {task}")
    except sr.UnknownValueError:
        listen("Я не раслышала что вы сказали.")
        task = command()
    return task


def makesomeshing(task):
    if "открой сайт" in task:
        listen("Выполняю")
        url = "https://google.com"
        webbrowser.open(url)
    elif "стоп" in task:
        listen("Без проблем. Если понадоблюсь - зовите")
        sys.exit()
    elif "имя" in task:
        listen("Меня зовут Энди")


while True:
    makesomeshing(command())
