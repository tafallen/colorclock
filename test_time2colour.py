import unittest
from time2colour import get_colour, get_colour_12, get_colour_60, get_colours_for_time
from datetime import time, datetime

class TestTime2Colour(unittest.TestCase):
    def test_get_colour_zero_divisor(self):
        with self.assertRaises(ValueError) as context:
            get_colour(0, 15)
        self.assertEqual(str(context.exception), "Divisor cannot be 0")

    def test_get_colour_edge_cases(self):
        # val == divisor
        self.assertEqual(get_colour(30, 30), [0, 255, 255])
        self.assertEqual(get_colour(12, 12), [0, 255, 255])

    def test_get_colour_below_divisor(self):
        # val < divisor
        self.assertEqual(get_colour(30, 0), [255, 0, 0])
        self.assertEqual(get_colour(30, 15), [127, 255, 0])

    def test_get_colour_above_divisor(self):
        # val > divisor
        self.assertEqual(get_colour(30, 45), [127, 0, 255])
        self.assertEqual(get_colour(30, 60), [255, 0, 0])

    def test_get_colour_modulo(self):
        # tests modulo logic when val > 2 * divisor
        self.assertEqual(get_colour(30, 75), get_colour(30, 15))

    def test_get_colour_negative(self):
        # tests negative val
        self.assertEqual(get_colour(30, -15), get_colour(30, 45))

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

    def test_get_colours_for_time_invalid_input(self):
        # Test with None
        with self.assertRaises(TypeError) as context:
            get_colours_for_time(None)
        self.assertEqual(str(context.exception), "current_time must be a datetime.time or datetime.datetime object")

        # Test with string
        with self.assertRaises(TypeError) as context:
            get_colours_for_time("10:30:45")
        self.assertEqual(str(context.exception), "current_time must be a datetime.time or datetime.datetime object")

        # Test with integer
        with self.assertRaises(TypeError) as context:
            get_colours_for_time(123456789)
        self.assertEqual(str(context.exception), "current_time must be a datetime.time or datetime.datetime object")

        # Test with dummy object
        class Dummy:
            pass
        with self.assertRaises(TypeError) as context:
            get_colours_for_time(Dummy())
        self.assertEqual(str(context.exception), "current_time must be a datetime.time or datetime.datetime object")

    def test_get_colours_for_datetime(self):
        # Test that datetime.datetime objects are also accepted
        test_dt = datetime(2023, 10, 27, 10, 30, 45)
        colours = get_colours_for_time(test_dt)
        self.assertEqual(len(colours), 3)
        self.assertEqual(colours[0], get_colour_12(10))

if __name__ == "__main__":
    unittest.main()
