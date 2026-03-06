import unittest
from unittest.mock import Mock
from time2colour import get_colour, get_colour_12, get_colour_60, get_colours_for_time

class TestTime2Colour(unittest.TestCase):
    def test_get_colour_edge_cases(self):
        # val == divisor
        # hue = (30 / 60) % 1.0 = 0.5 -> cyan [0, 255, 255]
        self.assertEqual(get_colour(30, 30), [0, 255, 255])
        self.assertEqual(get_colour(12, 12), [0, 255, 255])

    def test_get_colour_below_divisor(self):
        # val < divisor
        # val=0 -> hue=0 -> red [255, 0, 0]
        self.assertEqual(get_colour(30, 0), [255, 0, 0])
        # val=15 -> hue=(15/60)=0.25 -> chartreuse green [127, 255, 0]
        self.assertEqual(get_colour(30, 15), [127, 255, 0])

    def test_get_colour_above_divisor(self):
        # val > divisor
        # val=45 -> hue=(45/60)=0.75 -> purple [127, 0, 255]
        self.assertEqual(get_colour(30, 45), [127, 0, 255])
        # val=60 -> hue=(60/60) % 1.0 = 0 -> red [255, 0, 0]
        self.assertEqual(get_colour(30, 60), [255, 0, 0])

    def test_get_colour_modulo(self):
        # tests modulo logic when val > 2 * divisor
        self.assertEqual(get_colour(30, 75), get_colour(30, 15))

    def test_get_colour_12(self):
        # Just check it matches get_colour(12, val)
        for i in range(24):
            self.assertEqual(get_colour_12(i), get_colour(12, i))

    def test_get_colour_60(self):
        # Just check it matches get_colour(30, val)
        for i in range(60):
            self.assertEqual(get_colour_60(i), get_colour(30, i))

    def test_get_colours_for_time(self):
        # mock datetime object
        mock_time = Mock()
        mock_time.hour = 12
        mock_time.minute = 30
        mock_time.second = 45

        expected_hour = get_colour(12, 12)
        expected_minute = get_colour(30, 30)
        expected_second = get_colour(30, 45)

        self.assertEqual(get_colours_for_time(mock_time), [expected_hour, expected_minute, expected_second])

if __name__ == "__main__":
    unittest.main()
