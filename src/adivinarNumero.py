import random

numero_secreto = random.randint(1, 50)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 50): "))
    intentos += 1

    if intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Muy alto, intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
