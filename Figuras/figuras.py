import math


class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Circulo:

    def __init__(self, radio: int, centro: Punto):
        self.radio: int = radio
        self.centro: Punto = centro


    def calcular_area(self) -> float:

        return math.pi * self.radio ** 2

    def ubicacion_punto(self, punto : Punto):

        punto = punto
        if self.centro.x > punto.x and self.centro.y > punto.y:
            return print("El punto se encuentra dentro del circulo")

        else:
            return print("El punto está por fuera del circulo")

    def contiene(self, punto:Punto) -> bool:
        return (punto.x-self.centro.x)**2+(punto.y-self.centro.y)**2 <= self.radio**2

#Realizar función que diga si dos circulos se interceptan