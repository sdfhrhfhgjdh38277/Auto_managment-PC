import json
import webbrowser as web
import pyaudio
from vosk import Model, KaldiRecognizer

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
    if text == "браузер":
        web.open("google.com")
    if text == "стоп":
        print("стоп")
        quit()
    elif text == "привет":
        print("Hello")
