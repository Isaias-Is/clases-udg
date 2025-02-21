from nicegui import ui
from administrador import Administrador, Materia
from materia import generarMateriaAleatoria

admin = Administrador()
admin.recuperar("materias")

def agregar():
    mat = Materia()
    mat.nombre = nombre.value
    mat.clave = clave.value
    mat.carrera = carrera.value
    mat.creditos = creditos.value
    admin.agregarMateria(mat)
    admin.mostrarTablaMaterias()
    actualizar_tabla()

def generar():
    mat = generarMateriaAleatoria()
    admin.agregarMateria(mat)
    admin.mostrarTablaMaterias()
    actualizar_tabla()

def actualizar_tabla():
    tabla.update_rows([mat.to_dict() for mat in admin.materias])

def limpiar_tabla():
    tabla.update_rows([])

with ui.tabs().classes('bg-gray-100 fixed bottom-0 left-0 right-0') as tabs:
    tab1 = ui.tab("Formulario", icon='books').classes('items-end')
    tab2 = ui.tab("Mostrar", icon='info')

with ui.tab_panels(tabs).classes('fixed-center'):
    with ui.tab_panel(tab1).classes():
        with ui.card():
            ui.label("Ingrese los datos de la materia").classes('text-x1 font-bold')
            nombre = ui.input("Nombre")
            clave = ui.input("Clave")
            carrera = ui.input("Carrera")
            creditos = ui.input("Créditos", value=8)
            with ui.row():
                ui.button("Agregar", on_click=agregar)
                ui.button("Generar", on_click=generar)
    with ui.tab_panel(tab2).classes():
        with ui.card():
            ui.label("Lista de Materias").classes('text-x1 font-bold')
            tabla = ui.table(columns=[{'name': 'nombre', 'label': 'Nombre', 'field': 'nombre'},
                              {'name': 'clave', 'label': 'Clave', 'field': 'clave'},
                              {'name': 'carrera', 'label': 'Carrera', 'field': 'carrera'},
                              {'name': 'creditos', 'label': 'Creditos', 'field': 'creditos'},
                              ], rows=[mat.to_dict() for mat in admin.materias])
            with ui.row():
                ui.button("Mostrar", on_click=actualizar_tabla)
                ui.button("Limpiar", on_click=limpiar_tabla)
                ui.button("Vaciar Admin", on_click=lambda: limpiar_tabla() or admin.materias.clear())

tabs.set_value('Formulario')

ui.run(port=8081)