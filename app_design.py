import customtkinter
import tkinter
from tkinter import *
import os
from PIL import Image

"""
Main file for RC control car program 
"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("RC car control panel")
        self.geometry("800x500")
        self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "icon.png")), size=(45, 30))
        self.home_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "home_pic.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "keyboard_pic.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "joystick_pic.png")), size=(20, 20))
        self.keyboard_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "strzalki.png")), size=(251, 242))
        self.board = customtkinter.CTkImage(Image.open(os.path.join(image_path, "plansza.png")), size=(280, 280))
        self.analog = customtkinter.CTkImage(Image.open(os.path.join(image_path, "kolko.png")), size=(50, 50))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Control Panel", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Keyboard",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Joystick",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # create textbox/consol no 1
        self.console1position = 5.0
        self.textbox1 = customtkinter.CTkTextbox(self, width=360, height=50)
        self.textbox1.grid(row=0, column=1, padx=(20, 12), pady=(330, 20), sticky="nsew")
        self.textbox1.insert("0.0", "Console\n\n" + "Some info.\n\n")

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.keyboard_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.keyboard_image)
        self.keyboard_image_label.grid(row=0, column=1, padx=(20, 0), pady=(0, 0))

        self.label_tab_2 = customtkinter.CTkLabel(self.second_frame, text="W – MOVE FORWARD\n" +
                                                                          "S – MOVE BACKWARD\n" +
                                                                          "A – TURN LEFT \n" +
                                                                          "D – TURN RIGHT")
        self.label_tab_2.grid(row=1, column=1, padx=(20, 20), pady=(0, 8))

        # create textbox/console no 2
        self.console2position = 5.0
        self.textbox2 = customtkinter.CTkTextbox(self.second_frame, width=569, height=150)
        self.textbox2.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(20, 0))
        self.textbox2.insert("0.0", "Console\n\n" + "Some info.\n\n")

        # radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self.second_frame)
        self.radiobutton_frame.grid(row=0, column=2, rowspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Speed Control", font=customtkinter.CTkFont(size=20))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=(70, 0), pady=(50, 20), sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,
                                                           text="30% of MAX SPEED", font=customtkinter.CTkFont(size=13), command=self.radio_button_1)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=(70, 0), sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,
                                                           text="60% of MAX SPEED", font=customtkinter.CTkFont(size=13), command=self.radio_button_2)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=(70, 0), sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2,
                                                           text="100% of MAX SPEED", font=customtkinter.CTkFont(size=13), command=self.radio_button_3)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=(76, 0), sticky="n")

        # create third frame

        self.canvas_height = 275
        self.canvas_width = 110
        self.dragInfo_x = 0
        self.dragInfo_y = 0
        self.coordinates = []

        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.joystick_board = Canvas(self.third_frame, width=self.canvas_width, height=self.canvas_height)
        self.joystick_board.grid(row=0, column=0, pady=(20, 0), padx=(20, 140), sticky="nsew")

        self.bgphoto = PhotoImage(file='test_images//plansza.png')
        self.plansza = self.joystick_board.create_image(0, 0, image=self.bgphoto, anchor=NW)

        self.photoimage = PhotoImage(file='test_images//kontroler.png')
        self.joystick_steering_label = self.joystick_board.create_image(0, 0, image=self.photoimage, anchor=NW)
        self.joystick_board.moveto(self.joystick_steering_label, 115, 115)

        self.joystick_height = self.photoimage.height()
        self.joystick_width = self.photoimage.width()

        self.joystick_board.tag_bind(self.joystick_steering_label, "<Button-1>", self.drag_start)
        self.joystick_board.tag_bind(self.joystick_steering_label, "<B1-Motion>", self.drag_motion)
        self.joystick_board.tag_bind(self.joystick_steering_label, "<ButtonRelease-1>", self.dropped)

        # create textbox/consol no 3
        self.console3position = 5.0
        self.textbox3 = customtkinter.CTkTextbox(self.third_frame, width=569, height=150)
        self.textbox3.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(30, 20), sticky="nsew")
        self.textbox3.insert("0.0", "Console\n\n" + "Some info.\n\n")

        # select default frame
        self.select_frame_by_name("home")

        """Car control"""
        # initial speed value of a car
        self.current_speed = [62]

        # tab for holding speed data which will be sent to the car
        self.speed_data = [180, 0]

        # binding key press and release
        self.bind('<Key>', self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        # starting periodic function to pass data
        #self.alarm = self.after(100, self.printer)

        # tab for holding which window is currently displayed (1/2/3)
        self.which_window = [1]

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "keyboard" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "joystick" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "keyboard":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "joystick":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")
        self.which_window[0] = 1

    def frame_2_button_event(self):
        self.select_frame_by_name("keyboard")
        self.which_window[0] = 2

    def frame_3_button_event(self):
        self.select_frame_by_name("joystick")
        self.which_window[0] = 3

    def radio_button_1(self):
        self.current_speed[0] = 62
        self.textbox2.insert(index=self.console2position, text="30% of maximum car speed is set.\n\n")
        self.console2position += 2

    def radio_button_2(self):
        self.current_speed[0] = 124
        self.textbox2.insert(index=self.console2position, text="60% of maximum car speed is set.\n\n")
        self.console2position += 2

    def radio_button_3(self):
        self.current_speed[0] = 205
        self.textbox2.insert(index=self.console2position, text="100% of maximum car speed is set.\n\n")
        self.console2position += 2

    # wracanie joysticka na środek układu

    def drag_start(self, event):
        self.coordinates = self.joystick_board.coords(self.joystick_steering_label)
        self.x_pos = event.x
        self.y_pos = event.y

    # złapanie obiektu myszką

    def drag_motion(self, event):
        win_x = event.x
        win_y = event.y

        x = self.coordinates[0] - self.x_pos + event.x
        y = self.coordinates[1] - self.y_pos + event.y

        if x < 0:
            x = 0

        elif x > 250:
            x = 250

        else:
            self.x_pos = win_x

        if y < 0:
            y = 0

        elif y > 250:
            y = 250

        else:
            self.y_pos = win_y

        # obsługa przesuwania obiektu w naszym układzie wspl
        self.joystick_board.moveto(self.joystick_steering_label, x, y)
        self.coordinates = self.joystick_board.coords(self.joystick_steering_label)
        print(self.coordinates)

        #self.speed_data[0] = x-162
        #self.speed_data[1] = (y-135)*(-1)
        #self.speed_data_conversion()
        """moze trzeba dodać zabezpieczenie że jeżeli za mocno przeciągniemy to joystick wraca do jakiejs pozcyji"""

    def dropped(self, event):

        self.joystick_board.moveto(self.joystick_steering_label, 115, 115)

        self.speed_data[0] = 180
        self.speed_data[1] = 0

    def key_press(self, event):
        if self.which_window[0] == 2:
            if event.char == "w":
                self.speed_data[1] = self.current_speed[0]
            elif event.char == "s":
                self.speed_data[1] = -self.current_speed[0]
            elif event.char == "a":
                self.speed_data[0] = 140
            elif event.char == "d":
                self.speed_data[0] = 220

    def key_release(self, event):

        if self.which_window[0] == 2:
            if event.char == "w":
                self.speed_data[1] = 0
            elif event.char == "s":
                self.speed_data[1] = 0
            elif event.char == "a":
                self.speed_data[0] = 180
            elif event.char == "d":
                self.speed_data[0] = 180

    """periodic function for sending/printing data which control the car"""
    def printer(self):
        print(self.speed_data)
        self.alarm = self.after(10, self.printer)

    # function to convert units from axes (joystick) into real car control values
    def speed_data_conversion(self):

        if 11 < self.speed_data[1] < 71:
            self.speed_data[1] = 2 * self.speed_data[1] + 68
        elif -11 > self.speed_data[1] > -71:
            self.speed_data[1] = 2 * self.speed_data[1] - 68

        elif 11 > self.speed_data[1] >= 0:
            self.speed_data[1] = 0
        elif -11 < self.speed_data[1] <= 0:
            self.speed_data[1] = 0

        elif self.speed_data[1] > 71:
            self.speed_data[1] = 208
        elif self.speed_data[1] < -71:
            self.speed_data[1] = -208
        """
        1 część zrobiona aby przekształcić dane zebrane z osi Y
        na wartości odpowiadające sterowaniu silnika (DC 3V/6V)
        ruch przód-tył, aktualny zakres: 92 - 208
        """

        if 11 < self.speed_data[0] < 71:
            self.speed_data[0] = self.speed_data[0] + 169
        elif -11 > self.speed_data[0] > -71:
            self.speed_data[0] = self.speed_data[0] + 191

        elif 11 > self.speed_data[0] > -11:
            self.speed_data[0] = 180

        elif self.speed_data[0] > 71:
            self.speed_data[0] = 240
        elif self.speed_data[0] < -71:
            self.speed_data[0] = 120
        """
        2 część zrobiona aby przekształcić dane zebrane z osi X
        na wartości odpowiadające sterowaniu silnika (krokowego)
        skręt kół lewo-prawo, aktualny zakres: 120 - 240 (stopni)
        """


