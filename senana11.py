import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        return [producto.to_dict() for producto in self.productos.values()]

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id_producto: producto.to_dict() for id_producto, producto in self.productos.items()}, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id_producto: Producto(**producto) for id_producto, producto in data.items()}
        except FileNotFoundError:
            print("El archivo no existe.")

def menu():
    inventario = Inventario()
    inventario.cargar_inventario('inventario.json')

    while True:
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado.")

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
            print("Producto actualizado.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto.to_dict())
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            productos = inventario.mostrar_productos()
            for producto in productos:
                print(producto)

        elif opcion == '6':
            inventario.guardar_inventario('inventario.json')
            print("Inventario guardado.")

        elif opcion == '7':
            inventario.guardar_inventario('inventario.json')
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
