#include <Servo.h>
#include <Arduino.h>

const uint8_t VescOutputPin = 5;


Servo esc;

void setup() {
    esc.attach(VescOutputPin);
    esc.writeMicroseconds(1500); // Send "stop" signal to VESC
    Serial.begin(115200);
    Serial.begin(115200);
    Serial.println("VESC Control");
    delay(1900);
}

 void loop() {

  // ramp up to 0.5 throttle
    for (int i = 1500; i <= 1800; i+=50) {
        Serial.println(i);
        esc.writeMicroseconds(i);
        delay(1000);
    }

    // ramp down to stop
    for (int i = 1800; i >= 1500; i-=50) {
        Serial.println(i);
        esc.writeMicroseconds(i);
        delay(1000);
    }
}