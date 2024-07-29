# Implemente un programa que solicite al usuario una fracción, con formato X/Y, donde cada uno de X e Y es un número entero, y
# luego muestra, como un porcentaje redondeado al número entero más cercano, donde se indicará la cantidad
#  de combustible en el tanque. Se debe tener en cuenta los siguientes casos:
# - Colocar E en caso X/Y sea menor a 1% del total
# - Colocar F en caso X/Y sea mayor a 99%.
# - En otro caso, devolver el valor en porcentaje %
# También debe tomar en cuenta los siguientes casos:
# - X y Y deben ser números enteros
# - X debe ser menor o igual a Y, y Y != 0
#De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar cualquier excepción 
# como ValueError o ZeroDivisionError.

#Solución

def obtener_fraccion():
    while True:
        try:
            # Solicita la fracción al usuario
            fraccion = input("Ingrese la fracción en formato X/Y: ")
            # Divide la entrada en X e Y
            X, Y = fraccion.split('/')
            # Convierte X e Y a enteros
            X = int(X)
            Y = int(Y)

            # Verifica que X sea menor o igual a Y y que Y no sea 0
            if X > Y or Y == 0:
                raise ValueError("X debe ser menor o igual a Y y Y debe ser distinto de 0")

            # Calcula el porcentaje
            porcentaje = (X / Y) * 100

            # Redondea el porcentaje al entero más cercano
            porcentaje_redondeado = round(porcentaje)

            # Verifica los casos especiales y da el resultado
            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{porcentaje_redondeado}%"
        
        except ValueError:
            print("Error. Ingresar una fracción en formato X/Y, donde X y Y son enteros y X <= Y, y Y != 0.")
        except ZeroDivisionError:
            print("Error. Y no puede ser 0.")

# Se invoca a la función para obtener el resultado
resultado = obtener_fraccion()
print("Nivel de combustible:", resultado)