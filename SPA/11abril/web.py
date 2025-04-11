from pprint import pprint
from nicegui import ui
from typing import List
import matplotlib.pyplot as plt
from grafo import Grafo
from punto import Punto, generar_punto

puntos: List[Punto] = [generar_punto() for _ in range(10)]
pprint(puntos)
grafo = Grafo(puntos)
pprint(grafo.grafo)
with ui.header().classes('bg-gray-500 bold'):
    ui.markdown('## Grafos')

def agregar_conexion():
    origen = origen_select.value
    destino =  desitno_select.value
    try:
        grafo.agregar_conexion(origen, destino)
    except ValueError as e:
        ui.notify(str(e), type='negative')
        return
    dibujar_adyacentes()

def eliminar_conexion():
    origen = origen_select.value
    destino =  desitno_select.value
    try:
        grafo.eliminar_conexion(origen, destino)
    except ValueError as e:
        ui.notify(str(e), type='negative')
        return
    dibujar_adyacentes()

def dibujar_adyacentes():
    with plot:
        plt.cla()
        plt.xlim(0,500)
        plt.ylim(0,500)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Grafo")
        plt.gca().set_facecolor(color="#AABBCC")

        for punto in grafo.grafo.keys():
            color = [punto.red/255, punto.green/255, punto.blue/255]
            plt.scatter(punto.x, punto.y, s=punto.radio, color=color, alpha=.8)
            plt.text(punto.x, punto.y, str(punto), ha="center", va="center")

        for punto, adyacentes in grafo.grafo.items():
            for adyacente in adyacentes:
                plt.plot([punto.x, adyacente.x], [punto.y, adyacente.y], color='black', linewidth=1)


with ui.row().classes('w-full h-full gap-0 border-2 border-gray-300'):
    with ui.column().classes('w-1/2'):
        ui.label("Columna 1").classes('text-xl bold')
        with ui.row().classes('w-full items-center'):
            ui.label("Origen:").classes('w-1/2 text-right pr-2')
            origen_select = ui.select({punto: f'{punto}' for punto in puntos}).classes('w-1/3')
        with ui.row().classes('w-full items-center'):
            ui.label("Destino:").classes('w-1/2 text-right pr-2')
            desitno_select = ui.select({punto: f'{punto}' for punto in puntos}).classes('w-1/3')
        with ui.row().classes('w-full justify-center'):
            ui.button("Agregar Enlace:", on_click=agregar_conexion).classes('w-1/2 text-right pr-2')
            ui.button("Eliminar Enlace:", on_click=eliminar_conexion).classes('w-1/2 text-right pr-2')
    with ui.column().classes('w-1/2 border-l-2 border-gray-300'):
        ui.label("Columna 2").classes('text-xl')
        with ui.pyplot(figsize=(5,5), close=False) as plot:
            plt.xlim(0,500)
            plt.ylim(0,500)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Grafo")
            plt.gca().set_facecolor(color="#AABBCC")

ui.run(port=8081)