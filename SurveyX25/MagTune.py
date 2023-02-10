
""""
Main routine for Mag Tune
Forked from the Comm module of SD-Node
Tested with Python >=3.8
By: JOR
    v0.1    14SEP20     First go!
"""

import serial
import sys
import time

# Configure the first serial port, this should be the magnetometer
Serial_Port1 = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
Serial_Port1.flushInput()

time.sleep(3)

byte_array = b"\x24\x4d\x54\x2c\x30\x2c\x37\x2c\x30\x30\x30\x30\x2c\x9c\x0d\x0a"
Serial_Port1.write(byte_array)

try:
    print("press [ctrl][c] at any time to exit...")
    while True:
        # Receive data from serial link 1
        read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')
        while len(read_buffer1) != 0:
            try:
                current_line = str(read_buffer1)
                print('MAG:' + current_line.strip())
            except Exception as error:
                print("Main loop error: ", sys.exc_info()[0])
            finally:
                read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')

except KeyboardInterrupt:
    print("\n" + "Caught keyboard interrupt, exiting")
    exit(0)
finally:
    byte_array = b"\x24\x4d\x4f\x2c\x2c\x18\x0d\x0a"
    Serial_Port1.write(byte_array)
    print("Sent Mag Off command, exiting")
    exit(0)
