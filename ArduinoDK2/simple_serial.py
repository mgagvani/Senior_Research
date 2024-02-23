import serial as serial

# Open the serial port
ser = serial.Serial('COM11', 115200, timeout=1)

while True:
    list_ = [[int(x) for x in input("steer throttle: ").split()]]
    list_ = list__ = list_[0]
    print(list_)

    list_ = [list_[0] + 65536 * list_[1], list_[0] + 65536 * list_[1]]

    number = list_[0]
    print(number, number%65536, number//65536)

    # Send the number (32-bit integer)
    string_to_send = f"{list__[0]},ii{list__[1]}\n"
    ser.writelines(string_to_send.encode())

    # read if anything comes
    while ser.in_waiting:
        print(ser.readline())
