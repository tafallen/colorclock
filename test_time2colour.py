import unittest
from time2colour import get_colour, get_colour_12, get_colour_60, get_colours_for_time
from datetime import time

class TestTime2Colour(unittest.TestCase):
    def test_get_colour_edge_cases(self):
        # val == divisor
        self.assertEqual(get_colour(30, 30), [0, 255, 0])
        self.assertEqual(get_colour(12, 12), [0, 255, 0])

    def test_get_colour_below_divisor(self):
        # val < divisor
        # divisor=30, val=0 -> step=0, r=255, g=0, b=0
        self.assertEqual(get_colour(30, 0), [255, 0, 0])
        # divisor=30, val=15 -> step=127, r=128, g=127, b=0 (255/30 * 15 = 8.5 * 15 = 127.5 -> 127)
        self.assertEqual(get_colour(30, 15), [128, 127, 0])

    def test_get_colour_above_divisor(self):
        # val > divisor
        # divisor=30, val=45 -> step=127, r=0, g=128, b=127
        self.assertEqual(get_colour(30, 45), [0, 128, 127])
        # divisor=30, val=60 -> step=255, r=0, g=0, b=255
        self.assertEqual(get_colour(30, 60), [0, 0, 255])

    def test_get_colour_12(self):
        # Just check it matches get_colour(12, val)
        for i in range(24):
            self.assertEqual(get_colour_12(i), get_colour(12, i))

    def test_get_colour_60(self):
        # Just check it matches get_colour(30, val)
        for i in range(60):
            self.assertEqual(get_colour_60(i), get_colour(30, i))

    def test_get_colours_for_time(self):
        # Test with a specific time: 10:30:45
        test_time = time(10, 30, 45)
        expected_hour_colour = get_colour_12(10)
        expected_minute_colour = get_colour_60(30)
        expected_second_colour = get_colour_60(45)

        colours = get_colours_for_time(test_time)
        self.assertEqual(len(colours), 3)
        self.assertEqual(colours[0], expected_hour_colour)
        self.assertEqual(colours[1], expected_minute_colour)
        self.assertEqual(colours[2], expected_second_colour)

        # Test with midnight
        test_time_midnight = time(0, 0, 0)
        expected_hour_colour_midnight = get_colour_12(0)
        expected_minute_colour_midnight = get_colour_60(0)
        expected_second_colour_midnight = get_colour_60(0)

        colours_midnight = get_colours_for_time(test_time_midnight)
        self.assertEqual(len(colours_midnight), 3)
        self.assertEqual(colours_midnight[0], expected_hour_colour_midnight)
        self.assertEqual(colours_midnight[1], expected_minute_colour_midnight)
        self.assertEqual(colours_midnight[2], expected_second_colour_midnight)

if __name__ == "__main__":
    unittest.main()
