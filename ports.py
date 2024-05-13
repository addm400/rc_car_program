import serial.tools.list_ports

"""
class for getting COM connections from PC 
and finding HC-05
version 1.0
"""


class Port:
    def __init__(self):
        self.ports = serial.tools.list_ports.comports()

    def scanner(self):
        to_connect = []
        for port, desc, hwid in sorted(self.ports):
            if '98D341F70297' in hwid:
                to_connect.append(port)
        return to_connect
    # 98D341F70297 number associated with HC-05


