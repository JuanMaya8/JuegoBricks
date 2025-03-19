import random

def adivina_el_numero(numero_secreto, intentos_max=10):
    intentos = 0
    for intento in range(1, intentos_max + 1):
        intento_actual = random.randint(1, 50)
        intentos += 1

        if intento_actual < numero_secreto:
            print(f"Intento {intentos}: {intento_actual} es muy bajo.")
        elif intento_actual > numero_secreto:
            print(f"Intento {intentos}: {intento_actual} es muy alto.")
        else:
            print(f"¡Número adivinado! Era {numero_secreto}. Adivinado en {intentos} intentos.")
            return

    print(f"No se adivinó el número {numero_secreto} en {intentos_max} intentos.")

def main():
    numero_secreto = random.randint(1, 50)  # Número secreto aleatorio
    adivina_el_numero(numero_secreto)

if __name__ == "__main__":
    main()
