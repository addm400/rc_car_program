

class ConversionSys:
    def __init__(self):
        super().__init__()

        self.velocity = {
            "x_speed": 180,
            "y_speed": 0
        }

    def axis_conversion(self, coords):
        if coords[0] < 98:
            self.velocity["x_speed"] = coords[0] - 97
        if coords[0] > 98:
            self.velocity["x_speed"] = coords[0] - 98
        if coords[0] == 98:
            self.velocity["x_speed"] = 0

        if coords[1] < 98:
            self.velocity["y_speed"] = -coords[1] + 97
        if coords[1] > 98:
            self.velocity["y_speed"] = -(coords[1] - 98)
        if coords[1] == 98:
            self.velocity["y_speed"] = 0
