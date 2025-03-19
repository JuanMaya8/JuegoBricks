def contar_vocales(texto):
    texto = texto.lower()
    vocales = "aeiou"
    return sum(1 for letra in texto if letra in vocales)

def main():
    frase = "Hola Mundo"  # Texto fijo de ejemplo
    cantidad = contar_vocales(frase)
    print(f"Texto: {frase}")
    print(f"Número de vocales: {cantidad}")

if __name__ == "__main__":
    main()
