import unittest
from numeroRandom import generar_numero_aleatorio

class TestGenerarNumeroAleatorio(unittest.TestCase):
    def test_rango_correcto(self):
        for _ in range(1000):  # Se prueba varias veces para mayor seguridad
            numero = generar_numero_aleatorio()
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 100)

if __name__ == "__main__":
    unittest.main()
