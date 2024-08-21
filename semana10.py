import os

class Producto:
    def _init_(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def _init_(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        nombre, cantidad, precio = linea.strip().split(',')
                        self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
                print("Inventario cargado exitosamente.")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            open(self.archivo, 'w').close()

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto al inventario y lo guarda en el archivo."""
        if nombre not in self.productos:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
            self.guardar_inventario()
            print(f"Producto '{nombre}' agregado exitosamente.")
        else:
            print(f"El producto '{nombre}' ya existe en el inventario.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza un producto existente en el inventario."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre].cantidad = cantidad
            if precio is not None:
                self.productos[nombre].precio = precio
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")

# Ejemplo de uso
if _name_ == "_main_":
    inventario = Inventario()
    inventario.agregar_producto("Manzana", 100, 0.5)
    inventario.actualizar_producto("Manzana", 120)
    inventario.eliminar_producto("Manzana")