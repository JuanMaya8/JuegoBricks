def contar_vocales(texto):
    texto = texto.lower()  # ✅ Convierte todo a minúsculas
    vocales = "aeiou"
    return sum(1 for letra in texto if letra in vocales)
