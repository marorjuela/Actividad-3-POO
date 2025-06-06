# -*- coding: utf-8 -*-
"""Ejercicio propuesto página 231.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mqPPW_Be1UEr-x6VRnoX80s8bMwVVjAf
"""

class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self) -> str:
        return self.nombre

    def getDireccion(self) -> str:
        return self.direccion

    # setters
    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setDireccion(self, direccion: str):
        self.direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    # getters
    def getCarrera(self) -> str:
        return self.carrera

    def getSemestre(self) -> int:
        return self.semestre

    # setters
    def setCarrera(self, carrera: str):
        self.carrera = carrera

    def setSemestre(self, semestre: int):
        self.semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self) -> str:
        return self.departamento

    def getCategoria(self) -> str:
        return self.categoria

    def setDepartamento(self, departamento: str):
        self.departamento = departamento

    def setCategoria(self, categoria: str):
        self.categoria = categoria


if __name__ == "__main__":

    e = Estudiante("Ana Pérez", "C/ Falsa 123", "Ingeniería", 4)
    p = Profesor("Dr. López", "Av. Siempre Viva 742", "Matemáticas", "Titular")

    print("Estudiante:")
    print("  Nombre:   ", e.getNombre())
    print("  Dirección:", e.getDireccion())
    print("  Carrera:  ", e.getCarrera())
    print("  Semestre: ", e.getSemestre())

    print("\nProfesor:")
    print("  Nombre:      ", p.getNombre())
    print("  Dirección:   ", p.getDireccion())
    print("  Departamento:", p.getDepartamento())
    print("  Categoría:   ", p.getCategoria())