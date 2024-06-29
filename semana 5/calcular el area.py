# Este programa calcula el área de un rectángulo a partir de la base y altura ingresadas por el usuario.

# Pedir al usuario que ingrese la base y la altura del rectángulo
def calculate_rectangle_area():
    """
    Calcula el área de un rectángulo.
    """
    length = float(input("Ingresa la longitud del rectángulo: "))
    width = float(input("Ingresa el ancho del rectángulo: "))

    area = length * width

    print(f"El área del rectángulo es: [\\{area:.2f}\\] unidades cuadradas.")


if __name__ == "__main__":
    calculate_rectangle_area()


