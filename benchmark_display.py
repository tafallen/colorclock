import timeit
import sys
from unittest.mock import MagicMock

# Mock the rgbmatrix5x5 module before importing display
mock_rgbmatrix5x5 = MagicMock()
sys.modules['rgbmatrix5x5'] = mock_rgbmatrix5x5

import display

# Use a simple lambda to minimize overhead of the mock call
display.matrix.set_pixel = lambda *args: None

def benchmark_set_pixels():
    col = (255, 128, 64)
    # 5x5 grid
    leds = [(x, y) for x in range(5) for y in range(5)]

    number = 100000
    timer = timeit.Timer(lambda: display.set_pixels(col, leds))
    time_taken = timer.timeit(number=number)
    print(f"set_pixels (25 LEDs, {number} calls): {time_taken:.4f} seconds")

if __name__ == "__main__":
    benchmark_set_pixels()
