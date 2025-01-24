from personaje import Personaje
from typing import List

class Administrador:
    def __init__(self):
        self.lista: List[Personaje] = []
    
    def agregar(self, personaje: Personaje):
        self.lista.append(personaje)

    def mostrar(self):
        for personaje in self.lista:
            print("Tipo:", personaje.tipo)
            print("Fuerza:", personaje.fuerza)
            print("Salud:", personaje.salud)