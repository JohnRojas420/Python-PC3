# Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase Catálogo y Producto,
# realizar un objeto dentro de un catálogo productos el cual debe tener un método para agregar productos y otra
# para mostrar toda la lista de productos.
# Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede agregar más atributos
# a los productos para que se puedan hacer otras funcionalidades. Cree 3 objetos de tipo producto y agregalos 
# al catálogo. Colocar ejemplos empleandolos métodos de catálogo.

#Solución:

# Definiendo clases para Producto y Catálogo
class Producto:
    def __init__(self, nombre, marca, precio, año):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - {self.marca} - ${self.precio} - {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

    def buscar_por_marca(self, marca):
        return [producto for producto in self.productos if producto.marca.lower() == marca.lower()]
    
# Creando tres funciones de Producto
producto1 = Producto("Aceite Premium", "Primor", 13.89, 2022)
producto2 = Producto("Paquete Gaseosa 3L", "Inca Cola", 41.50, 2024)
producto3 = Producto("Saco de Arroz", "Faraón", 208.50, 2023)

# Crear instancia de Catalogo y agregar productos
catalogo = Catalogo()
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrando todos los productos antes definidos:
print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()

# Aplicando filtro de productos por año
año_filtrar = 2024
print(f"\nProductos del año {año_filtrar}:")
productos_filtrados = catalogo.filtrar_por_año(año_filtrar)
for producto in productos_filtrados:
    print(producto)

# Buscar productos por marca
marca_buscar = "Faraón"
print(f"\nProductos de la marca {marca_buscar}:")
productos_buscados = catalogo.buscar_por_marca(marca_buscar)
for producto in productos_buscados:
    print(producto)