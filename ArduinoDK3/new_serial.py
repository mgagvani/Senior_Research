import serial as serial

ser = serial.Serial('COM11', 115200, timeout=1)

while True:
    list_ = [int(x) for x in input("steer throttle: ").split()]

    # send message <hello, steer, throttle>
    # just like over serial console terminal
    msg = f"<hello, {list_[0]}, {list_[1]}>"
    ser.write(msg.encode())
