#!/usr/bin/env python

import colorsys
import display
import time
from datetime import datetime
# from rgbmatrix5x5 import RGBMatrix5x5

# matrix = RGBMatrix5x5()
# matrix.set_clear_on_exit()
# matrix.set_brightness(0.8)

# def set_hour_pixels(col):
#     r = col[0]
#     g = col[1]
#     b = col[2]
#     matrix.set_pixel(0,0, r,b,g)
#     matrix.set_pixel(0,1, r,b,g)
#     matrix.set_pixel(0,2, r,b,g)
#     matrix.set_pixel(0,3, r,b,g)
#     matrix.set_pixel(0,4, r,b,g)

#     matrix.set_pixel(1,0, r,b,g)
#     matrix.set_pixel(1,4, r,b,g)

#     matrix.set_pixel(2,0, r,b,g)
#     matrix.set_pixel(2,4, r,b,g)

#     matrix.set_pixel(3,0, r,b,g)
#     matrix.set_pixel(3,4, r,b,g)

#     matrix.set_pixel(4,0, r,b,g)
#     matrix.set_pixel(4,1, r,b,g)
#     matrix.set_pixel(4,2, r,b,g)
#     matrix.set_pixel(4,3, r,b,g)
#     matrix.set_pixel(4,4, r,b,g)

# def set_minute_pixels(col):
#     r = col[0]
#     g = col[1]
#     b = col[2]
#     matrix.set_pixel(1,1, r,b,g)
#     matrix.set_pixel(1,2, r,b,g)
#     matrix.set_pixel(1,3, r,b,g)
#     matrix.set_pixel(2,1, r,b,g)
#     matrix.set_pixel(2,3, r,b,g)
#     matrix.set_pixel(3,1, r,b,g)
#     matrix.set_pixel(3,2, r,b,g)
#     matrix.set_pixel(3,3, r,b,g)
#     matrix.show()

# def set_second_pixels( col ):
#     matrix.set_pixel(2,2,col[0],col[1],col[2])
#     matrix.show()

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

