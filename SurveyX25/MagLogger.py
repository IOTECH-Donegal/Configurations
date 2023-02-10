""""
Main routine for Mag Logger
Forked from the Comm module of SD-Node
Tested with Python >=3.8
By: JOR
    v0.1    14SEP20     First go!
"""

import serial
import sys
import time
import Constants

# Create the log file and open it
output_filename = "survey.log"
output_file = open(output_filename, 'a', newline='')

print("Opening port to MAG")
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

print("Opening port to GPS")
# Configure the second serial port
# A RS232-USB dongle should be ttyUSB1 with a UBlox PPP
Serial_Port2 = serial.Serial(
    # port='COM11',
    port='/dev/ttyUSB1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=.1
)
Serial_Port2.flushInput()

print("Starting Mag")
time.sleep(3)
byte_array = b"\x24\x4d\x4d\x2c\x2c\x16\x0d\x0a"
Serial_Port1.write(byte_array)

# Main Loop
try:
    print("press [ctrl][c] at any time to exit...")
    while True:
        # Receive data from serial link 1
        read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')
        while len(read_buffer1) != 0:
            try:
                current_line = str(read_buffer1)
                # Log the data
                output_file.writelines(current_line)
                print('MAG:' + current_line.strip())
            except Exception as error:
                print("Main loop error: ", sys.exc_info()[0])
            finally:
                read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')

        # Receive data from serial link 2
        read_buffer2 = Serial_Port2.readline().decode('ascii', errors='replace')
        while len(read_buffer2) != 0:
            try:
                current_line = str(read_buffer2)
                # Log the data
                output_file.writelines(current_line)
                print('GPS:' + current_line.strip())
            except Exception as error:
                print("Main loop error: ", sys.exc_info()[0])
            finally:
                read_buffer2 = Serial_Port2.readline().decode('ascii', errors='replace')

except KeyboardInterrupt:
    print("\n" + "Caught keyboard interrupt, exiting")
    exit(0)
finally:
    byte_array = b"\x24\x4d\x4f\x2c\x2c\x18\x0d\x0a"
    Serial_Port1.write(byte_array)
    print("Sent Mag Off command, exiting")
    exit(0)
