from pyfirmata2 import Arduino, SERVO
import time

board = Arduino('COM6')
print('connected')
pin = 3
board.digital[pin].mode = SERVO
board.digital[pin].write(90)
time.sleep(1)
board.digital[pin].write(80)
time.sleep(0.5)
board.digital[pin].write(60)
time.sleep(0.5)
board.digital[pin].write(40)
time.sleep(0.5)
board.digital[pin].write(20)
time.sleep(0.5)
time.sleep(8)
board.digital[pin].write(90)
print('done')

