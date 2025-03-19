def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

frase = input("Ingrese una palabra o frase: ")
if es_palindromo(frase):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
