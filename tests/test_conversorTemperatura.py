import sys
import os

# Agregar el directorio 'src' al path para encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from conversorTemperatura import celsius_a_fahrenheit  # Importación después de sys.path

class TestConversorTemperatura(unittest.TestCase):
    def test_cero_grados(self):
        self.assertEqual(celsius_a_fahrenheit(0), 32)

    def test_valor_positivo(self):
        self.assertEqual(celsius_a_fahrenheit(25), 77)

    def test_valor_negativo(self):
        self.assertEqual(celsius_a_fahrenheit(-40), -40)

    def test_gran_valor(self):
        self.assertEqual(celsius_a_fahrenheit(100), 212)

    def test_decimal(self):
        self.assertAlmostEqual(celsius_a_fahrenheit(37.5), 99.5, places=1)

if __name__ == "__main__":
    unittest.main()
