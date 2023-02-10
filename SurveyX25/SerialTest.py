""""
Main routine for Serial Mux
Forked from the Comm module of SD-Node
Tested with Python >=3.8
By: JOR
    v0.1    14SEP20     First go!
"""

import sys
import socket
import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for p in ports:
    print('Name:', p.name)
    print('Device:', p.device)
    print('Description:', p.description)
    print('Location:', p.location)
    print('Manufacturer:', p.manufacturer)
    print('Product:', p.product)
    print('HWID:', p.hwid)
    print('VID:', p.vid)
    print('PID:', p.pid)
    print('Serial Number:', p.serial_number)
    print()
print(len(ports), ' ports found')

exit(0)
