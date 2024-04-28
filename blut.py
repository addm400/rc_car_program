from pyfirmata2 import Arduino, SERVO
import time


class Blut:
    def __init__(self):
        super().__init__()

        self.data = {
            "x": 180,
            "y": 91,
            "port": "COM6"
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
            self.data['connection_status'] = 1
        except:
            print("connection failed")
        else:
            print("*****CONNECTED*****")
            self.board_setup()

    def board_setup(self):
        pass
        self.board.digital[self.pin3].mode = SERVO

    def transmission(self, value):
        self.board.digital[self.pin3].write(value)






