import sys
import os

# Agregar el directorio 'src' al path para encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from verificarPalindromo import es_palindromo  # Importación después de sys.path

class TestVerificarPalindromo(unittest.TestCase):
    def test_palindromo_simple(self):
        self.assertTrue(es_palindromo("oso"))

    def test_palindromo_con_espacios(self):
        self.assertTrue(es_palindromo("anita lava la tina"))

    def test_palindromo_con_mayusculas(self):
        self.assertTrue(es_palindromo("Ana"))

    def test_palindromo_con_signos(self):
        self.assertTrue(es_palindromo("A mamá Roma le aviva el amor a mamá."))  # ✅ Ahora sí pasa

    def test_no_es_palindromo(self):
        self.assertFalse(es_palindromo("Hola Mundo"))

    def test_cadena_vacia(self):
        self.assertTrue(es_palindromo(""))

if __name__ == "__main__":
    unittest.main()
