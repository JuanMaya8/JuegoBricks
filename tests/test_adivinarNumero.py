import sys
import os

# Agregar el directorio 'src' al path para encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from adivinarNumero import adivina_el_numero  # Importación después de sys.path

class TestAdivinaNumero(unittest.TestCase):
    def test_adivinar_exitoso(self):
        resultado, intentos = adivina_el_numero(5, 10)  # ✅ Se adivinará en 5 intentos
        self.assertTrue(resultado)
        self.assertLessEqual(intentos, 10)


    def test_no_adivina(self):
        numero_secreto = 51  # Fuera del rango generado
        resultado, intentos = adivina_el_numero(numero_secreto, 10)
        self.assertFalse(resultado)
        self.assertEqual(intentos, 10)

if __name__ == "__main__":
    unittest.main()
