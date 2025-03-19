def es_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

def main():
    frase = "Anita lava la tina"  # Frase fija de ejemplo
    resultado = "Es un palíndromo" if es_palindromo(frase) else "No es un palíndromo"
    print(f"Frase: {frase}")
    print(resultado)

if __name__ == "__main__":
    main()
