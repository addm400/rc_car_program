
"""
Class made to convert values given by gui to
control values of a car
version 0.9
"""


class ConversionSys:
    def __init__(self):

        self.velocity = {
            "x_speed": 75,
            "y1_speed": 90,
            "y2_speed": 90,
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
        self.velocity["y1_speed"] = (coords[1] - self.axis_value["end_value"]) * (-1)

        if scale == 1:
            return self.speed_data_conversion_100()
        if scale == 1.25:
            return self.velocity
        if scale == 1.5:
            return self.speed_data_conversion_150()

    # function to convert units from axes (joystick) into real car control values
    def speed_data_conversion_100(self):

        if 15 < self.velocity["y1_speed"] < 90:
            self.velocity["y1_speed"] = 98 - self.velocity["y1_speed"]
        elif -15 > self.velocity["y1_speed"] > -90:
            self.velocity["y1_speed"] = -self.velocity["y1_speed"] + 90

        elif 15 >= self.velocity["y1_speed"] >= 0:
            self.velocity["y1_speed"] = 90
        elif -15 <= self.velocity["y1_speed"] <= 0:
            self.velocity["y1_speed"] = 90

        elif self.velocity["y1_speed"] >= 90:
            self.velocity["y1_speed"] = 10
        elif self.velocity["y1_speed"] <= -90:
            self.velocity["y1_speed"] = 170

        self.velocity["y2_speed"] = 180 - self.velocity["y1_speed"]
        """
        1st part is to transform the data collected from the Y axis
        to values corresponding to the control of the micro servo mechanism
        front-back movement, current range: 10-170
        """

        if 15 <= self.velocity["x_speed"] <= 81:
            if self.velocity["x_speed"] % 5 == 0:
                self.velocity["last_div_5"] = 85 - self.velocity["x_speed"]
                self.velocity["x_speed"] = self.velocity["last_div_5"]
            else:
                self.velocity["x_speed"] = self.velocity["last_div_5"]
        elif -15 >= self.velocity["x_speed"] >= -81:
            if self.velocity["x_speed"] % 5 == 0:
                self.velocity["last_div_5"] = 65 - self.velocity["x_speed"]
                self.velocity["x_speed"] = self.velocity["last_div_5"]
            else:
                self.velocity["x_speed"] = self.velocity["last_div_5"]

        elif 15 > self.velocity["x_speed"] > -15:
            self.velocity["x_speed"] = 75

        elif self.velocity["x_speed"] > 81:
            self.velocity["x_speed"] = 5
        elif self.velocity["x_speed"] < -81:
            self.velocity["x_speed"] = 145
        """
        2nd part is to transform the data collected from the X axis
        to values corresponding to the control of the micro servo mechanism
        left-right wheel rotation, current range: 5 - 145 (degrees)
        """
        return self.velocity

    def speed_data_conversion_150(self):

        if 28 <= self.velocity["y1_speed"] < 158:
            self.velocity["y1_speed"] = -int(self.velocity["y1_speed"]/2) + 90
        elif -28 >= self.velocity["y1_speed"] > -158:
            self.velocity["y1_speed"] = -int(self.velocity["y1_speed"]/2) + 90

        elif 28 > self.velocity["y1_speed"] >= 0:
            self.velocity["y1_speed"] = 90
        elif -28 < self.velocity["y1_speed"] <= 0:
            self.velocity["y1_speed"] = 90

        elif self.velocity["y1_speed"] >= 158:
            self.velocity["y1_speed"] = 10
        elif self.velocity["y1_speed"] <= -158:
            self.velocity["y1_speed"] = 170

        self.velocity["y2_speed"] = 180 - self.velocity["y1_speed"]
        """
        1st part is to transform the data collected from the Y axis
        to values corresponding to the control of the micro servo mechanism
        front-back movement, current range: 10-170
        """

        if 28 < self.velocity["x_speed"] < 158:
            self.velocity["x_speed"] = -int(self.velocity["x_speed"]/2) + 85
        elif -28 > self.velocity["x_speed"] > -158:
            self.velocity["x_speed"] = -int(self.velocity["x_speed"]/2) + 65

        elif 28 >= self.velocity["x_speed"] >= -28:
            self.velocity["x_speed"] = 75

        elif self.velocity["x_speed"] >= 158:
            self.velocity["x_speed"] = 5
        elif self.velocity["x_speed"] <= -158:
            self.velocity["x_speed"] = 145
        """
        2nd part is to transform the data collected from the X axis
        to values corresponding to the control of the micro servo mechanism
        left-right wheel rotation, current range: 5 - 145 (degrees)
        """
        return self.velocity
