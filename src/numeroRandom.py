import random

def generar_numero_aleatorio():
    return random.randint(1, 100)

def main():
    numero = generar_numero_aleatorio()
    print(f"Número aleatorio generado: {numero}")

if __name__ == "__main__":
    main()
