def contar_vocales(texto):
    texto = texto.lower()
    vocales = "aeiou"
    contador = sum(1 for letra in texto if letra in vocales)
    print(f"Número de vocales: {contador}")

frase = input("Ingrese una frase o palabra: ")
contar_vocales(frase)
