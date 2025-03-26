import unittest
from src.contadorVocales import contar_vocales  # ✅ Asegúrate de importar correctamente

class TestContarVocales(unittest.TestCase):
    def test_mayusculas_y_minusculas(self):
        self.assertEqual(contar_vocales("Ingenieria de Software"), 10)
        
    def test_solo_vocales(self):
        self.assertEqual(contar_vocales("aeiou"), 5)
    
    def test_sin_vocales(self):
        self.assertEqual(contar_vocales("bcdfg"), 0)
    
    def test_vocales_repetidas(self):
        self.assertEqual(contar_vocales("aaaeeeiii"), 9)

if __name__ == "__main__":
    unittest.main()
