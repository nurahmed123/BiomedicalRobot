#include <Servo.h>

Servo servo;  // Create a servo object

void setup() {
  Serial.begin(9600);
  servo.attach(2);  // Attach the servo to pin 9
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();  // Read the angle from the Serial Monitor
    servo.write(angle);  // Set the servo position
    delay(1500);
  }
}
