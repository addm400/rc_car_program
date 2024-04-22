import serial
import time


class Blut:
    def __init__(self):
        super().__init__()

        self.data = {
            "x_speed": 180,
            "y_speed": 0,
            "port": "0"
        }

        self.blueooth = None
        self.input_data = None

    def define_port(self, port_value):
        self.data['port'] = port_value

    def start_connection(self):
        print("\n*****CONNECTION STARTED*****")
        self.blueooth = serial.Serial(self.data['port'], 9600)
        for i in range(3):
            for j in range(3):
                print('.', end="")
                time.sleep(0.5)
            print("")
            time.sleep(0.5)
        print("*****CONNECTED*****")
        time.sleep(1)

    def transmission(self):

        while True:
            self.blueooth.write(str.encode(str(self.data['x_speed'])) + b", "
                                + str.encode(str(self.data['y_speed'])))

            self.input_data = self.blueooth.readline()
            print(self.input_data.decode())
            time.sleep(0.01)


bluczus = Blut()
bluczus.define_port("COM6")
bluczus.start_connection()
bluczus.transmission()




