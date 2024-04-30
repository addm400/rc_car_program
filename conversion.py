

class ConversionSys:
    def __init__(self):
        super().__init__()

        self.velocity = {
            "x_speed": 90,
            "y_speed": 90,
            "last_div_5": 0
        }

        self.axis_value = {"end_value": 98}

    def scale_check(self, scale):
        if scale == 1:
            self.axis_value["end_value"] = 98
        if scale == 1.5:
            self.axis_value["end_value"] = 158

    # function to convert values from tkinter canvas to carthesian coordinate system with start point at (0,0)
    def axis_conversion(self, coords, scale):

        self.scale_check(scale)

        self.velocity["x_speed"] = coords[0] - self.axis_value["end_value"]
        self.velocity["y_speed"] = (coords[1] - self.axis_value["end_value"]) * (-1)

        if scale == 1:
            return self.speed_data_conversion_100()
        if scale == 1.5:
            return self.speed_data_conversion_150()

    # function to convert units from axes (joystick) into real car control values
    def speed_data_conversion_100(self):

        if 15 < self.velocity["y_speed"] < 90:
            self.velocity["y_speed"] = 98 - self.velocity["y_speed"]
        elif -15 > self.velocity["y_speed"] > -90:
            self.velocity["y_speed"] = -self.velocity["y_speed"] + 90

        elif 15 >= self.velocity["y_speed"] >= 0:
            self.velocity["y_speed"] = 90
        elif -15 <= self.velocity["y_speed"] <= 0:
            self.velocity["y_speed"] = 90

        elif self.velocity["y_speed"] >= 90:
            self.velocity["y_speed"] = 10
        elif self.velocity["y_speed"] <= -90:
            self.velocity["y_speed"] = 170
        """
        1 część zrobiona aby przekształcić dane zebrane z osi Y
        na wartości odpowiadające sterowaniu mechanizmu micro servo
        ruch przód-tył, aktualny zakres: 10-170
        """

        if 15 <= self.velocity["x_speed"] <= 81:
            if self.velocity["x_speed"] % 5 == 0:
                self.velocity["last_div_5"] = 80 - self.velocity["x_speed"]
                self.velocity["x_speed"] = self.velocity["last_div_5"]
            else:
                self.velocity["x_speed"] = self.velocity["last_div_5"]
        elif -15 >= self.velocity["x_speed"] >= -81:
            if self.velocity["x_speed"] % 5 == 0:
                self.velocity["last_div_5"] = 60 - self.velocity["x_speed"]
                self.velocity["x_speed"] = self.velocity["last_div_5"]
            else:
                self.velocity["x_speed"] = self.velocity["last_div_5"]

        elif 15 > self.velocity["x_speed"] > -15:
            self.velocity["x_speed"] = 70

        elif self.velocity["x_speed"] > 81:
            self.velocity["x_speed"] = 0
        elif self.velocity["x_speed"] < -81:
            self.velocity["x_speed"] = 140
        """
        2 część zrobiona aby przekształcić dane zebrane z osi X
        na wartości odpowiadające sterowaniu silnika (krokowego)
        skręt kół lewo-prawo, aktualny zakres: 120 - 240 (stopni)
        """
        return self.velocity

    def speed_data_conversion_150(self):

        if 25 < self.velocity["y_speed"] < 158:
            self.velocity["y_speed"] = self.velocity["y_speed"] + 56
        elif -25 > self.velocity["y_speed"] > -158:
            self.velocity["y_speed"] = self.velocity["y_speed"] - 56

        elif 25 > self.velocity["y_speed"] >= 0:
            self.velocity["y_speed"] = 0
        elif -25 < self.velocity["y_speed"] <= 0:
            self.velocity["y_speed"] = 0

        elif self.velocity["y_speed"] >= 158:
            self.velocity["y_speed"] = 214
        elif self.velocity["y_speed"] <= -158:
            self.velocity["y_speed"] = -214
        """
        1 część zrobiona aby przekształcić dane zebrane z osi Y
        na wartości odpowiadające sterowaniu silnika (DC 3V/6V)
        ruch przód-tył, aktualny zakres: 92 - 208
        """

        if 25 < self.velocity["x_speed"] < 145:
            self.velocity["x_speed"] = int(self.velocity["x_speed"]/2) + 167
        elif -25 > self.velocity["x_speed"] > -145:
            self.velocity["x_speed"] = int(self.velocity["x_speed"]/2) + 193

        elif 25 >= self.velocity["x_speed"] >= -25:
            self.velocity["x_speed"] = 180

        elif self.velocity["x_speed"] > 145:
            self.velocity["x_speed"] = 240
        elif self.velocity["x_speed"] < -145:
            self.velocity["x_speed"] = 120
        """
        2 część zrobiona aby przekształcić dane zebrane z osi X
        na wartości odpowiadające sterowaniu silnika (krokowego)
        skręt kół lewo-prawo, aktualny zakres: 120 - 240 (stopni)
        """
        return self.velocity