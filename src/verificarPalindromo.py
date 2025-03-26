import re
import unicodedata

def es_palindromo(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)  # ✅ Quita tildes (á, é, í, ó, ú)
    texto = re.sub(r"[^a-z0-9]", "", texto)  # ✅ Elimina todo lo que no sea letra o número
    return texto == texto[::-1]
