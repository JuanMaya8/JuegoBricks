import re

def es_palindromo(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]", "", texto)  # ✅ Solo deja letras y números
    return texto == texto[::-1]
