from nicegui import ui

ui.label("Calculo área de un rectángulo").style('font-size: 32px;')

def area_rectangulo():
    if base_input.value == "" and altura_input.value == "":
        ui.notify("Falta la base y la altura.", type='negative', position='top')
        return
    if base_input.value == "":
        ui.notify("Falta la base.", type='negative', position='top')
        return
    if altura_input.value == "":
        ui.notify("Falta la altura.", type='negative', position='top')
        return

    base = int(base_input.value)
    altura = int(altura_input.value)
    area = base * altura

    area_label.set_text(f"Area: {area}")

with ui.row():
    base_input = ui.input('Base').props('type=number')
    altura_input = ui.input('Altura').props('type=number')
    ui.button("Calcular: ", on_click=area_rectangulo)

with ui.row():
    area_label = ui.label("Area: ").style('font-size: 24px')

ui.run(port=8092)