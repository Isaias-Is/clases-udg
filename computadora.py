from random import choice

class Computadora:
	contador_id = 1

	def __init__(self, marca, memoria, procesador, disco):
		self.id_ = Computadora.contador_id
		Computadora.contador_id += 1
		self.marca = marca
		self.memoria = memoria
		self.procesador = procesador
		self.disco = disco


	def __repr__(self):
		return f"Computadora(id={self.id_}, marca={self.marca}, memoria={self.memoria}, procesador={self.procesador}, disco={self.disco})"

	def to_dict(self):
		return {
			"id": self.id_,
			"marca": self.marca,
			"memoria": self.memoria,
			"procesador": self.procesador,
			"disco": self.disco
		}

# Funciones del paquete.
def generar_computadora() -> Computadora:
	marcas = ['Dell', 'Lenovo', 'Asus', 'Acer', 'Apple', 'HP', 'Tuxon', 'MSI', 'Gigabyte']
	memorias = [4, 8, 16, 32, 64, 128]
	procesadores = ['Intel i5', 'Intel i7', 'AMD Ryzen 3', 'AMD Ryzen 5', 'Intel i3', 'M4', 'AMD Ryzen 7', 'Snapdragon X']
	discos = [256, 512, 1024, 2028, 4056]

	marca = choice(marcas)
	memoria = choice(memorias)
	procesador = choice(procesadores)
	disco = choice(discos)

	return Computadora(marca, memoria, procesador, disco)