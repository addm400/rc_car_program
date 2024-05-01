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
        self.pin5 = 5
        self.pin6 = 6
        self.board = None
        self.input_data = None  # dorzucić otrzymywanie informacji zwrotnej

    def define_port(self, port_value):
        self.data['port'] = port_value

    def start_connection(self):
        self.board = Arduino(self.data['port'])

    def board_setup(self):
        self.board.digital[self.pin3].mode = SERVO
        self.board.digital[self.pin5].mode = SERVO
        self.board.digital[self.pin6].mode = SERVO

    def check_connection(self):
        return self.data['connected']

    def transmission(self, x_value, y1_value, y2_value):
        self.board.digital[self.pin3].write(x_value)
        self.board.digital[self.pin5].write(y1_value)
        self.board.digital[self.pin6].write(y2_value)





