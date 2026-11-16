def calculadora():
    print("=== Calculadora en Python ===")
    print("Operaciones: + (suma), - (resta), * (multiplicación), / (división)")

    while True:
        operacion = input(
            "\nElige una operación (+, -, *, /) o 's' para salir: ").strip()

        if operacion.lower() == 's':
            print("¡Hasta luego!")
            break

        if operacion not in ['+', '-', '*', '/']:
            print("Operación no válida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor ingresa solo números válidos.")
            continue

        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1 / num2}")


if __name__ == "__main__":
    calculadora()
