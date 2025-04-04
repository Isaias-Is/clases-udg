from punto import Punto
from typing import List, Dict, Set

class Grafo:
	def __init__(self, puntos: List[Punto]):
		self.grafo: Dict[Punto, Set[Punto]] = {punto: set() for punto in puntos}

	def agregar_conexion(self, punto1: Punto, punto2: Punto):
		self.grafo[punto1].add(punto2)
		self.grafo[punto2].add(punto1)
