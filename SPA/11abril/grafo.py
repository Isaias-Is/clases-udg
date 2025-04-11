from punto import Punto
from typing import List, Dict, Set

class Grafo:
	def __init__(self, puntos: List[Punto]):
		self.grafo: Dict[Punto, Set[Punto]] = {punto: set() for punto in puntos}

	def agregar_conexion(self, punto1: Punto, punto2: Punto):
		uno2 = 2
		if (not isinstance(punto1, Punto) and (uno2 := 1)) or (not isinstance(punto2, Punto)):
			raise ValueError(f"El punto {uno2} no es válido.")
		if punto1 == punto2:
			raise ValueError("ERROR: Se esta tratanto de conectar un punto a si mismo. Los puntos deben ser diferentes.")
		self.grafo[punto1].add(punto2)
		self.grafo[punto2].add(punto1)

	def eliminar_conexion(self, punto1: Punto, punto2: Punto):
		malPunto = 0
		if not isinstance(punto1, Punto): 
			malPunto = 1
		if not isinstance(punto2, Punto):
			raise ValueError(f"El punto {malPunto} no es válido.")
		if punto1 == punto2:
			raise ValueError("ERROR: Se esta tratanto de conectar un punto a si mismo. Los puntos deben ser diferentes.")
		if punto1 not in self.grafo[punto2]:
			raise ValueError("No hay conexión entre los puntos.")
		self.grafo[punto1].remove(punto2)
		self.grafo[punto2].remove(punto1)