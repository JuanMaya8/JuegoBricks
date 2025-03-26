import sys
import os

# Agregar el directorio 'src' al path para encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from numeroRandom import generar_numero_aleatorio  # Importación después de sys.path

class TestNumeroRandom(unittest.TestCase):
    def test_rango_numero_aleatorio(self):
        for _ in range(100):  # Ejecutar varias veces para asegurar el rango
            numero = generar_numero_aleatorio()
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 100)

if __name__ == "__main__":
    unittest.main()
