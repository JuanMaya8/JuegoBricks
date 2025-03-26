import unittest
from contadorVocales import contar_vocales

class TestContarVocales(unittest.TestCase):
    def test_texto_con_vocales(self):
        self.assertEqual(contar_vocales("Hola Mundo"), 4)
        self.assertEqual(contar_vocales("Python"), 1)
        self.assertEqual(contar_vocales("Universidad"), 5)

    def test_texto_sin_vocales(self):
        self.assertEqual(contar_vocales("bcdfg"), 0)
        self.assertEqual(contar_vocales(""), 0)

    def test_texto_con_mayusculas(self):
        self.assertEqual(contar_vocales("AEIOU"), 5)
        self.assertEqual(contar_vocales("AeIoU"), 5)

if __name__ == "__main__":
    unittest.main()
