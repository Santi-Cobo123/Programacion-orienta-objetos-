def ingreso_datos_diarios():
    """Función para ingresar las temperaturas diarias."""
    temperaturas_diarias = []
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
        temperaturas_diarias.append(data["temp"])
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

