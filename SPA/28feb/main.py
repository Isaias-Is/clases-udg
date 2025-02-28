import csv
from typing import List
from nicegui import ui, events
from computadora import *

c0 = Computadora("Asus", 16, "AMD", 1000)
c1 = Computadora(marca="Lenovo", memoria=32, procesador="Intel I7", disco=1000)
c2 = generar_computadora()
c3 = generar_computadora()
# print(c0)
# print(c0.to_dict())
# print(c1)
# print(c1.to_dict())
# print(c2)
# print(c2.to_dict())
# print(c3)
# print(c3.to_dict())

computadoras: List[Computadora] = []
computadoras.append(c0)
computadoras.append(c1)
computadoras.append(c2)
computadoras.append(c3)

def guardar_csv():
    print("Generando...")
    with open('computadoras.csv', 'w') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=['id', 'marca', 'memoria', 'procesador', 'disco'], lineterminator='\n')
        writer.writeheader()
        writer.writerows([c.to_dict() for c in computadoras])

def recuperar_csv():
    global computadoras
    with open('computadoras.csv', 'r') as archivo:
        lector = csv.DictReader(archivo)
        computadoras = []
        for fila in lector:
            c = Computadora(marca=fila['marca'], memoria=fila['memoria'], procesador=fila['procesador'], disco=fila['disco'])
            c.id = int(fila['id'])
            computadoras.append(c)

def generar_ui():
    global computadoras
    c = generar_computadora()
    computadoras.append(c)
    tabla.add_rows([])
    actualizar_tabla()

def cargar_csv(archivo: events.UploadEventArguments):
    global computadoras
    computadoras = []
    contenido = archivo.content.read().decode('utf-8').splitlines()
    lector = csv.DictReader(contenido)
    for fila in lector:
        c = Computadora(marca=fila['marca'], memoria=fila['memoria'], procesador=fila['procesador'], disco=fila['disco'])
        c.id = int(fila['id'])
        computadoras.append(c)
    tabla.rows = []
    actualizar_tabla()

def menu():
    while True:
        print("1. Generar computadora")
        print("2. Mostrar computadora")
        print("3. Guardar")
        print("4. Recuperar")
        print("0. Salir")
        op = int(input('Elige una opción: '))
        if op == 1:
            c = generar_computadora()
            print(c)
            computadoras.append(c)
        elif op == 2:
            print(computadoras)
        elif op == 3:
            guardar_csv()
        elif op == 4:
            recuperar_csv()
        elif op == 0:
            break
        else:
            print("Opción No Válida")

def actualizar_tabla():
    global computadoras
    tabla.update_rows([c.to_dict() for c in computadoras])

with ui.tabs().classes('fixed bottom-0 left-0 right-0') as tabs:
    tab1 = ui.tab("Tabla")
    tab2 = ui.tab("Exportar/Importar")
with ui.tab_panels(tabs).classes("w-full h-full"):
    with ui.tab_panel(tab1):
        tabla = ui.table(columns=[
            {"name": "id", "label": "ID", "field": "id"},
            {"name": "marca", "label": "marca", "field": "marca"},
            {"name": "memoria", "label": "memoria", "field": "memoria"},
            {"name": "procesador", "label": "procesador", "field": "procesador"},
            {"name": "disco", "label": "disco", "field": "disco"},
        ], rows=[])
        ui.button("Generar", on_click=generar_ui)
        actualizar_tabla()
    with ui.tab_panel(tab2):
        with ui.card():
            ui.button("Guardar", on_click=guardar_csv)
            ui.button("Descargar", on_click= lambda: ui.download("computadoras.csv"))
            ui.upload(on_upload=cargar_csv)

tabs.set_value('Tabla')

ui.run(port=8081)