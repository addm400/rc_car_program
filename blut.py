from pyfirmata2 import Arduino, SERVO
import time


class Blut:
    def __init__(self):
        super().__init__()

        self.data = {
            "x": 180,
            "y": 90,
            "port": "0"
        }

        self.pin3 = 3
        self.board = None
        self.input_data = None  # dorzucić otrzymywanie informacji zwrotnej

    def define_port(self, port_value):
        self.data['port'] = port_value

    def start_connection(self):
        print("\n*****CONNECTION STARTED*****")
        self.board = Arduino(self.data['port'])
        for i in range(3):
            for j in range(3):
                print('.', end="")
                time.sleep(0.5)
            print("")
            time.sleep(0.5)
        print("*****CONNECTED*****")
        time.sleep(1)
        self.board_setup()

    def board_setup(self):
        pass
        self.board.digital[self.pin3].mode = SERVO

    def transmission(self):

        for i in range(5):
            speed = 90
            for j in range(8):
                self.board.digital[self.pin3].write(speed)
                speed = speed - 10
                print(speed)
                time.sleep(0.5)


bluczus = Blut()
bluczus.define_port("COM6")
bluczus.start_connection()
bluczus.transmission()
print('done')

