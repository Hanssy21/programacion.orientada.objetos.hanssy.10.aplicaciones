def contar_palabras():
    texto = input("Ingresa un texto: ")
    palabras = texto.split()  # Divide el texto en una lista de palabras
    print(f"El texto contiene {len(palabras)} palabras.")

if __name__ == "__main__":
    contar_palabras()  # Llama a la función principal