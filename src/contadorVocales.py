def contar_vocales(texto):
    texto = texto.lower()  # Convertir todo a minúsculas
    vocales = "aeiou"
    contador = 0

    for letra in texto:
        print(f"Letra analizada: {letra}")  # 🔥 Ver cada letra
        if letra in vocales:
            print(f"Vocal encontrada: {letra}")  # 🔍 Confirmar vocal
            contador += 1

    print(f"Texto analizado: {texto}")
    print(f"Vocales contadas: {contador}")

    return contador
