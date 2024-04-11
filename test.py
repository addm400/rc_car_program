
from pynput.keyboard import Key
from pynput import keyboard
import threading

""" ten program monitoruje przyciski i sprawdza kiedy zostały naciśnięte i puszczone, dzięki temu mogę napisać
 prowadzić rejestr które przyciski są trzymane a które puszczone i na tej podstawie sterować kierunkiem jazdy,
 do tego należy napisać funkcje które uniemożliwią wciśnięcie dwóch przeciwnych przycisków """


class KeyControl:
    def __init__(self):
        super().__init__()
        self.done = False
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

    def key_check(self):
        if self.up == 1 and self.down == 1:
            self.up = 0
            self.down = 0
            print("wrong")
        elif self.left == 1 and self.right == 1:
            self.left = 0
            self.right = 0
            print("wrong")

    def on_press_key(self, key):
        if key == Key.right:
            self.right = 1
        elif key == Key.left:
            self.left = 1
        elif key == Key.up:
            self.up = 1
        elif key == Key.down:
            self.down = 1

    def on_release_key(self, key):
        if key == Key.right:
            self.right = 0
        elif key == Key.left:
            self.left = 0
        elif key == Key.up:
            self.up = 0
        elif key == Key.down:
            self.down = 0

    def printer(self):
        while not self.done:
            self.key_check()
            values = [self.up, self.down, self.left, self.right]
            print(values)

    def start(self):
        t1 = threading.Thread(target=self.printer)
        t2 = keyboard.Listener(on_press=self.on_press_key, on_release=self.on_release_key)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
