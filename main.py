from Figuras.figuras import Circulo, Punto

punto_1: Punto = Punto(2,3)
circulo_1: Circulo = Circulo(3, Punto(2,3))

print(circulo_1.calcular_area())

print(circulo_1.ubicacion_punto(punto_1))

print(circulo_1.contiene(punto_1))



