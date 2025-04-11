from dataclasses import dataclass
from random import randint, seed

@dataclass
class Punto:
    x: int
    y: int
    red: int
    blue: int
    green: int
    radio: int

    def __repr__(self):
        return f'({self.x},{self.y})'
    
    def __hash__(self):
        return hash((self.x, self.y))

seed(42)
def generar_punto() -> Punto:
    return Punto(x=randint(0, 500), y=randint(0, 500), red=randint(0, 255), blue=randint(0, 255), green=randint(0, 255), radio=randint(0, 50))