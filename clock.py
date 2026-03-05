#!/usr/bin/env python

import display
import time
import time2colour
from datetime import datetime

def update_display(current_time):
    cols = time2colour.get_colours_for_time(current_time)
    display.set_hour_pixels(cols[0])
    display.set_minute_pixels(cols[1])
    display.set_second_pixels(cols[2])


while True:
    update_display(datetime.now())

    time.sleep(1)

