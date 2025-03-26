import random

def adivina_el_numero(numero_secreto, intentos_max=10):
    intentos = 0
    for _ in range(intentos_max):
        intento_actual = random.randint(1, 50)
        intentos += 1

        if intento_actual == numero_secreto:
            return True, intentos  # ✅ Retorna True si adivina el número
    
    return False, intentos  # ❌ Retorna False si no lo logra
