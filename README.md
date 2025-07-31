# 🗣️🎛️ Voice Controlled Servo Motor (ESP32 + Python)

This project demonstrates how to control a servo motor connected to an ESP32 using voice commands through a Python script.
It uses local speech recognition and serial communication to interpret commands like forward, backward, and stop.

## 🚀 Features

- 🎙️ Voice-controlled operation (no cloud APIs)

- 🧠 Local speech recognition (using speech_recognition)

- 🔄 Serial communication with ESP32 via pyserial

- ⚙️ Real-time servo control

## 🧩 Components

- ESP32 Dev Board

- Servo Motor (e.g. SG90)

- Microphone (USB or laptop-integrated)

- Jumper wires + breadboard

## 🔌 Wiring (ESP32 → Servo)

| Servo Pin | ESP32 Pin |
| --------- | --------- |
| Signal    | D13       |
| VCC       | 5V        |
| GND       | GND       |

## 📦 Installation (Python Side)

```bash
pip install pyserial speechrecognition pyaudio
```
⚠️ For pyaudio on Windows, use:
```bash
pip install pipwin
pipwin install pyaudio
```

## 🧠 Arduino Code (ESP32)

Upload the following code to your ESP32 using Arduino IDE:

```cpp

#include <ESP32Servo.h>

Servo myServo;
char receivedChar;

void setup() {
  Serial.begin(9600);
  myServo.attach(13); // Servo connected to GPIO13
  myServo.write(0);   // Start at 0°
}

void loop() {
  if (Serial.available()) {
    receivedChar = Serial.read();
    Serial.print("Received: ");
    Serial.println(receivedChar);

    if (receivedChar == 'f') {
      myServo.write(90);  // Forward
    } else if (receivedChar == 's') {
      myServo.write(0);   // Stop
    } else if (receivedChar == 'b') {
      myServo.write(180); // Backward
    }
  }
}
```

## 🐍 Python Voice Control Script

```python
import speech_recognition as sr
import serial
import time

ser = serial.Serial("COM5", 9600)  # Use your correct COM port
time.sleep(2)

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("🎙️ Say something:")
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print(f"🔊 You said: {command}")

            if "forward" in command:
                ser.write(b'f')
                print("[→] Sent: forward")

            elif "backward" in command:
                ser.write(b'b')
                print("[←] Sent: backward")

            elif "stop" in command:
                ser.write(b's')
                print("[■] Sent: stop")

    except Exception as e:
        print("⚠️ Error:", e)
```

## 🛠️ Tips

- Make sure the Arduino Serial Monitor is closed before running the Python script.

- Only one program can access the serial port at a time.

- Test commands manually with ser.write(b'f') to confirm serial is working.

