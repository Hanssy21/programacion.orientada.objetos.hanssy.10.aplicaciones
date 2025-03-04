def convertir_unidades():
    print("Conversor de unidades")
    print("1. Kilómetros a millas")
    print("2. Millas a kilómetros")
    print("3. Kilogramos a libras")
    print("4. Libras a kilogramos")

    opcion = int(input("Elige una opción (1-4): "))

    if opcion == 1:
        km = float(input("Ingresa la distancia en kilómetros: "))
        print(f"{km} km es igual a {km * 0.621371} millas.")
    elif opcion == 2:
        millas = float(input("Ingresa la distancia en millas: "))
        print(f"{millas} millas es igual a {millas / 0.621371} kilómetros.")
    elif opcion == 3:
        kg = float(input("Ingresa el peso en kilogramos: "))
        print(f"{kg} kg es igual a {kg * 2.20462} libras.")
    elif opcion == 4:
        libras = float(input("Ingresa el peso en libras: "))
        print(f"{libras} libras es igual a {libras / 2.20462} kilogramos.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    convertir_unidades()  # Llama a la función principal