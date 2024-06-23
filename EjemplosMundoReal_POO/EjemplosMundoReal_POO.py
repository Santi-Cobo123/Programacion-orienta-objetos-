class Prenda:
    def _init_(self, codigo, nombre, talla, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.talla = talla
        self.precio = precio
        self.disponible = True

    def vender(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True

class Tienda:
    def _init_(self, nombre):
        self.nombre = nombre
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def buscar_prenda(self, talla):
        for prenda in self.prendas:
            if prenda.talla == talla and prenda.disponible:
                return prenda
        return None

    def mostrar_existencias(self):
        for prenda in self.prendas:
            print(f"{prenda.nombre} ({prenda.codigo}) - Talla: {prenda.talla}, Precio: {prenda.precio}, Disponible: {'Sí' if prenda.disponible else 'No'}")

# Ejemplo de uso
tienda = Tienda("Ropa Elegante")

# Agregar prendas a la tienda
tienda.agregar_prenda(Prenda(101, "Camisa blanca", "M", 29.99))
tienda.agregar_prenda(Prenda(102, "Pantalón negro", "32", 49.99))
tienda.agregar_prenda(Prenda(103, "Vestido azul", "S", 59.99))

# Mostrar existencias
tienda.mostrar_existencias()

# Vender una prenda
prenda_disponible = tienda.buscar_prenda("M")
if prenda_disponible:
    prenda_disponible.vender()
    print(f"{prenda_disponible.nombre} vendido.")
else:
    print("Lo siento, no hay prendas disponibles de esa talla.")

# Mostrar existencias actualizadas
tienda.mostrar_existencias()