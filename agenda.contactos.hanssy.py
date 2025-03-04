class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre  # Atributo nombre
        self.telefono = telefono  # Atributo teléfono

class Agenda:
    def __init__(self):
        self.contactos = []  # Inicializa una lista vacía de contactos
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)  # Agrega un contacto a la lista
    
    def eliminar_contacto(self, nombre):
        self.contactos = [cont for cont in self.contactos if cont.nombre != nombre]  # Elimina el contacto por nombre
    
    def buscar_contacto(self, nombre):
        for cont in self.contactos:  # Recorre la lista de contactos
            if cont.nombre == nombre:
                return cont  # Si encuentra el contacto, lo devuelve
        return None  # Si no encuentra el contacto, devuelve None
    
    def listar_contactos(self):
        for cont in self.contactos:  # Recorre la lista de contactos
            print(f"{cont.nombre} - {cont.telefono}")  # Muestra la información de cada contacto

def main():
    agenda = Agenda()  # Crea una instancia de la clase Agenda
    while True:
        accion = input("Elige una opción: agregar, eliminar, buscar, listar, salir: ").lower()  # Solicita una acción
        
        if accion == "agregar":
            nombre = input("Nombre del contacto: ")  # Solicita el nombre
            telefono = input("Teléfono: ")  # Solicita el teléfono
            agenda.agregar_contacto(Contacto(nombre, telefono))  # Agrega el contacto a la agenda
        
        elif accion == "eliminar":
            nombre = input("Nombre del contacto a eliminar: ")  # Solicita el nombre a eliminar
            agenda.eliminar_contacto(nombre)  # Elimina el contacto
        
        elif accion == "buscar":
            nombre = input("Nombre del contacto a buscar: ")  # Solicita el nombre a buscar
            contacto = agenda.buscar_contacto(nombre)  # Busca el contacto
            if contacto:
                print(f"{contacto.nombre} - {contacto.telefono}")  # Si lo encuentra, muestra la información
            else:
                print("Contacto no encontrado")  # Si no lo encuentra, muestra un mensaje
                
        elif accion == "listar":
            agenda.listar_contactos()  # Muestra todos los contactos
        
        elif accion == "salir":
            break  # Termina el programa
        else:
            print("Opción no válida")  # Muestra un mensaje si la opción no es válida

if __name__ == "__main__":
    main()  # Ejecuta la función principal