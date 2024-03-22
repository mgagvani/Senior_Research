import serial as serial
import time

ser = serial.Serial('COM11', 115200, timeout=1)

'''
while True:
    list_ = [int(x) for x in input("steer throttle: ").split()]

    # send message <hello, steer, throttle>
    # just like over serial console terminal
    msg = f"<hello, {list_[0]}, {list_[1]}>"
    ser.write(msg.encode())
'''
while True:
    for i in range(1000, 2000, 50):
        ser.read(ser.in_waiting)
        ser.write(f"<hello, {i}, 1500>".encode())
        ser.flush()
        time.sleep(0.1)
        print(i)

    for i in range(2000, 1000, -50):
        ser.read(ser.in_waiting)
        ser.write(f"<hello, {i}, 1500>".encode())
        ser.flush()
        time.sleep(0.1)
        print(i)
