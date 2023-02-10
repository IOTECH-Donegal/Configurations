
""""
Main routine for reading binary values from a serial port
Forked from the Comm module of SD-Node
Tested with Python >=3.8
By: JOR
    v0.1    14SEP20     First go!
"""

import serial
import sys

# Configure the first serial port, this should be the master GPS
# U-Blox connected directly should be ttyACM0
Serial_Port1 = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
Serial_Port1.flushInput()

# Main Loop
try:
    print("press [ctrl][c] at any time to exit...")
    while True:
        # Receive data from serial link 1
        read_buffer1 = Serial_Port1.readline()
        while len(read_buffer1) != 0:
            try:
                print(read_buffer1.hex())
                print(bytearray(read_buffer1))
            except Exception as error:
                print("Main loop error: ", sys.exc_info()[0])
            finally:
                read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')
except KeyboardInterrupt:
    print("\n" + "Caught keyboard interrupt, exiting")
    exit(0)
finally:
    print("Exiting Main Thread")
    exit(0)


