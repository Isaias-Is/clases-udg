from personaje import Personaje
from administrador import Administrador

admin = Administrador()

while True:
    print("1) Agregar Personaje")
    print("2) Mostrar Personajes")
    print("0) Salir")
    print("---------------------\nOpción: ", end="")
    op = input()
    print("---------------------")
    if op == "1":
        p = Personaje()
        # Recabar la información del usuario.
        p.tipo = input("Tipo: ")
        p.fuerza = float(input("Fuerza: "))
        p.salud = int(input("Salud: ")) 
        admin.agregar(p) # Agregar el nuevo personaje al administrador de personajes.
    elif op == "2":
        admin.mostrar()
    elif op == "0":
        break
    else:
        print("Opción no valida.")

#p01 = Personaje()
#p01.tipo = "Guerrero"
#p01.fuerza = 80.5
#p01.salud = 50
#
#admin.agregar(p01)
#admin.mostrar()