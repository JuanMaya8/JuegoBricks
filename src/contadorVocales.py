def contar_vocales(texto):
    vocales = "aeiouAEIOU"  # ✅ Ahora incluye mayúsculas también
    return sum(1 for letra in texto if letra in vocales)
