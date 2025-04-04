from dataclasses import dataclass

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