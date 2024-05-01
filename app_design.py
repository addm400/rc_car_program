
import tkinter
import customtkinter
from tkinter import *
from PIL import Image, ImageTk

import os
import ctypes
from threading import Thread

from bluetooth_communication import *
from conversion import *
from ports import *


"""
Main file for RC control car program
"""


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # creating object to convert values from joystick axis to values to control micro servo
        self.conversion_sys = ConversionSys()

        # binding key press and release
        self.bind('<Key>', self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        self.title("RC car control panel")
        self.geometry("800x500")
        self.resizable(False, False)

        # set grid layout 3x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # tab for holding which window is currently displayed (1/2/3)
        self.which_window = [1]

        # values used to adjust size of images in canvas
        self.image_database = {
            "board_size_100": 275,
            "board_size_150": 436,
            "joystick_size_100": 80,
            "joystick_size_150": 120,
        }

        # values used to adjust size of canvas
        self.canvas_database = {
            "canvas_width_100": 275, "canvas_height_100": 275,
            "canvas_width_150": 436, "canvas_height_150": 436,
        }

        # a dictionary to store data for joystick positioning
        self.joystick_database = {
            "x_home": 98,
            "y_home": 97,
            "end_value": 195
        }

        # a dictionary to store data for car controling
        self.car_database = {
            "keyboard_speed_forward": 70,
            "keyboard_speed_backward": 110,
            "current_speed_x": 75,
            "current_speed_y1": 90,
            "current_speed_y2": 90,
            "connection_status": "not connected"
        }

        # load images that will be used later
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "icon.png")), size=(45, 30))
        self.home_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_pic.png")), size=(20, 20))
        self.keyboard_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "keyboard_pic.png")), size=(20, 20))
        self.joystick_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "joystick_pic.png")), size=(20, 20))
        self.arrows_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "strzalki.png")), size=(239, 220))

        self.joystick_board_image = Image.open('test_images//arrows.png')
        self.joystick_board_image = self.joystick_board_image.resize((self.image_database["board_size_100"], self.image_database["board_size_100"]))

        self.joystick_circle = Image.open('test_images//kolko.png')
        self.joystick_circle = self.joystick_circle.resize((self.image_database["joystick_size_100"], self.image_database["joystick_size_100"]))

        # create navigation frame on the left hand side
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Control Panel", image=self.logo_icon,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # create buttons to switch between pages
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_icon, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.keyboard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Keyboard",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.keyboard_icon, anchor="w", command=self.keyboard_button_event)
        self.keyboard_button.grid(row=2, column=0, sticky="ew")

        self.joystick_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Joystick",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.joystick_icon, anchor="w", command=self.joystick_button_event)
        self.joystick_button.grid(row=3, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # looking for a COM port associated with HC-05 bluetooth module for Arduino
        self.bluetooth_module_port = Port()

        # creating object to handle bluetooth communication with the car and passing COM port
        self.bluetooth = Blut()
        self.bluetooth.define_port(self.bluetooth_module_port.scanner()[0])

        """tutaj należy zrobić layout dla ramki home"""

        self.welcome_text = customtkinter.CTkTextbox(self.home_frame, width=300, height=200, corner_radius=0)
        self.welcome_text.grid(row=0, column=0, rowspan=4, padx=(20, 0), pady=(60, 20))
        self.welcome_text.insert(index="0.0", text="\n WELCOME\n\n" +
                                 " This is program made for RC car control\n\n" +
                                 " 1. Connect your device to the car\n\n" +
                                 " 2. Start driving your car\n\n" +
                                 " You can use keyboard or joystick steering\n\n")
        self.welcome_text.configure(state="disabled")

        self.connection_frame = customtkinter.CTkFrame(self.home_frame, height=200, width=200)
        self.connection_frame.grid(row=0, column=1, padx=(20, 20), pady=(80, 0))
        self.port = self.bluetooth_module_port.scanner()

        if len(self.port) > 0:
            self.port = "MICROCONTROLLER FOUND AT: "+self.bluetooth_module_port.scanner()[0]
        else:
            self.port = "MICROCONTROLLER NOT FOUND"

        self.com_port_label = customtkinter.CTkLabel(self.connection_frame, text=self.port)
        self.com_port_label.grid(row=0, column=0, padx=10, pady=10)

        self.connect_button = customtkinter.CTkButton(self.home_frame, command=self.connect_button_event,
                                                      text="Connect", fg_color="green", hover_color='grey')
        self.connect_button.grid(row=1, column=1, padx=20, pady=(10, 0))
        # zrobić tak żeby nie dało się kliknąć znowu przycisku connect i dissconnect
        self.disconnect_button = customtkinter.CTkButton(self.home_frame, command=self.disconnect_button_event,
                                                         text="Disconnect", fg_color="red", hover_color='grey')
        self.disconnect_button.grid(row=2, column=1, padx=20, pady=10)

        # create textbox/consol
        self.consol_frame = customtkinter.CTkFrame(self, fg_color='#1d1e1e', corner_radius=0)
        self.consol_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew",)

        # frame and label created to display console name at the top of the text box
        self.console_name = customtkinter.CTkLabel(master=self.consol_frame, text="Console",
                                                        font=customtkinter.CTkFont(size=13))
        self.console_name.grid(row=0, column=0, padx=(10, 20), pady=(0, 0), sticky="nsew")

        # a variable for holding current position of cursor in console
        self.consoleposition = 5.0

        self.console = customtkinter.CTkTextbox(self, width=100, height=120, corner_radius=0)
        self.console.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.console.configure(state="disabled")

        # create second frame
        self.keyboard_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.keyboard_frame.grid_columnconfigure(0, weight=1)

        self.keyboard_image_label = customtkinter.CTkLabel(self.keyboard_frame, text="", image=self.arrows_image)
        self.keyboard_image_label.grid(row=0, column=0, padx=(20, 0), pady=(0, 0))

        self.keyboard_instruction_frame = customtkinter.CTkFrame(self.keyboard_frame)
        self.keyboard_instruction_frame.grid(row=1, column=0, padx=(20, 0), pady=(0, 15), sticky="nsew")

        self.keyboard_instruction = customtkinter.CTkLabel(self.keyboard_instruction_frame, text="W – MOVE FORWARD\n" +
                                                                          "S – MOVE BACKWARD\n" +
                                                                          "A – TURN LEFT \n" +
                                                                          "D – TURN RIGHT")
        self.keyboard_instruction.grid(row=0, column=0, padx=(70, 0), pady=(15, 15))

        # radiobutton frame
        self.radiobutton_speed_control_frame = customtkinter.CTkFrame(self.keyboard_frame)
        self.radiobutton_speed_control_frame.grid(row=0, column=1, rowspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)

        # creating label for radio buttons to control speed
        self.label_radio_speed = customtkinter.CTkLabel(master=self.radiobutton_speed_control_frame, text="Speed Control", font=customtkinter.CTkFont(size=20))
        self.label_radio_speed.grid(row=0, column=1, columnspan=1, padx=(70, 50), pady=(50, 20), sticky="nsew")

        self.radio_30_button = customtkinter.CTkRadioButton(master=self.radiobutton_speed_control_frame, variable=self.radio_var, value=0,
                                                            text="30% of MAX SPEED", font=customtkinter.CTkFont(size=13), command=self.radio_button_1)
        self.radio_30_button.grid(row=1, column=1, pady=10, padx=(70, 50), sticky="n")

        self.radio_60_button = customtkinter.CTkRadioButton(master=self.radiobutton_speed_control_frame, variable=self.radio_var, value=1,
                                                            text="60% of MAX SPEED", font=customtkinter.CTkFont(size=13), command=self.radio_button_2)
        self.radio_60_button.grid(row=2, column=1, pady=10, padx=(70, 50), sticky="n")

        self.radio_100_button = customtkinter.CTkRadioButton(master=self.radiobutton_speed_control_frame, variable=self.radio_var, value=2,
                                                             text="100% of MAX SPEED", font=customtkinter.CTkFont(size=13), command=self.radio_button_3)
        self.radio_100_button.grid(row=3, column=1, pady=10, padx=(76, 50), sticky="n")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        # getting current scale factor of windows for image adjusting
        self.scaleFactor = (ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100)

        self.joystick_board_label = Canvas(self.third_frame, width=self.canvas_database["canvas_width_100"],
                                           height=self.canvas_database["canvas_height_100"], highlightthickness=0)
        self.joystick_board_label.grid(row=0, column=0, pady=(20, 0), padx=(22, 306))

        # scaling images based on scale factor
        self.scaling_image()

        # creating bg photo of joystick board using canvas
        self.bgphoto = ImageTk.PhotoImage(self.joystick_board_image)
        self.joystick_board = self.joystick_board_label.create_image(0, 0, image=self.bgphoto, anchor=NW)

        # creating photo of joystick control using canvas
        self.analog = ImageTk.PhotoImage(self.joystick_circle)
        self.joystick_control_circle = self.joystick_board_label.create_image(0, 0, image=self.analog, anchor=NW)

        self.joystick_board_label.moveto(self.joystick_control_circle,
                                         self.joystick_database["x_home"], self.joystick_database["y_home"])

        self.joystick_board_label.tag_bind(self.joystick_control_circle, "<Button-1>", self.drag_start)
        self.joystick_board_label.tag_bind(self.joystick_control_circle, "<B1-Motion>", self.drag_motion)
        self.joystick_board_label.tag_bind(self.joystick_control_circle, "<ButtonRelease-1>", self.dropped)

        # creating variables to hold data used to move joystick
        self.coordinates = self.joystick_board_label.coords(self.joystick_control_circle)
        self.x_pos = None
        self.y_pos = None

        # select default frame
        self.select_frame_by_name("home")

    """
    ***** The end of __init__ section *****
    """

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.keyboard_button.configure(fg_color=("gray75", "gray25") if name == "keyboard" else "transparent")
        self.joystick_button.configure(fg_color=("gray75", "gray25") if name == "joystick" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "keyboard":
            self.keyboard_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.keyboard_frame.grid_forget()
        if name == "joystick":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    # handling navigation button events and tracking which window is currently selected
    def home_button_event(self):
        self.select_frame_by_name("home")
        self.which_window[0] = 1

    def keyboard_button_event(self):
        self.select_frame_by_name("keyboard")
        self.which_window[0] = 2

    def joystick_button_event(self):
        self.select_frame_by_name("joystick")
        self.which_window[0] = 3

    def console_print(self, text):
        self.console.configure(state="normal")
        self.console.insert(index=self.consoleposition, text=" "+text+"\n\n")
        self.consoleposition += 2
        self.console.configure(state="disabled")
        self.console.see("end")
    # handling radio button events and changing car control values that are ready to send to microcontroller
    def radio_button_1(self):
        self.car_database['keyboard_speed_forward'] = 70
        self.car_database['keyboard_speed_backward'] = 110
        self.console_print("30% of maximum car speed is set")

    def radio_button_2(self):
        self.car_database['keyboard_speed_forward'] = 40
        self.car_database['keyboard_speed_backward'] = 140
        self.console_print("60% of maximum car speed is set")

    def radio_button_3(self):
        self.car_database['keyboard_speed_forward'] = 10
        self.car_database['keyboard_speed_backward'] = 170
        self.console_print("100% of maximum car speed is set")


    # handling beginning of drag motion
    def drag_start(self, event):
        self.coordinates = self.joystick_board_label.coords(self.joystick_control_circle)
        self.x_pos = event.x
        self.y_pos = event.y

    # handling drag motion
    def drag_motion(self, event):
        win_x = event.x
        win_y = event.y

        # getting the object coords where, there was an event
        x = self.coordinates[0] - self.x_pos + event.x
        y = self.coordinates[1] - self.y_pos + event.y

        # tracking position of the joystick and keeping it within the limits of the board
        if x < 0:
            x = 0
        elif x > self.joystick_database['end_value']:
            x = self.joystick_database['end_value']
        else:
            self.x_pos = win_x

        if y < 0:
            y = 0
        elif y > self.joystick_database['end_value']:
            y = self.joystick_database['end_value']
        else:
            self.y_pos = win_y

        # obsługa przesuwania obiektu w naszym układzie wspl
        self.joystick_board_label.moveto(self.joystick_control_circle, x, y)
        self.coordinates = self.joystick_board_label.coords(self.joystick_control_circle)
        # conv from float to int
        self.coordinates[0] = int(self.coordinates[0])
        self.coordinates[1] = int(self.coordinates[1])

        # conv from axis values to control values
        new_speed = self.conversion_sys.axis_conversion(self.coordinates, self.scaleFactor)

        self.car_database['current_speed_x'] = new_speed["x_speed"]
        self.car_database['current_speed_y1'] = new_speed["y1_speed"]
        self.car_database['current_speed_y2'] = new_speed["y2_speed"]

    def dropped(self, event):
        self.joystick_board_label.moveto(self.joystick_control_circle,
                                         self.joystick_database["x_home"], self.joystick_database["y_home"])

        self.car_database['current_speed_x'] = 75
        self.car_database['current_speed_y1'] = 90
        self.car_database['current_speed_y2'] = 90

    def key_press(self, event):
        if self.which_window[0] == 2:
            if event.char == "w":
                self.car_database['current_speed_y1'] = self.car_database['keyboard_speed_forward']
                self.car_database['current_speed_y2'] = self.car_database['keyboard_speed_backward']
            elif event.char == "s":
                self.car_database['current_speed_y1'] = self.car_database['keyboard_speed_backward']
                self.car_database['current_speed_y2'] = self.car_database['keyboard_speed_forward']
            elif event.char == "a":
                self.car_database['current_speed_x'] = 115
            elif event.char == "d":
                self.car_database['current_speed_x'] = 35

    def key_release(self, event):

        if self.which_window[0] == 2:
            if event.char == "w":
                self.car_database['current_speed_y1'] = 90
            elif event.char == "s":
                self.car_database['current_speed_y1'] = 90
            elif event.char == "a":
                self.car_database['current_speed_x'] = 75
            elif event.char == "d":
                self.car_database['current_speed_x'] = 75

    # function for checking COM port and enabling bluetooth communication
    def printer(self):
        """port = self.bluetooth_module_port.scanner()
        self.console_print("Connecting started...")
        # checking if COM port is found
        if len(port) > 0:
            try:
                self.bluetooth.start_connection()
            except AttributeError as e:
                self.console_print("Check connection and try again")
                self.car_database['connection_status'] = "not connected"
            except:
                self.console_print("Check connection and try again")
                self.car_database['connection_status'] = "not connected"
            else:
                self.car_database['connection_status'] = "connected"
                self.console_print("Connected")
                self.bluetooth.board_setup()
                self.trans()
        else:
            self.console_print('Check if bluetooth is enabled')
            self.console_print('Check if car is connected to your device')
            self.car_database['connection_status'] = "not connected" """
        self.trans()

    # periodic function for sending control data to the car
    def trans(self):
        #self.bluetooth.transmission(self.car_database['current_speed_y1'])
        print(self.car_database['current_speed_x'], self.car_database['current_speed_y1'], self.car_database['current_speed_y2'])
        self.alarm = self.after(10, self.trans)

    def scaling_image(self):
        """function made to scale images and axis values depending on scale factor of Windows for ex. 100%, 150%"""
        if self.scaleFactor == 1.5:
            self.joystick_board_label.configure(width=self.canvas_database["canvas_width_150"],
                                                height=self.canvas_database["canvas_height_150"])
            self.joystick_board_label.grid(row=0, column=0, pady=(20, 0), padx=(0, 410))

            self.joystick_board_image = self.joystick_board_image.resize((self.image_database["board_size_150"],
                                                                          self.image_database["board_size_150"]))

            self.joystick_circle = self.joystick_circle.resize((self.image_database["joystick_size_150"],
                                                                self.image_database["joystick_size_150"]))

            self.joystick_database["x_home"] = 157
            self.joystick_database["y_home"] = 156
            self.joystick_database['end_value'] = 316

    def com_menu_event(self, selection):
        print(selection)

    def connect_button_event(self):
        if self.car_database['connection_status'] == "not connected":
            new_thread = Thread(target=self.printer, args=(), daemon=True)
            new_thread.start()
            self.car_database['connection_status'] = "connected"
        else:
            self.console_print("Car is alread connected")

    def disconnect_button_event(self):
        pass

