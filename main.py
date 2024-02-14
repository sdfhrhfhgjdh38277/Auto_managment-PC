import json
import webbrowser as web

import pyaudio
import pyttsx3 as pyt
from vosk import Model, KaldiRecognizer

pye = pyt.init()
model = Model(r"voice_model")
recognize = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000
)
stream.start_stream()


def listen():
    while True:
        data = stream.read(80000, exception_on_overflow=False)
        if recognize.AcceptWaveform(data) or len(data) > 0:
            answer = json.loads(recognize.Result())
            if answer["text"]:
                yield answer["text"]


for text in listen():
    print(text)
    if text == "браузер":
        pye.say("Открываю.")
        pye.runAndWait()
        web.open("google.com")
    if text == "стоп":
        pye.say("Выключаюсь. ")
        pye.runAndWait()
        quit()
    elif text == "привет":
        pye.say("Чем могу помочь? ")
        pye.runAndWait()
