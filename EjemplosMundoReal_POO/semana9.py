class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio del producto

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos

    def añadir_producto(self, producto):
        # Asegurarse de que el ID sea único
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)  # Añadir producto a la lista

    def eliminar_producto(self, id_producto):
        # Eliminar producto por ID
        self.productos = [p for p in self.productos if p.get_id() != id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualizar cantidad o precio de un producto por ID
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Buscar productos por nombre (puede haber nombres similares)
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        # Mostrar todos los productos en el inventario
        if not self.productos:
            print("El inventario está vacío.")
            return
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")


def menu():
    inventario = Inventario()

    # Añadir productos iniciales
    inventario.añadir_producto(Producto("001", "Aceite", 10, 2.50))
    inventario.añadir_producto(Producto("002", "Girasol", 20, 3.00))
    inventario.añadir_producto(Producto("003", "Sal", 30, 1.20))
    inventario.añadir_producto(Producto("004", "Azúcar", 15, 1.50))

    while True:
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se desea cambiar): ")
            precio = input("Nuevo precio (dejar vacío si no se desea cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre)
            for p in productos_encontrados:
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
