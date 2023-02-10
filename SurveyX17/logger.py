# by: JOR
# Date: 30APR20
# Function: Logs serial data from 2 serial sources, forwards to SignalK or OpenCPN
# Script: logger.py

import serial
import socket
import sys
import threading

# Create a simple UDP socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Create global variables
output_file_name = 'home/pi/survey.log'

# Configure ports
serial1 = serial.Serial(port='/dev/ttyS0', baudrate=38400, timeout=1)


def handle_data(port_number, data):
    if len(data) > 0:
        print(data)
        data_bytes = bytearray()
        data_bytes.extend(map(ord, data))
        output_file = open(output_file_name, 'a', newline='')

        with output_file:
            output_file.write(data)
            output_file.close()
        try:
            my_socket.sendto(data_bytes, ("127.0.0.1", 10110))
        except socket.error as msg:
            sys.stderr.write('UDP socket warning: {}\n'.format(msg) + "\n")
        except Exception as error:
            print("UDP socket unexpected error:", sys.exc_info()[0])

def read_from_port_1(serial_port):
    while True:
        # Take in the serial data, ignore any errors
        try:
            data = serial1.readline().decode('utf-8', errors='replace')
            # print(data)
            handle_data(1, data)
        except:
            pass


thread1 = threading.Thread(target=read_from_port_1, args=(serial1,))
thread1.start()

