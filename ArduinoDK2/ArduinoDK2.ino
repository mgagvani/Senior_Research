#include "SerialTransfer.h"
#include <Servo.h>

#define STEER_PIN 9
#define THROTTLE_PIN 5

#define LED_PIN 13 // Onboard LED

Servo steer;
Servo throttle;

String inputString = "";
String inputSteer = "";
String inputThrottle = "";

void setup()
{
    Serial.begin(115200);

    steer.attach(STEER_PIN);
    throttle.attach(THROTTLE_PIN);

    steer.writeMicroseconds(1500);
    throttle.writeMicroseconds(1500);

    // digital output for LED
    pinMode(LED_PIN, OUTPUT);
}

void loop()
{
    // recieve ****,****\n -> bytes = 10
    if (Serial.available() > 10)
    {   
        delay(2); // allow time for buffer to fill

        // receive 
        inputString = Serial.readStringUntil('\n');

        // extract steer and throttle values
        int commaIndex = inputString.indexOf(',');
        inputSteer = inputString.substring(0, commaIndex);
        inputThrottle = inputString.substring(commaIndex + 1);

        // convert to 32-bit number
        uint16_t steerVal = inputSteer.toInt();
        uint16_t throttleVal = inputThrottle.toInt();

        Serial.println("Steer: " + String(steerVal) + " Throttle: " + String(throttleVal));

        // actuate
        steer.writeMicroseconds(steerVal);
        throttle.writeMicroseconds(throttleVal);
    }
}