# Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y ancho. 
# La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los atributos de la clase.
# Además cree una clase CUADRADO que heredé de rectangulo. Cree un objeto de tipo rectangulo y 1 de tipo cuadrado.

# Solución

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        # Un cuadrado es un rectángulo con lados iguales
        super().__init__(lado, lado) 

# Crear un objeto de tipo RECTANGULO
rectangulo = RECTANGULO(6, 8)
area_rectangulo = rectangulo.calcular_area()
print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {area_rectangulo}")

# Crear un objeto de tipo CUADRADO 
cuadrado = CUADRADO(9)
area_cuadrado = cuadrado.calcular_area()
print(f"El área del cuadrado con lado {cuadrado.largo} es: {area_cuadrado}")