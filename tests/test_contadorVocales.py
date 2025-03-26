import sys
import os

# Agregar el directorio 'src' al path para encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from contadorVocales import contar_vocales  # Importación después de sys.path

class TestContarVocales(unittest.TestCase):
    def test_frase_simple(self):
        self.assertEqual(contar_vocales("Hola Mundo"), 4)

    def test_solo_vocales(self):
        self.assertEqual(contar_vocales("aeiou"), 5)

    def test_sin_vocales(self):
        self.assertEqual(contar_vocales("rhythm"), 0)

    def test_mayusculas_y_minusculas(self):
        self.assertEqual(contar_vocales("Python Es Genial"), 6)  # ✅ Ahora debería funcionar



    def test_frase_con_numeros_y_simbolos(self):
        self.assertEqual(contar_vocales("123!@#Hello World!"), 3)

if __name__ == "__main__":
    unittest.main()
