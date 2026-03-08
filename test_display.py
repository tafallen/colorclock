import unittest
from unittest.mock import MagicMock, call
import sys

# Mock the rgbmatrix5x5 module before importing display
mock_rgbmatrix5x5 = MagicMock()
sys.modules['rgbmatrix5x5'] = mock_rgbmatrix5x5

import display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        # Reset the mock before each test to clear call history
        display.matrix.reset_mock()

    def test_set_pixels(self):
        col = [255, 128, 0]
        leds = [(0, 1), (2, 3), (4, 4)]

        display.set_pixels(col, leds)

        # Verify set_pixel is called for each led
        expected_calls = [
            call.set_pixel(0, 1, 255, 128, 0),
            call.set_pixel(2, 3, 255, 128, 0),
            call.set_pixel(4, 4, 255, 128, 0)
        ]
        display.matrix.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(display.matrix.set_pixel.call_count, 3)

    def test_set_hour_pixels(self):
        col = [10, 20, 30]
        display.set_hour_pixels(col)

        # Verify set_pixel was called for each hour LED
        self.assertEqual(display.matrix.set_pixel.call_count, len(display.hour_leds))

        # Verify the first call to ensure correct arguments
        first_led = display.hour_leds[0]
        display.matrix.set_pixel.assert_any_call(first_led[0], first_led[1], col[0], col[1], col[2])

    def test_set_minute_pixels(self):
        col = [40, 50, 60]
        display.set_minute_pixels(col)

        self.assertEqual(display.matrix.set_pixel.call_count, len(display.minute_leds))
        first_led = display.minute_leds[0]
        display.matrix.set_pixel.assert_any_call(first_led[0], first_led[1], col[0], col[1], col[2])

    def test_set_second_pixels(self):
        col = [70, 80, 90]
        display.set_second_pixels(col)

        self.assertEqual(display.matrix.set_pixel.call_count, len(display.second_leds))
        first_led = display.second_leds[0]
        display.matrix.set_pixel.assert_any_call(first_led[0], first_led[1], col[0], col[1], col[2])

    def test_show(self):
        display.show()
        display.matrix.show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
