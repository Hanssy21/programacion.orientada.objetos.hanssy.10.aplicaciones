class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad
        self.curso = curso    # Atributo curso

class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = []  # Inicializa una lista vacía de estudiantes
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)  # Agrega un estudiante a la lista
    
    def eliminar_estudiante(self, nombre):
        self.estudiantes = [est for est in self.estudiantes if est.nombre != nombre]  # Elimina al estudiante con el nombre dado
    
    def listar_estudiantes(self):
        for est in self.estudiantes:  # Recorre la lista de estudiantes
            print(f"{est.nombre} - {est.edad} años - Curso: {est.curso}")  # Imprime la información de cada estudiante

def main():
    gestion = GestionEstudiantes()  # Crea una instancia de la clase GestionEstudiantes
    while True:
        accion = input("Elige una opción: agregar, eliminar, listar, salir: ").lower()  # Pide una acción
        
        if accion == "agregar":
            nombre = input("Nombre del estudiante: ")  # Solicita el nombre
            edad = int(input("Edad: "))  # Solicita la edad
            curso = input("Curso: ")  # Solicita el curso
            gestion.agregar_estudiante(Estudiante(nombre, edad, curso))  # Crea un nuevo estudiante y lo agrega
        
        elif accion == "eliminar":
            nombre = input("Nombre del estudiante a eliminar: ")  # Solicita el nombre del estudiante a eliminar
            gestion.eliminar_estudiante(nombre)  # Elimina al estudiante por su nombre
        
        elif accion == "listar":
            gestion.listar_estudiantes()  # Muestra la lista de estudiantes
        
        elif accion == "salir":
            break  # Termina el programa
        else:
            print("Opción no válida")  # Si la opción no es válida, muestra un mensaje

if __name__ == "__main__":
    main()  # Ejecuta la función principal