import unittest
from time2colour import get_colour

class TestSecurityFix(unittest.TestCase):
    def test_divisor_type_validation(self):
        # Test with string
        with self.assertRaisesRegex(TypeError, "Divisor must be a number"):
            get_colour("30", 15)
        # Test with None
        with self.assertRaisesRegex(TypeError, "Divisor must be a number"):
            get_colour(None, 15)
        # Test with list
        with self.assertRaisesRegex(TypeError, "Divisor must be a number"):
            get_colour([30], 15)

    def test_val_type_validation(self):
        # Test with string
        with self.assertRaisesRegex(TypeError, "Value must be a number"):
            get_colour(30, "15")
        # Test with None
        with self.assertRaisesRegex(TypeError, "Value must be a number"):
            get_colour(30, None)
        # Test with dict
        with self.assertRaisesRegex(TypeError, "Value must be a number"):
            get_colour(30, {"val": 15})

    def test_valid_numeric_types(self):
        # Should not raise TypeError
        try:
            get_colour(30, 15)      # int, int
            get_colour(30.0, 15)    # float, int
            get_colour(30, 15.5)    # int, float
            get_colour(30.0, 15.5)  # float, float
        except TypeError:
            self.fail("get_colour raised TypeError unexpectedly with valid numeric inputs")

if __name__ == "__main__":
    unittest.main()
