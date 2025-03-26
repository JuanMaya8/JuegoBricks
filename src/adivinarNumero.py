def adivina_el_numero(numero_secreto, intentos_max=10):
    intentos = 0
    for intento_actual in range(1, intentos_max + 1):  # Intentos desde 1 hasta intentos_max
        intentos += 1
        if intento_actual == numero_secreto:  # ✅ Prueba sin random
            return True, intentos
    
    return False, intentos  # ❌ No adivinó
