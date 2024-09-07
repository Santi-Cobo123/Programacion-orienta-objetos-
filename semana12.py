class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Tupla (nombre, apellido)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos

    def añadir_libro(self, libro):
        """Añadir un libro a la biblioteca."""
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        """Quitar un libro de la biblioteca."""
        if isbn in self.libros:
            removed_book = self.libros.pop(isbn)
            print(f"Libro quitado: {removed_book}")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario."""
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya existe.")

    def dar_baja_usuario(self, id_usuario):
        """Dar de baja un usuario existente."""
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {id_usuario}")
        else:
            print("El ID de usuario no se encuentra registrado.")

    def prestar_libro(self, isbn, id_usuario):
        """Facilitar el préstamo de un libro a un usuario."""
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    usuario.libros_prestados.append(libro)
                    print(f"Libro prestado a {usuario.nombre}: {libro}")
                    return
        print("No se puede prestar el libro. Verifique el ISBN o el ID de usuario.")

    def devolver_libro(self, isbn, id_usuario):
        """Facilitar la devolución de un libro."""
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                for libro in usuario.libros_prestados:
                    if libro.isbn == isbn:
                        usuario.libros_prestados.remove(libro)
                        print(f"Libro devuelto por {usuario.nombre}: {libro}")
                        return
        print("No se puede devolver el libro. Verifique el ISBN o el ID de usuario.")

    def buscar_libro(self, criterio, valor):
        """Buscar libros por título, autor o categoría."""
        resultados = []
        for libro in self.libros.values():
            if (criterio == 'titulo' and valor.lower() in libro.titulo.lower()) or \
               (criterio == 'autor' and valor.lower() in libro.autor[0].lower()) or \
               (criterio == 'categoria' and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        """Mostrar una lista de todos los libros actualmente prestados a un usuario."""
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                if usuario.libros_prestados:
                    print(f"Libros prestados a {usuario.nombre}:")
                    for libro in usuario.libros_prestados:
                        print(f"- {libro}")
                else:
                    print(f"{usuario.nombre} no tiene libros prestados.")
                return
        print("El ID de usuario no se encuentra registrado.")


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien años de soledad", ("Gabriel", "García Márquez"), "Ficción", "978-3-16-148410-0")
    libro2 = Libro("1984", ("George", "Orwell"), "Ficción", "978-0-452-28423-4")

    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Crear usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("Ana Gómez", "002")

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("978-3-16-148410-0", "001")
    biblioteca.prestar_libro("978-0-452-28423-4", "002")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("001")
    biblioteca.listar_libros_prestados("002")

    # Devolver un libro
    biblioteca.devolver_libro("978-3-16-148410-0", "001")

    # Buscar libros
    print("Buscar por autor 'George':")
    libros_encontrados = biblioteca.buscar_libro('autor', 'George')
    for libro in libros_encontrados:
        print(libro)

    # Quitar un libro
    biblioteca.quitar_libro("978-0-452-28423-4")
