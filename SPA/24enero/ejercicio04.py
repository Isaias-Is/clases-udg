temp = int(input("Temperatura: "))

if temp <= 0:
    print("Esta Helado")
elif temp > 0 and temp <= 10:
    print("Esta haciendo frio.")
elif temp > 10 and temp <= 18:
    print("El clima esta fresco.")
elif temp > 18 and temp <= 25:
    print("Hace calor.")
else:
    print("Hace mucho calor.")
    