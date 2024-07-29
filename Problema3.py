# Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase 
# “CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
# Cree 2 objetos de tipo circulo y calcule su área.

#Solución:

# Primero de debe improtar el módulo "math"
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# Definición y asignación de valores
circulo1 = CIRCULO(8)
circulo2 = CIRCULO(12)

# Se definen área1 y área2 y se calcula el área de los dos círculos
area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

print(f"El área del círculo con radio {circulo1.radio} es: {area1}")
print(f"El área del círculo con radio {circulo2.radio} es: {area2}")