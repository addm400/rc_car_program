from pyfirmata2 import Arduino, SERVO
import time


class Blut:
    def __init__(self):
        super().__init__()

        self.data = {
            "x": 180,
            "y": 91,
            "port": "COM3",
            "connected": 0
        }

        self.pin3 = 3
        self.board = None
        self.input_data = None  # dorzucić otrzymywanie informacji zwrotnej

    def define_port(self, port_value):
        self.data['port'] = port_value

    def start_connection(self):
        print("\n*****CONNECTING STARTED*****")
        try:
            self.board = Arduino(self.data['port'])
            self.board.analog[0].read()  # to jest chyba lekarstwo na problemy z wykrywaniem płytki
        except:
            print("connection failed")
        else:
            print("*****CONNECTED*****")
            self.data['connected'] = 1
            self.board_setup()

    def board_setup(self):
        pass
        self.board.digital[self.pin3].mode = SERVO

    def check_connection(self):
        return self.data['connected']

    def transmission(self, value):
        self.board.digital[self.pin3].write(value)






