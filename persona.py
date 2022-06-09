class Persona():
    def __init__(self, nombre, edad, conocimientos):
        self.__nombre = nombre
        self.__edad = edad
        self.__conocimientos = conocimientos

    @property
    def conocimientos(self):
        return self.__conocimientos

    @conocimientos.setter
    def conocimientos(self, num_conocimientos):
        self.__conocimientos = num_conocimientos

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, conocimientos=0):
        Persona.__init__(self, nombre, edad, conocimientos)

    def estudiar(self):
        self.conocimientos += 5


class Profesor(Persona):
    def __init__(self, nombre, edad, conocimientos=100):
        Persona.__init__(self, nombre, edad, conocimientos)

    def ensenar(self, estudiante):
        self.conocimientos += 1
        estudiante.conocimientos += 10
