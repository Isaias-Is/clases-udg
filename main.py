from nicegui import ui

def clic_boton():
    print("Hiciste clic en el botón.")
    salida.push("Hiciste clic en el botón.")
    salida.push("Hola " + nombre.value)
    mensaje.set_text("Hola " + nombre.value)

with ui.row().style() as row:
    nombre = ui.input("Nombre:")
    ui.button('HOLA', on_click=clic_boton, color='#FF8552').classes('text-black')
row.style("align-items: center; justify-content: center;")
row.style("border: solid #FF8552 2px; padding: 5px; border-radius: 15px")
row.style("width: 100%")

mensaje = ui.label(text="").style("font-size: 2rem; color: #297373")
salida = ui.log().classes('bg-[#39393A] text-white')

ui.query('body').style('background-color: #E6E6E6')

# Encabezado y pie de página.
with ui.header().classes('bg-[#E9D758];'):
    ui.label("Primeros pasos con NiceGUI").classes('text-white')
with ui.footer().classes('bg-[#39393A]'):
    ui.label('© Copyright: Todos los derechos resevados. © 2025').classes('text-white')

ui.run(port=8090)