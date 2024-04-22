import serial
import time

print("Start")
port = "COM6"  # This will be different for various devices and on windows it will probably be a COM port.
bluetooth = serial.Serial(port, 9600)  # Start communications with the bluetooth unit
print("Connected")
time.sleep(1)
# bluetooth.flushInput() #This gives the bluetooth a little kick

# send 5 groups of data to the bluetooth
for i in range(5):
    if i == 0:
        bluetooth.write(b"LED ON")  # Turn Off the LED
    else:
        bluetooth.write(b"DATA shit "+str.encode(str(i)))  # These need to be bytes not unicode, plus a number
    input_data = bluetooth.readline()  # This reads the incoming data. In this particular example it will be the "Bluetooth answers" line
    print(input_data.decode())  # These are bytes coming in so decode is needed
    time.sleep(0.1)  # A pause between bursts

bluetooth.write(b"LED OFF")  # Turn Off the LED, but no answer back from Bluetooth will be printed by python
time.sleep(10)

bluetooth.close()  # Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
