class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre  # Atributo nombre
        self.cantidad = cantidad  # Atributo cantidad
        self.precio = precio  # Atributo precio

class Inventario:
    def __init__(self):
        self.productos = []  # Inicializa una lista vacía de productos
    
    def agregar_producto(self, producto):
        self.productos.append(producto)  # Agrega un producto a la lista
    
    def eliminar_producto(self, nombre):
        self.productos = [prod for prod in self.productos if prod.nombre != nombre]  # Elimina el producto por nombre
    
    def listar_productos(self):
        for prod in self.productos:  # Recorre la lista de productos
            print(f"{prod.nombre} - Cantidad: {prod.cantidad} - Precio: {prod.precio}")  # Muestra la información de cada producto

def main():
    inventario = Inventario()  # Crea una instancia de Inventario
    while True:
        accion = input("Elige una opción: agregar, eliminar, listar, salir: ").lower()  # Solicita una acción
        
        if accion == "agregar":
            nombre = input("Nombre del producto: ")  # Solicita el nombre del producto
            cantidad = int(input("Cantidad: "))  # Solicita la cantidad
            precio = float(input("Precio: "))  # Solicita el precio
            inventario.agregar_producto(Producto(nombre, cantidad, precio))  # Agrega el producto al inventario
        
        elif accion == "eliminar":
            nombre = input("Nombre del producto a eliminar: ")  # Solicita el nombre del producto a eliminar
            inventario.eliminar_producto(nombre)  # Elimina el producto por nombre
        
        elif accion == "listar":
            inventario.listar_productos()  # Muestra los productos en el inventario
        
        elif accion == "salir":
            break  # Termina el programa
        else:
            print("Opción no válida")  # Muestra un mensaje si la opción no es válida

if __name__ == "__main__":
    main()  # Ejecuta la función principal