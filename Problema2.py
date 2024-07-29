# Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
# la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada calificación 
# en un entero. Deberá utilizar una sentencia try/except para informar al usuario cuando los valores introducidos
#  no puedan ser convertidos debido a un error de tipeo o formato. (Los métodos de cadena le serán de utilidad)

#Solución:

def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario una lista de calificaciones separadas por comas
            entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales
            lista_calificaciones = entrada.split(',')
            
            # Se debe convertir cada calificación en un número entero
            calificaciones = [int(calificacion.strip()) for calificacion in lista_calificaciones]
            
            # Imprimir la lista de calificaciones
            print("Las calificaciones son:", calificaciones)
            break
        
        except ValueError:
            # Informar al usuario sobre el error de conversión
            print("Error: Asegúrese de que todas las calificaciones sean números enteros y estén correctamente separadas por comas.")
            print("Por favor, inténtelo de nuevo.")

obtener_calificaciones() 
