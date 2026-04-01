import colorsys
import functools

# Use HSV to get a nicer time to colour conversion
def get_colour(divisor, val):
    if divisor == 0:
        raise ValueError("Divisor cannot be 0")
    # hue goes from 0.0 to 1.0 over the range of 2 * divisor
    hue = (val / (2.0 * divisor)) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    return (int(r * 255), int(g * 255), int(b * 255))

@functools.lru_cache(maxsize=64)
def get_colour_60( val ):
    return get_colour(30,val)

@functools.lru_cache(maxsize=32)
def get_colour_12(val):
    return get_colour(12,val)

def get_colours_for_time(time):
    hour = get_colour_12(time.hour)
    minute = get_colour_60(time.minute)
    second = get_colour_60(time.second)
    return (hour,minute,second)
