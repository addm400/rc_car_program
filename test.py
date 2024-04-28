import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    if 'Bluetooth' in desc:
        print("{}: {}".format(port, desc))