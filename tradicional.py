def ingreso_datos_diarios():
    """Función para ingresar las temperaturas diarias."""
    temperaturas_diarias = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingresa la temperatura del día {dia}: "))
        temperaturas_diarias.append(temperatura)
    return temperaturas_diarias

def calcular_promedio_semanal(temperaturas_semanales):
    """Función para calcular el promedio semanal de las temperaturas."""
    promedio = sum(temperaturas_semanales) / len(temperaturas_semanales)
    return promedio

def main():
    """Función principal para ejecutar el programa."""
    temperaturas_semanales = ingreso_datos_diarios()
    promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
    print(f"El promedio semanal de las temperaturas es: \[{promedio_semanal:.2f}\]°C")

if __name__ == "__main__":
    main()
