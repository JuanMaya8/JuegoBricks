import unittest
from verificarPalindromo import es_palindromo

class TestEsPalindromo(unittest.TestCase):
    def test_palindromos(self):
        self.assertTrue(es_palindromo("Anita lava la tina"))
        self.assertTrue(es_palindromo("A Santa at NASA"))
        self.assertTrue(es_palindromo("Luz azul"))
        self.assertTrue(es_palindromo("La ruta natural"))
        self.assertTrue(es_palindromo("No subas, abusón"))

    def test_no_palindromos(self):
        self.assertFalse(es_palindromo("Hola mundo"))
        self.assertFalse(es_palindromo("Python es genial"))
        self.assertFalse(es_palindromo("Esto no es un palíndromo"))

    def test_palindromos_con_puntuacion(self):
        self.assertTrue(es_palindromo("¿Acaso hubo búhos acá?"))
        self.assertTrue(es_palindromo("Dábale arroz a la zorra el abad."))

if __name__ == "__main__":
    unittest.main()
