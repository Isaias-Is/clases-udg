from nicegui import ui
import matplotlib.pyplot as plt

with ui.header().classes('bg-gray-500 bold'):
    ui.markdown('## Grafos')

with ui.row().classes('w-full h-full gap-0 border-2 border-gray-300'):
    with ui.column().classes('w-1/2'):
        ui.label("Columna 1").classes('text-xl bold')
        with ui.row().classes('w-full items-center'):
            ui.label("Origen:").classes('w-1/2 text-right pr-2')
            ui.select([1,2]).classes('w-1/3')
        with ui.row().classes('w-full items-center'):
            ui.label("Destino:").classes('w-1/2 text-right pr-2')
            ui.select([1,2]).classes('w-1/3')
        with ui.row().classes('w-full justify-center'):
            ui.button("Agregar Enlace:").classes('w-1/2 text-right pr-2')
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