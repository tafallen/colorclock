from datetime import datetime

# TODO: Use HSV to get a nicer time to colour conversion
def get_colour(divisor, val):
    r=255
    g=255
    b=255
    x = 255/divisor

    if val == divisor:
        r = 0
        b = 0
        g = 255
    elif val < divisor:
        step =  int(x * val)
        r = 255 - step
        g = step
        b = 0
    else:
        step = int(x * (val - divisor))
        r = 0
        g = 255 - step
        b = step

    return [r,g,b]

def get_colour_60( val ):
    return get_colour(30,val)

def get_colour_12(val):
    return get_colour(12,val)

def get_colours_for_time(time):
    hour = get_colour_12(time.hour)
    minute = get_colour_60(time.minute)
    second = get_colour_60(time.second)
    return [hour,minute,second]