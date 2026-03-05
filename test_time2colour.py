import unittest
from time2colour import get_colour, get_colour_12, get_colour_60

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

if __name__ == "__main__":
    unittest.main()
