class InformacionClimatica:
    """Clase que representa la información diaria del clima."""
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperatura_diaria(self):
        """Método para ingresar la temperatura diaria."""
        datos_diarios = [
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
        for data in datos_diarios:
            self.temperaturas_diarias.append(data["temp"])

    def calcular_promedio_semanal(self):
        """Método para calcular el promedio semanal de las temperaturas."""
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

def main():
    """Función principal para ejecutar el programa."""
    informacion_climatica = InformacionClimatica()
    informacion_climatica.ingresar_temperatura_diaria()
    promedio_semanal = informacion_climatica.calcular_promedio_semanal()
    print(f"El promedio semanal de las temperaturas es: \[{promedio_semanal:.2f}\]°C")

if __name__ == "__main__":
    main()
