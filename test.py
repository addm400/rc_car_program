import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

to_connect = []

for port, desc, hwid in sorted(ports):
    if 'Bluetooth' in desc:
        to_connect.append(port)

print(to_connect)