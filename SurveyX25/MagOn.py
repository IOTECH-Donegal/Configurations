
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
import Constants

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

byte_array = b"\x24\x4d\x4d\x2c\x2c\x16\x0d\x0a"
Serial_Port1.write(byte_array)

try:
    print("press [ctrl][c] at any time to exit...")
    while True:
        # Receive data from serial link 1

        read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')
        nmea_full_sentence = str(read_buffer1)
        while len(read_buffer1) != 0:
            try:
                # Break it up into fields
                list_of_values = nmea_full_sentence.split(',')
                # Process the mag value and assign it to a property
                total_field_hex = list_of_values[2]
                total_field_raw = int(total_field_hex, 16)
                total_field = total_field_raw / Constants.FieldConversion
                print('MAG: ', total_field)
            except ZeroDivisionError:
                print('MAG: 0')
            except Exception as error:
                print("Main loop error: ", sys.exc_info()[0])
            finally:
                read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')

except KeyboardInterrupt:
    print("\n" + "Caught keyboard interrupt, exiting")
    exit(0)
finally:
    #byte_array = b"\x24\x4d\x4f\x2c\x2c\x18\x0d\x0a"
    #Serial_Port1.write(byte_array)
    print("Sent Mag Off command, exiting")
    exit(0)
