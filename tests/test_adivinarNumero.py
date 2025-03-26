import unittest
from adivinarNumero import adivina_el_numero

class TestAdivinaNumero(unittest.TestCase):
    def test_adivinar_exitoso(self):
        numero_secreto = 25
        resultado, intentos = adivina_el_numero(numero_secreto, 50)
        self.assertTrue(resultado)
        self.assertLessEqual(intentos, 50)

    def test_no_adivina(self):
        numero_secreto = 51  # Fuera del rango generado
        resultado, intentos = adivina_el_numero(numero_secreto, 10)
        self.assertFalse(resultado)
        self.assertEqual(intentos, 10)

if __name__ == "__main__":
    unittest.main()
