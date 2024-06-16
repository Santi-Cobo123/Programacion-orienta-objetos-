class InformacionClimatica:
    """Clase que representa la información diaria del clima."""
    def __init__(self):
        self.temperaturas_diarias = []


    def ingresar_temperatura_diaria(self):
        """Método para ingresar la temperatura diaria."""
        for dia in range(1, 8):
            temperatura = float(input(f"Ingresa la temperatura del día {dia}: "))
            self.temperaturas_diarias.append(temperatura)

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