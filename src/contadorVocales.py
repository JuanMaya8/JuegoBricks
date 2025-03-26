def contar_vocales(texto):
    vocales = "aeiou"
    return sum(1 for letra in texto.lower() if letra in vocales)
