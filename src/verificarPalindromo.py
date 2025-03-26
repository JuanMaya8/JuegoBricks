def es_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]
