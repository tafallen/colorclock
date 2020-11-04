#!/usr/bin/env python

import colorsys
import display
import time
from datetime import datetime

def get_colour_60( val ):
    r=255
    g=255
    b=255
    x = 255/30

    if val == 30:
        r = 0
        b = 0
        g = 255
    elif val < 30:
        step =  int(x * val)
        r = 255 - step
        g = step
        b = 0
    else:
        step = int(x * (val - 30))
        r = 0
        g = 255 - step
        b = step

    return [r,g,b]

def get_colour_12(val):
    r=255
    g=255
    b=255
    x = 255/12

    if val == 12:
        r = 0
        b = 0
    elif val < 12:
        step = int( val * x)
        r = 255 - step
        g = step
        b = 0
    else:
        step = int((val - 12) * x)
        r = 0
        g = 255 - step
        b = step

    return [r,g,b]


while True:
    now = datetime.now()

    display.set_hour_pixels(get_colour_12(now.hour))
    display.set_minute_pixels(get_colour_60(now.minute))
    display.set_second_pixels(get_colour_60(now.second))

    time.sleep(1)

