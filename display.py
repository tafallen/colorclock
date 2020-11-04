from rgbmatrix5x5 import RGBMatrix5x5

matrix = RGBMatrix5x5()
matrix.set_clear_on_exit()
matrix.set_brightness(0.8)

hour_leds = [
    [0,0],
    [0,1],
    [0,2],
    [0,3],
    [0,4],

    [1,0],
    [1,4],

    [2,0],
    [2,4],

    [3,0],
    [3,4],

    [4,0],
    [4,1],
    [4,2],
    [4,3],
    [4,4]
]

minute_leds = [
    [1,1],
    [1,2],
    [1,3],

    [2,1],
    [2,3],

    [3,1],
    [3,2],
    [3,3],
]

second_leds = [
    [2,2]
]

def set_hour_pixels(col):
    set_pixels(col, hour_leds)

def set_minute_pixels(col):
    set_pixels(col, minute_leds)

def set_second_pixels(col):
    set_pixels(col, second_leds)

def set_pixels(col,leds):
    for led in leds:
        matrix.set_pixel(led[0],led[1], col[0],col[1],col[2])
    matrix.show()