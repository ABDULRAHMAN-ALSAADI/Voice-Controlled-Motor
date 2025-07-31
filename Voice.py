import sys
import os
import json
import serial
from vosk import Model, KaldiRecognizer
import pyaudio

# ========== CONFIG ==========
model_path = "model"  # your vosk model folder
serial_port = "COM5"  # update to match your COM port
baud_rate = 9600      # match with Arduino
# ============================

# Init serial
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Load Vosk model
if not os.path.exists(model_path):
    print("Model not found!")
    sys.exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Start audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

print("🎙️ Say 'forward', 'stop', or 'backward'...")

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result.get("text", "").lower()
        print(f"🗣️ You said: {text}")

        if "forward" in text:
            ser.write(b'f\n')
        elif "stop" in text:
            ser.write(b's\n')
        elif "backward" in text:
            ser.write(b'b\n')

