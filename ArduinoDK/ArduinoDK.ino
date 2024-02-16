#include "SerialTransfer.h"
#include <Servo.h>

#define STEER_PIN 9
#define THROTTLE_PIN 5

#define LED_PIN 13 // Onboard LED

SerialTransfer myTransfer;

Servo steer;
Servo throttle;

uint16_t data[2] = {1500, 1500};


void setup()
{
    Serial.begin(115200);
    myTransfer.begin(Serial);

    steer.attach(STEER_PIN);
    throttle.attach(THROTTLE_PIN);

    steer.writeMicroseconds(1500);
    throttle.writeMicroseconds(1500);

    // digital output for LED
    pinMode(LED_PIN, OUTPUT);
}

void loop()
{
    if (myTransfer.available())
    {   
        // recieve
        uint16_t recSize = 0;
        recSize = myTransfer.rxObj(data, recSize);

        // send all received data back to Python
        uint16_t sendSize = sizeof(data);
        for (uint16_t i = 0; i < recSize; i++)
            sendSize = myTransfer.txObj(data, sendSize);
        myTransfer.sendData(sendSize);

        // actuate
        steer.writeMicroseconds(data[0]);
        throttle.writeMicroseconds(data[1]);

        // debug
        if (data[1] > 1000) {
            analogWrite(LED_PIN, map(data[1], 1000, 2000, LOW, HIGH));
        }
        else {
            digitalWrite(LED_PIN, LOW);
        }
    }
}