from pyfirmata2 import Arduino, SERVO


class Blut:
    def __init__(self):
        super().__init__()

        self.data = {
            "x": 180,
            "y": 91,
            "port": "COM4",
            "connected": 0
        }

        self.pin3 = 3
        self.board = None
        self.input_data = None  # dorzucić otrzymywanie informacji zwrotnej

    def define_port(self, port_value):
        self.data['port'] = port_value

    def start_connection(self):

        print("\n*****CONNECTING STARTED*****")
        self.board = Arduino(self.data['port'])

    def board_setup(self):
        pass
        self.board.digital[self.pin3].mode = SERVO

    def check_connection(self):
        return self.data['connected']

    def transmission(self, value):
        self.board.digital[self.pin3].write(value)





