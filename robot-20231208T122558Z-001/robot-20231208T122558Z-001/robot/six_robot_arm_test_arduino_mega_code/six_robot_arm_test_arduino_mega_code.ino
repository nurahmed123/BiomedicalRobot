#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
  servo1.attach(3);
  servo2.attach(4);
  servo3.attach(5);
  servo4.attach(6);
  servo5.attach(7);
servo1.write(90);
servo2.write(90);
servo3.write(90);
servo4.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    int angle;
    Serial.print(command);
    Serial.print("  ");
    switch (command) {
      case '1':
        angle = Serial.parseInt();
        Serial.println(angle);
        servo1.write(angle);
        break;

      case '2':
        angle = Serial.parseInt();
        Serial.println(angle);
        servo2.write(angle);
        break;

      case '3':
        angle = Serial.parseInt();
        Serial.println(angle);
        servo3.write(angle);
        break;

      case '4':
        angle = Serial.parseInt();
        Serial.println(angle);
        servo4.write(angle);
        break;

      case '5':
        angle = Serial.parseInt();
        Serial.println(angle);
        servo5.write(angle);
        break;
    }
    //delay(2);
  }
}
