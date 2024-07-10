class Vehiculo:
    """
    Clase Vehiculo que demuestra el uso de constructores y destructores.
    """
    def __init__(self, marca, modelo, año):
        """
        Constructor de la clase Vehiculo.
        Inicializa los atributos marca, modelo y año del objeto.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        print(f"Se ha creado un nuevo vehículo: {self.marca} {self.modelo} ({self.año}).")

    def __del__(self):
        """
        Destructor de la clase Vehiculo.
        Realiza una acción de limpieza o cierre de recursos (en este caso, simplemente imprime un mensaje).
        """
        print(f"El vehículo {self.marca} {self.modelo} ({self.año}) ha sido eliminado.")

# Crear objetos Vehiculo
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Honda", "Civic", 2018)

# Eliminar objetos Vehiculo (activará los destructores)
del vehiculo1
del vehiculo2

