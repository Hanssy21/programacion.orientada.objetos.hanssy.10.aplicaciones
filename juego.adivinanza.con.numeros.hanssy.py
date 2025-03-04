import random  # Importa el módulo random para generar números aleatorios

def jugar():
    numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos = 0  # Inicializa el contador de intentos
    while True:
        intento = int(input("Adivina el número entre 1 y 100: "))  # Solicita un número al usuario
        intentos += 1  # Incrementa el contador de intentos
        if intento < numero_secreto:
            print("El número es mayor.")  # Si el número es menor, avisa al usuario
        elif intento > numero_secreto:
            print("El número es menor.")  # Si el número es mayor, avisa al usuario
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")  # Si el número es correcto, muestra el mensaje de éxito
            break  # Sale del bucle cuando se adivina el número

if __name__ == "__main__":
    jugar()  # Llama a la función para iniciar el juego