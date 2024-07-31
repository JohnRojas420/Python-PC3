# Crea una clase llamada Punto con sus dos coordenadas X e Y.
# Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
# Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
# Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
# Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
# (Optativo)Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla.
#Solución
# En primer lugar, se importa el módulo math
import math
#Se define la clase punto, inicialización y string
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.x != 0 and self.y == 0:
            return "Eje X"
        else:
            return "Origen"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
    
# Ejemplos de uso:
p1 = Punto(4, 5)
p2 = Punto(8, 10)

print(p1)  # (4, 5)
print(p2)  # (8, 10)

print(p1.cuadrante())  # Primer cuadrante
print(Punto(-4, 5).cuadrante())  # Segundo cuadrante
print(Punto(-4, -5).cuadrante())  # Tercer cuadrante
print(Punto(4, -5).cuadrante())  # Cuarto cuadrante
print(Punto(0, 5).cuadrante())  # Eje Y
print(Punto(4, 0).cuadrante())  # Eje X
print(Punto(0, 0).cuadrante())  # Origen

print(p1.vector(p2))  
print(p1.distancia(p2))  