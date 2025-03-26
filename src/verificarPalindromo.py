import re

def es_palindromo(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]", "", texto)  # ✅ Elimina espacios y signos de puntuación
    return texto == texto[::-1]
