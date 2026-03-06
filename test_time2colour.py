import unittest
from time2colour import get_colour, get_colour_12, get_colour_60

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
