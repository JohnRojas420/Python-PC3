# Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El menú para utilizar
# deberá tener las siguientes funcionalidades:
# 1. Calcular el área de un circulo
# 2. Calcular el área de un rectangulo
# 3. Calcular el área de un cuadrado
# 4. Salir.
# Deberá emplear un método que valide que los datos ingresados sean números validos y positivos en caso corresponda.

# Solución:
# Importando el módulo MATH

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado