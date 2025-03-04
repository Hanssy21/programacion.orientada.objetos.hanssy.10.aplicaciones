def convertir_temperatura():
    print("Conversor de temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    
    # Solicita al usuario que elija una opción
    opcion = int(input("Elige una opción (1 o 2): "))
    
    if opcion == 1:
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = (celsius * 9/5) + 32  # Fórmula para convertir de Celsius a Fahrenheit
        print(f"{celsius}°C es igual a {fahrenheit}°F.")
    
    elif opcion == 2:
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9  # Fórmula para convertir de Fahrenheit a Celsius
        print(f"{fahrenheit}°F es igual a {celsius}°C.")
    
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    convertir_temperatura()  # Llama a la función principal