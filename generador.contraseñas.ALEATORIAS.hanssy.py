import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation  # Conjunto de caracteres posibles
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))  # Genera una contraseña aleatoria
    return contraseña

def main():
    longitud = int(input("¿Cuántos caracteres debe tener la contraseña? "))
    contraseña = generar_contraseña(longitud)  # Genera la contraseña
    print(f"La contraseña generada es: {contraseña}")

if __name__ == "__main__":
    main()  # Llama a la función principal