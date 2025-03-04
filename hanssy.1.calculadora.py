class Calculadora:
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

def main():
    calc = Calculadora()  # Se crea una instancia de la clase Calculadora
    operacion = input("Elige una operación (+, -, *, /): ")  # Se solicita al usuario que elija una operación
    a = float(input("Ingresa el primer número: "))  # Se solicita el primer número
    b = float(input("Ingresa el segundo número: "))  # Se solicita el segundo número
    
    if operacion == "+":
        print(calc.suma(a, b))  # Si la operación es suma, se llama al método suma
    elif operacion == "-":
        print(calc.resta(a, b))  # Si la operación es resta, se llama al método resta
    elif operacion == "*":
        print(calc.multiplicacion(a, b))  # Si la operación es multiplicación, se llama al método multiplicación
    elif operacion == "/":
        print(calc.division(a, b))  # Si la operación es división, se llama al método división
    else:
        print("Operación no válida")  # Si la operación no es válida, se muestra un mensaje de error

if __name__ == "__main__":
    main()  # Se ejecuta la función principal