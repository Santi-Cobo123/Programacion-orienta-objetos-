import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
        return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    return None

def editar_y_guardar_codigo(ruta_script, codigo):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'w') as archivo:
            archivo.write(codigo)
        print(f"Código de {ruta_script} guardado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")
        print("e - Editar y guardar un script")

        eleccion = input("Elige un script para ver su código, 'e' para editar, o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion == 'e':
            script_a_editar = input("Ingresa el número del script que deseas editar: ")
            if script_a_editar in opciones:
                ruta_script = os.path.join(ruta_base, opciones[script_a_editar])
                codigo_actual = mostrar_codigo(ruta_script)
                if codigo_actual:
                    codigo_editado = input("Ingresa el código modificado:\n")
                    editar_y_guardar_codigo(ruta_script, codigo_editado)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
