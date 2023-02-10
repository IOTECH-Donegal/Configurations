
""""
Main routine for Mag Test
Forked from the Comm module of SD-Node
Tested with Python >=3.8
By: JOR
    v0.1    14SEP20     First go!
"""

import serial
import sys

# Configure the first serial port, this should be the magnetometer
Serial_Port1 = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=True,
    dsrdtr=True,
    timeout=1
)
Serial_Port1.flushInput()

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
    print("Exiting Main Thread")
    exit(0)
