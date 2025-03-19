def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = 25  # Valor fijo de ejemplo
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C es igual a {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
