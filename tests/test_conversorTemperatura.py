import unittest
from conversorTemperatura import celsius_a_fahrenheit

class TestConversionTemperatura(unittest.TestCase):
    def test_conversion_correcta(self):
        self.assertEqual(celsius_a_fahrenheit(0), 32)
        self.assertEqual(celsius_a_fahrenheit(25), 77)
        self.assertEqual(celsius_a_fahrenheit(100), 212)
        self.assertEqual(celsius_a_fahrenheit(-40), -40)

    def test_conversion_decimal(self):
        self.assertAlmostEqual(celsius_a_fahrenheit(37.5), 99.5, places=1)
        self.assertAlmostEqual(celsius_a_fahrenheit(-10.5), 13.1, places=1)

if __name__ == "__main__":
    unittest.main()
