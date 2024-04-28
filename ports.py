import serial.tools.list_ports


class Port:
    def __init__(self):
        super().__init__()
        self.ports = serial.tools.list_ports.comports()

    def scanner(self):
        to_connect = []
        for port, desc, hwid in sorted(self.ports):
            if 'Bluetooth' in desc:
                to_connect.append(port)
        return to_connect



