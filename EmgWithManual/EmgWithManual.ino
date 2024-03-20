#include <ESP32Servo.h>

// Define the pin for the button and the servo
const int buttonPin = 33;
const int moodSwitchingPin = 15;
const int servoPin = 14;
const int servoPin1 = 13;

bool useEmg = false;

// Create a Servo object
Servo myServo;
Servo myServo1;

// Variables to store the servo position and button state
int servoPosition = 0;
int buttonState;
int lastButtonState = LOW;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 10;

void setup() {
  // Attach the servo to its pin
  myServo.attach(servoPin);
  myServo1.attach(servoPin1);

  // Set button pin as INPUT
  pinMode(buttonPin, INPUT);
  pinMode(moodSwitchingPin, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  int menuSwitchStatus = digitalRead(moodSwitchingPin);
  // Serial.println(menuSwitchStatus);
  if (menuSwitchStatus == LOW) {
    delay(500);
    if (menuSwitchStatus == LOW) {
      useEmg ? useEmg = false : useEmg = true;
    }
  }
  Serial.println(useEmg);
  // Read the state of the button with debounce
  int reading = digitalRead(buttonPin);
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;

      // If the button is pressed, toggle the servo position
      if (buttonState == LOW) {
        toggleServoPosition();
        Serial.println("Single press");
      }
    }
  }

  // Store the current button state for comparison in the next iteration
  lastButtonState = reading;
}

void toggleServoPosition() {
  // Toggle the servo position between 0 and 180 degrees
  if (servoPosition == 0) {
    servoPosition = 180;
    Serial.println("hello");
  } else {
    servoPosition = 0;
    Serial.println("hi");
  }

  // Move the servo to the new position
  myServo.write(servoPosition);
  myServo1.write(servoPosition);
  delay(15);  // Give the servo some time to move
}
