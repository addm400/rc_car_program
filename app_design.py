import customtkinter
import tkinter
from tkinter import *
import os
from PIL import Image

"""
Now this project is using Git as version control unit
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

        self.console1position = 5.0  # zastanowić się czy nie dodać tutaj self
        self.console2position = 5.0
        self.console3position = 5.0

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

        # create textbox no 1
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

        # create textbox no 2
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
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.joystick_steering_label = customtkinter.CTkLabel(self.third_frame, image=self.board, text="")
        self.joystick_steering_label = customtkinter.CTkLabel(self.third_frame, image=self.board,  text="")
        self.joystick_steering_label.grid(row=0, column=0, pady=(20, 0), padx=(0, 140), sticky="nsew")
        self.joystick_steering_label = customtkinter.CTkLabel(self.third_frame, image=self.analog, text="")
        self.joystick_steering_label.place(x=162, y=135)

        self.joystick_steering_label.bind("<Button-1>", self.drag_start)
        self.joystick_steering_label.bind("<B1-Motion>", self.drag_motion)
        self.joystick_steering_label.bind("<ButtonRelease-1>", self.dropped)

        self.speed_data = [180, 0]

        # create textbox no 3
        self.textbox3 = customtkinter.CTkTextbox(self.third_frame, width=569, height=150)
        self.textbox3.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(30, 20), sticky="nsew")
        self.textbox3.insert("0.0", "Console\n\n" + "Some info.\n\n")

        # select default frame
        self.select_frame_by_name("home")

        """key control section"""

        self.bind('<Key>', self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        self.alarm = self.after(100, self.printer)
        # wydruk wartości sterowanych samochodu

        self.current_speed = [62]
        # wartość początkowa prędkości

        self.which_window = [1]
        # okno home otwiera się jako pierwsze przyjmuje wartości 1, 2, 3

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
        self.joystick_steering_label.startX = event.x
        self.joystick_steering_label.startY = event.y
    # złapanie obiektu myszką

    def drag_motion(self, event):

        x = self.joystick_steering_label.winfo_x() - self.joystick_steering_label.startX + event.x
        y = self.joystick_steering_label.winfo_y() - self.joystick_steering_label.startY + event.y
        # obsługa przesuwania obiektu w naszym układzie wspl

        """logika do tego aby joystick trzymał się w granicach naszego układu"""
        if y < 54 and x > 243:
            y = 54
            x = 243
        elif y > 216 and x < 81:
            x = 81
            y = 216
        elif x > 243:
            x = 243
            if y > 216:
                y = 216
        elif y > 216:
            y = 216
            if x > 243:
                x = 243
        elif x < 81:
            x = 81
            if y < 54:
                y = 54
        elif y < 54:
            y = 54
            if x < 81:
                x = 81
            if x > 243:
                x = 243

        self.joystick_steering_label.place(x=x, y=y)
        self.speed_data[0] = x-162
        self.speed_data[1] = (y-135)*(-1)
        self.speed_data_conversion()

    def dropped(self, event):
        self.joystick_steering_label.place(x=162, y=135)

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

    def printer(self):
        print(self.speed_data)
        self.alarm = self.after(10, self.printer)

    # funkcja do zamiany jednostek na osiach
    def speed_data_conversion(self):

        """
        1 część zrobiona aby przekształcić dane zebrane z osi Y
        na wartości odpowiadające sterowaniu silnika (DC 3V/6V)
        ruch przód-tył, aktualny zakres: 92 - 208
        """
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
        2 część zrobiona aby przekształcić dane zebrane z osi X
        na wartości odpowiadające sterowaniu silnika (krokowego)
        skręt kół lewo-prawo, aktualny zakres: 120 - 240 (stopni)
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


