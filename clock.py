#!/usr/bin/env python

# import colorsys
import display
import time
import time2colour
from datetime import datetime

# def get_colour(divisor, val):
#     r=255
#     g=255
#     b=255
#     x = 255/divisor

#     if val == divisor:
#         r = 0
#         b = 0
#         g = 255
#     elif val < divisor:
#         step =  int(x * val)
#         r = 255 - step
#         g = step
#         b = 0
#     else:
#         step = int(x * (val - divisor))
#         r = 0
#         g = 255 - step
#         b = step

#     return [r,g,b]

# def get_colour_60( val ):
#     return get_colour(30,val)

# def get_colour_12(val):
#     return get_colour(12,val)

def update_display(time):
    cols = time2colour.get_colours_for_time(time)
    display.set_hour_pixels(cols[0])
    display.set_minute_pixels(cols[1])
    display.set_second_pixels(cols[2])
    # display.set_hour_pixels(get_colour_12(time.hour))
    # display.set_minute_pixels(get_colour_60(time.minute))
    # display.set_second_pixels(get_colour_60(time.second))

while True:
    now = datetime.now()

    update_display(now)

    time.sleep(1)

