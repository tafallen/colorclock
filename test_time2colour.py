import unittest
from datetime import datetime
from time2colour import get_colour, get_colour_60, get_colour_12, get_colours_for_time

class TestTime2Colour(unittest.TestCase):

    def test_get_colour_less_than_divisor(self):
        # divisor = 30, val = 0 -> [255, 0, 0]
        self.assertEqual(get_colour(30, 0), [255, 0, 0])
        # divisor = 30, val = 15 -> step = int(8.5 * 15) = 127 -> [128, 127, 0]
        self.assertEqual(get_colour(30, 15), [128, 127, 0])

    def test_get_colour_equal_to_divisor(self):
        # divisor = 30, val = 30 -> [0, 255, 0]
        self.assertEqual(get_colour(30, 30), [0, 255, 0])

    def test_get_colour_greater_than_divisor(self):
        # divisor = 30, val = 45 -> step = int(8.5 * 15) = 127 -> [0, 128, 127]
        self.assertEqual(get_colour(30, 45), [0, 128, 127])
        # divisor = 30, val = 60 -> step = int(8.5 * 30) = 255 -> [0, 0, 255]
        self.assertEqual(get_colour(30, 60), [0, 0, 255])

    def test_get_colour_60(self):
        # get_colour_60 calls get_colour(30, val)
        self.assertEqual(get_colour_60(0), [255, 0, 0])
        self.assertEqual(get_colour_60(30), [0, 255, 0])
        self.assertEqual(get_colour_60(60), [0, 0, 255])

    def test_get_colour_12(self):
        # get_colour_12 calls get_colour(12, val)
        # x = 255/12 = 21.25
        self.assertEqual(get_colour_12(0), [255, 0, 0])
        self.assertEqual(get_colour_12(12), [0, 255, 0])
        # val = 6 -> step = int(21.25 * 6) = 127 -> [128, 127, 0]
        self.assertEqual(get_colour_12(6), [128, 127, 0])

    def test_get_colours_for_time(self):
        # 12:30:45
        # hour = get_colour_12(12) = [0, 255, 0]
        # minute = get_colour_60(30) = [0, 255, 0]
        # second = get_colour_60(45) = [0, 128, 127]
        t = datetime(2023, 1, 1, 12, 30, 45)
        expected = [
            [0, 255, 0],
            [0, 255, 0],
            [0, 128, 127]
        ]
        self.assertEqual(get_colours_for_time(t), expected)

if __name__ == '__main__':
    unittest.main()
