from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.garden.joystick import Joystick
import serial.tools.list_ports
import serial
import threading
import time

class BluetoothDevicePopup(Popup):
    def __init__(self, devices, callback, **kwargs):
        super().__init__(title="Select Bluetooth Device", **kwargs)  # Set popup title
        layout = BoxLayout(orientation='vertical')
        self.devices = devices
        for device in devices:
            button = Button(text=device.device, size_hint_y=None, height=40)
            button.bind(on_release=lambda b, d=device.device: self.on_device_selected(b, d, callback)) # Pass device name to callback
            layout.add_widget(button)
        self.content = layout

    def on_device_selected(self, instance, device, callback):
        callback(device)  # Call the callback with the selected device
        self.dismiss()    # Close the popup after selecting a device

class ServoControlApp(App):

    def build(self):
        # Get available serial ports (including Bluetooth)
        self.bluetooth_devices = list(serial.tools.list_ports.comports())
        if not self.bluetooth_devices:
            return Label(text="No Bluetooth devices found")

        # Open Bluetooth device selection popup
        popup = BluetoothDevicePopup(devices=self.bluetooth_devices, callback=self.connect_to_device)
        popup.open()

        # Placeholder layout to be replaced after selecting a device
        self.layout = BoxLayout(orientation='vertical')
        return self.layout

    def connect_to_device(self, device):
        # Connect to selected Bluetooth device
        #self.ser = serial.Serial(device, 9600) # Adjust baud rate if necessary
        # Add label above the joystick with smaller size hint
        label = Label(text="RC Car control joystick", size_hint=(1, 0.1))
        self.layout.add_widget(label)
        # Build smaller joystick interface
        joystick = Joystick(size_hint=(1, 0.9))
        joystick.bind(pad=self.send_angle)
        # Replace placeholder layout with joystick interface
        self.layout.clear_widgets()
        self.layout.add_widget(label)
        self.layout.add_widget(joystick)

    def send_angle(self, instance, pad):
        # Map joystick position to servo angle
        x, y = pad
        self.angle1 = int(x * 90)  # Center position is 90 degrees
        self.angle2 = int(y * 90)
        # Send servo angle to Arduino Nano
        #self.ser.write(str(angle1).encode())

    def periodic_function(self):
        while True:
            # Perform your servo control function here
            print(self.angle1, self.angle2)
            time.sleep(0.5)  # Adjust the interval as needed (e.g., 5 seconds)

    # Start the periodic function in a separate thread
    thread = threading.Thread(target=periodic_function)
    thread.daemon = True  # Daemonize the thread to allow the program to exit cleanly
    thread.start()


ServoControlApp().run()
