# Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos para:
# 1. Display - Debe mostrar toda la información del estudiante (nombre y número de registro).
# 2. setAge - Debe asignar la edad al estudiante
# 3. setNota - Debe asignar las notas al estudiante.

# Solución:
# Se crea la clase Alumno y luego se define la inicialización de características
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")
# Haciendo los métodos para setAge y setNota  
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, nota):
        self.nota = nota

# Se crea un objeto de tipo Alumno y se le asigna valores, nombre y código
alumno1 = Alumno("Marco Pérez", "P148965M")

# Se asigna los valores de edad y nota al alumno
alumno1.setAge(20)
alumno1.setNota(18)

# Mostrar la información del alumno
alumno1.display()