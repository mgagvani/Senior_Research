// sweep servo from left to right

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.writeMicroseconds(1500); // Send "stop" signal to servo
}

// use writeMicroseconds to control the speed of the servo
void loop() {
    for (int i = 1000; i <= 2000; i += 100) {
        myservo.writeMicroseconds(i);
        delay(1000);
    }
    for (int i = 2000; i >= 1000; i -= 100) {
        myservo.writeMicroseconds(i);
        delay(1000);
    }
}