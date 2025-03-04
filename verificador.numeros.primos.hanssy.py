def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(n ** 0.5) + 1):  # Recorre hasta la raíz cuadrada del número
        if n % i == 0:
            return False  # Si es divisible, no es primo
    return True  # Si no es divisible por ningún número, es primo

def main():
    numero = int(input("Ingresa un número para verificar si es primo: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

if __name__ == "__main__":
    main()  # Llama a la función principal