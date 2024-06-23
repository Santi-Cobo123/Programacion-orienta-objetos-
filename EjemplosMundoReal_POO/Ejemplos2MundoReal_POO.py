class Habitacion:
    def _init_(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

class Hotel:
    def _init_(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def buscar_habitacion(self, tipo):
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and habitacion.disponible:
                return habitacion
        return None

    def mostrar_disponibilidad(self):
        for habitacion in self.habitaciones:
            print(f"Habitación {habitacion.numero} ({habitacion.tipo}): {'Disponible' if habitacion.disponible else 'Ocupada'}")

# Ejemplo de uso
hotel = Hotel("Hotel Magnolia")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(Habitacion(101, "individual", 80.0))
hotel.agregar_habitacion(Habitacion(102, "doble", 120.0))
hotel.agregar_habitacion(Habitacion(103, "suite", 200.0))

# Mostrar disponibilidad de habitaciones
hotel.mostrar_disponibilidad()

# Reservar una habitación
habitacion_disponible = hotel.buscar_habitacion("doble")
if habitacion_disponible:
    habitacion_disponible.reservar()
    print(f"Habitación {habitacion_disponible.numero} reservada.")
else:
    print("Lo siento, no hay habitaciones disponibles de ese tipo.")

# Mostrar disponibilidad actualizada
hotel.mostrar_disponibilidad()