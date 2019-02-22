#! /usr/bin/python3
from sense_hat import SenseHat
import time
import sys

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
fedora = SenseHat()
try:
    while True:
        temp = fedora.get_temperature()
        f = (temp * 9/5) + 32
        if f <= 65:
            fedora.show_message("%.1f F" % f, text_colour=blue, scroll_speed=0.15)
        elif f > 65 and f <= 70:
          fedora.show_message("%.1f F" % f, text_colour=white, scroll_speed=0.15)
        elif f > 70:
          fedora.show_message("%.1f F" % f, text_colour=red, scroll_speed=0.15)
        time.sleep(2)
except KeyboardInterrupt:
    fedora.clear()
    sys.exit()
