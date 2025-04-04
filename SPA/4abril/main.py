from punto import Punto
from grafo import Grafo
from typing import List
from pprint import pprint
from matplotlib import pyplot as plt

puntos: List[Punto] = []

punto1 = Punto(x=100, y=100, red=255, green=0, blue=0, radio=25)
punto2 = Punto(x=100, y=400, red=0, green=255, blue=0, radio=25)
punto3 = Punto(x=400, y=100, red=0, green=0, blue=255, radio=25)
punto4 = Punto(x=400, y=400, red=255, green=255, blue=0, radio=25)
punto5 = Punto(x=250, y=250, red=0, green=255, blue=255, radio=25)

puntos.append(punto1)
puntos.append(punto2)
puntos.append(punto3)
puntos.append(punto4)
puntos.append(punto5)

pprint(puntos)

fig, ax = plt.subplots()
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)
for punto in puntos:
    color = (punto.red/255, punto.green/255, punto.blue/255)
    ax.scatter(x=punto.x, y=punto.y, color=color, s=punto.radio, alpha=.8)
    ax.text(punto.x, punto.y, str(punto), ha="center", va='center')
#plt.show()

grafo = Grafo(puntos)
pprint(grafo.grafo)

grafo.agregar_conexion(punto1, punto3)
grafo.agregar_conexion(punto1, punto2)
grafo.agregar_conexion(punto2, punto4)
grafo.agregar_conexion(punto4, punto3)
grafo.agregar_conexion(punto1, punto5)
grafo.agregar_conexion(punto2, punto5)
grafo.agregar_conexion(punto3, punto5)
grafo.agregar_conexion(punto4, punto5)
pprint(grafo.grafo)

fig2, ax2 = plt.subplots()

for punto in grafo.grafo.keys():
    for adyacentes in grafo.grafo[punto]:
        ax2.plot([punto.x, adyacentes.x], [punto.y, adyacentes.y], color="black")
        print(adyacentes)

plt.show()