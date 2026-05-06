"""
Ejercicio 1
Crear un programa donde:
Crear una clase: Alumno
crear sus atributos: Nombre, Apellido, Edad y Curso
crearle un método: programar (), que imprima  “ el alumno (nombre) está programando”

Crear el objeto Alumno instanciando con el método programar()

Los datos solicitados que el alumno completará, tiene que ser indistinto
si es en mayuscula o minuscula
"""

class Alumno:
    def __init__(self, Nombre, Apellido, Edad, Curso):
        self.Nombre = Nombre.capitalize()#Asi ponemos mayuscula solo la primera letra
        self.Apellido = Apellido.capitalize()
        self.Edad = Edad
        self.curso = Curso

    def Programar(self):
        print(f"{self.Nombre} está programando")
        
# Instanciando el objeto Alumno
alumno = Alumno("Christian", "Barrios", 22, "Sexto Programación")
alumno.Programar()

#Entendi por indistinto que el alumno puede ingresar los datos como sea, pero en los que yo requiera mayuscula, los pondria.