
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  
        self.carrera = carrera

    def presentarse(self):
        super().presentarse()
        print(f"Estudio la carrera de {self.carrera}.")

estudiante1 = Estudiante("Carlos", 21, "Ingeniería Informática")
estudiante1.presentarse()
