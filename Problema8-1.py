# Importando el módulo operaciones.py as Problema8
import Problema8

# Dando un ejemplo del uso del módulo en las operaciones fundamentales
a = 16
b = 8
c = "cuatro"

print("Suma:", Problema8.suma(a, b))         
print("Resta:", Problema8.resta(a, b))       
print("Producto:", Problema8.producto(a, b)) 
print("División:", Problema8.division(a, b)) 

# Algunos ejemplos con errores: 
print("Suma con error:", Problema8.suma(a, c))         # Error: Tipo de dato no válido.
print("División por cero:", Problema8.division(a, 0))  # Error: No es posible dividir entre cero.