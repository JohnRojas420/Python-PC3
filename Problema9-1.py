
import Problema9

def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Error: El número debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Tipo de dato no válido. Por favor, ingrese un número.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = validar_numero_positivo("Ingrese el radio del círculo: ")
            circulo = Problema9.Circulo(radio)
            print(f"El área del círculo es: {circulo.area()}")

        elif opcion == '2':
            ancho = validar_numero_positivo("Ingrese el ancho del rectángulo: ")
            alto = validar_numero_positivo("Ingrese el alto del rectángulo: ")
            rectangulo = Problema9.Rectangulo(ancho, alto)
            print(f"El área del rectángulo es: {rectangulo.area()}")

        elif opcion == '3':
            lado = validar_numero_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = Problema9.Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.area()}")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()