from nicegui import ui
from matplotlib import pyplot as plt
from algoritmos import generar_punto, Punto, puntos_mas_cercanos, PuntoMasCercano
from typing import List

puntos: List[Punto] = []

def dibujar_punto():
    punto = generar_punto()
    puntos.append(punto)
    print(punto)
    with plot:
        color = [punto.red/255, punto.green/255, punto.blue/255]
        plt.scatter(punto.x, punto.y, color=color, s=punto.radio, alpha=.6)

def limpiar_puntos():
    puntos.clear()
    with plot:
        plt.cla()
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        plt.xlabel('x')
        plt.ylabel('y')

def dibujar_puntos_mas_cercanos():
    resultado: List[PuntoMasCercano]= puntos_mas_cercanos(puntos)
    with plot:
        plt.cla()
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        plt.xlabel('x')
        plt.ylabel('y')
        for punto in puntos:
            color = [punto.red/255, punto.green/255, punto.blue/255]
            plt.scatter(punto.x, punto.y, color=color, s=punto.radio, alpha=.6)
        for punto_mas_cercano in resultado:
            punto1 = punto_mas_cercano.punto1
            punto2 = punto_mas_cercano.punto2
            plt.plot([punto1.x, punto2.x], [punto1.y, punto2.y])

ui.query('body').style('background-color: #FF8552')

ui.label("Puntos Más Cercanos").style('font-size: 36px; color: #3939A;').classes('font-bold self-center')

with ui.row().classes('self-center'):
    with ui.pyplot(figsize=(5,5), close=False).style('height: 700px') as plot:
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.gca().set_facecolor('#E6E6E6')

with ui.row().classes('self-center'):
    ui.button("Dibujar", on_click=dibujar_punto)
    ui.button("Limpiar", on_click=limpiar_puntos)
    ui.button("Start", on_click=lambda: timer.activate)
    ui.button("Stop", on_click=lambda: timer.deactivate)
    ui.button("Dibujar Puntos Más Cercanos", on_click=dibujar_puntos_mas_cercanos)

timer = ui.timer(1, dibujar_punto, active=False)

ui.run(port=8081)