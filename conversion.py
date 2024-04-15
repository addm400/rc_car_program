

class ConversionSys:
    def __init__(self):
        super().__init__()

        self.velocity = {
            "x_speed": 180,
            "y_speed": 0
        }

        self.axis_value = {"end_value": 98}

    def scale_check(self, scale):
        if scale == 1:
            self.axis_value["end_value"] = 98
        if scale == 1.5:
            self.axis_value["end_value"] = 98

    def axis_conversion(self, coords, scale):

        self.scale_check(scale)

        if coords[0] < self.axis_value["end_value"]:
            self.velocity["x_speed"] = coords[0] - self.axis_value["end_value"]
        if coords[0] > self.axis_value["end_value"]:
            self.velocity["x_speed"] = coords[0] - self.axis_value["end_value"]
        if coords[0] == self.axis_value["end_value"]:
            self.velocity["x_speed"] = 0

        if coords[1] < self.axis_value["end_value"]:
            self.velocity["y_speed"] = -coords[1] + self.axis_value["end_value"]
        if coords[1] > self.axis_value["end_value"]:
            self.velocity["y_speed"] = -(coords[1] - self.axis_value["end_value"])
        if coords[1] == self.axis_value["end_value"]:
            self.velocity["y_speed"] = 0

        if scale == 1:
            return self.speed_data_conversion()
        if scale == 1.5:
            return self.speed_data_conversion()

    # function to convert units from axes (joystick) into real car control values
    def speed_data_conversion(self):

        if 15 < self.velocity["y_speed"] < 85:
            self.velocity["y_speed"] = 2*self.velocity["y_speed"] + 44
        elif -15 > self.velocity["y_speed"] > -85:
            self.velocity["y_speed"] = 2*self.velocity["y_speed"] - 44

        elif 15 > self.velocity["y_speed"] >= 0:
            self.velocity["y_speed"] = 0
        elif -15 < self.velocity["y_speed"] <= 0:
            self.velocity["y_speed"] = 0

        elif self.velocity["y_speed"] > 85:
            self.velocity["y_speed"] = 214
        elif self.velocity["y_speed"] < -85:
            self.velocity["y_speed"] = -214
        """
        1 część zrobiona aby przekształcić dane zebrane z osi Y
        na wartości odpowiadające sterowaniu silnika (DC 3V/6V)
        ruch przód-tył, aktualny zakres: 92 - 208
        """

        if 15 < self.velocity["x_speed"] < 81:
            self.velocity["x_speed"] = self.velocity["x_speed"] + 165
        elif -15 > self.velocity["x_speed"] > -81:
            self.velocity["x_speed"] = self.velocity["x_speed"] + 195

        elif 15 > self.velocity["x_speed"] > -15:
            self.velocity["x_speed"] = 180

        elif self.velocity["x_speed"] > 81:
            self.velocity["x_speed"] = 240
        elif self.velocity["x_speed"] < -81:
            self.velocity["x_speed"] = 120
        """
        2 część zrobiona aby przekształcić dane zebrane z osi X
        na wartości odpowiadające sterowaniu silnika (krokowego)
        skręt kół lewo-prawo, aktualny zakres: 120 - 240 (stopni)
        """
        return self.velocity
