class Empleado:
    """
    Clase base que representa a un empleado.
    """

    def __init__(self, nombre, id_empleado, salario):
        """
        Inicializa los atributos de un empleado.

        Args:
            nombre (str): Nombre del empleado.
            id_empleado (int): Identificador único del empleado.
            salario (float): Salario del empleado.
        """
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__salario = salario

    def calcular_bono(self):
        """
        Calcula el bono del empleado.

        Returns:
            float: Bono del empleado.
        """
        return self.__salario * 0.1

    def mostrar_informacion(self):
        """
        Muestra la información del empleado.
        """
        print(f"Nombre: {self.__nombre}")
        print(f"ID: {self.__id_empleado}")
        print(f"Salario: {self.__salario}")
        print(f"Bono: {self.calcular_bono()}")


class Gerente(Empleado):
    """
    Clase derivada que representa a un gerente.
    """

    def __init__(self, nombre, id_empleado, salario, equipo):
        """
        Inicializa los atributos de un gerente.

        Args:
            nombre (str): Nombre del gerente.
            id_empleado (int): Identificador único del gerente.
            salario (float): Salario del gerente.
            equipo (list): Lista de empleados a cargo del gerente.
        """
        super().__init__(nombre, id_empleado, salario)
        self.__equipo = equipo

    def calcular_bono(self):
        """
        Calcula el bono del gerente.

        Returns:
            float: Bono del gerente.
        """
        bono_base = super().calcular_bono()
        return bono_base + (bono_base * 0.2)

    def mostrar_informacion(self):
        """
        Muestra la información del gerente y su equipo.
        """
        super().mostrar_informacion()
        print("Equipo a cargo:")
        for empleado in self.__equipo:
            print(f"- {empleado.get_nombre()}")


# Crear instancias de las clases
empleado1 = Empleado("Juan Pérez", 1001, 5000.0)
gerente1 = Gerente("María Gómez", 2001, 8000.0, [empleado1])

# Demostrar la funcionalidad del programa
empleado1.mostrar_informacion()
print()
gerente1.mostrar_informacion()
