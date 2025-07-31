#include <ESP32Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(5);
  Serial.println("ESP32 Ready!");
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    Serial.print("Got command: ");
    Serial.println(command);

    if (command == 'f') {
      myServo.write(180);
    } else if (command == 's') {
      myServo.write(90);
    } else if (command == 'b') {
      myServo.write(0);
    }
  }
}
