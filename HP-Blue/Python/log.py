from datetime import datetime
import sys
import serial

print('***** Logger2 *****')
print('Accepts NMEA data from a UBlox, and serial data from a strain gauge')
print('Saves with a date/time named logfile')

# Create the log file and open it
def logfilename():
    now = datetime.now()
    return 'NMEALogger-%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d.nmea' % \
                (now.year, now.month, now.day,
                 now.hour, now.minute, now.second)

# For UB2204
output_filename = "/home/johnoraw/Logfiles/" + logfilename()
output_file = open(output_filename, 'a', newline='')
print(f'Logging to {output_file}')

# Configure the first serial port, this should be the master GPS
# U-Blox connected directly should be ttyACM0

Serial_Port1 = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=True,
    dsrdtr=True,
    timeout=1
)
Serial_Port1.flushInput()

Serial_Port1.flushInput()

# Configure the second serial port
# A RS232-USB dongle should be ttyUSBx
Serial_Port2 = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=True,
    dsrdtr=True,
    timeout=.1
)
Serial_Port2.flushInput()

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
                print('GPS:' + current_line.strip())
            except Exception as error:
                print("Main GPS loop error: ", sys.exc_info()[0])
            finally:
                read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')

        # Receive data from serial link 2
        read_buffer2 = Serial_Port2.readline().decode('ascii', errors='replace')
        while len(read_buffer2) != 0:
            try:
                current_line = str(read_buffer2)
                # Log the data
                output_file.writelines(current_line)
                print('Gauge:' + current_line.strip())
            except Exception as error:
                print("Main Strain Gauge loop error: ", sys.exc_info()[0])
            finally:
                read_buffer2 = Serial_Port2.readline().decode('ascii', errors='replace')

except KeyboardInterrupt:
    print("\n" + "Caught keyboard interrupt, exiting")
    exit(0)
finally:
    print("Exiting Main Thread")
    exit(0)

