from .libro.py import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        return resultados