from rgbmatrix5x5 import RGBMatrix5x5

matrix = RGBMatrix5x5()
matrix.set_clear_on_exit()
matrix.set_brightness(0.8)

# TODO: Arrays for pixel co-ords

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
    for x in hour_leds:
        matrix.set_pixel(x[0],x[1], col[0],col[1],col[2])
    matrix.show()

def set_minute_pixels(col):
    for x in minute_leds:
        matrix.set_pixel(x[0],x[1], col[0],col[1],col[2])
    # r = col[0]
    # g = col[1]
    # b = col[2]
    # matrix.set_pixel(1,1, r,b,g)
    # matrix.set_pixel(1,2, r,b,g)
    # matrix.set_pixel(1,3, r,b,g)
    # matrix.set_pixel(2,1, r,b,g)
    # matrix.set_pixel(2,3, r,b,g)
    # matrix.set_pixel(3,1, r,b,g)
    # matrix.set_pixel(3,2, r,b,g)
    # matrix.set_pixel(3,3, r,b,g)
    matrix.show()

def set_second_pixels( col ):
    for x in second_leds:
        matrix.set_pixel(x[0],x[1], col[0],col[1],col[2])
    # matrix.set_pixel(2,2,col[0],col[1],col[2])
    matrix.show()