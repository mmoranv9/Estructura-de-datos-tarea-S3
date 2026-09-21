import math

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        d = math.sqrt(dx**2 + dy**2)
        self.distancias.append(d)
        return d

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        return min(puntos, key=lambda p: self.distancia_euclidiana(referencia, p))


cd = CalculadorDistancia()

print("Distancia entre (0,0) y (3,4):", cd.distancia_euclidiana((0,0), (3,4)))
print("Punto más cercano a (0,0):", cd.punto_mas_cercano((0,0), (3,4), (1,1), (5,5)))
print("Historial de distancias:", cd.distancias)



#Ejercicio 2
class CalculadorManhattan:
    def __init__(self):
        self.historial = []

    def distancia_manhattan(self, p1, p2):
        dx = abs(p1[0] - p2[0])
        dy = abs(p1[1] - p2[1])
        d = dx + dy
        self.historial.append(d)
        return d

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        cercano = puntos[0]
        menor = self.distancia_manhattan(referencia, cercano)
        for p in puntos[1:]:
            dist = self.distancia_manhattan(referencia, p)
            if dist < menor:
                menor = dist
                cercano = p
        return cercano


cm = CalculadorManhattan()
print(">>> Distancia Manhattan entre (0,0) y (3,4):", cm.distancia_manhattan((0,0), (3,4)))
print(">>> Punto más cercano a (2,2):", cm.punto_mas_cercano((2,2), (1,1), (4,4), (2,5)))
print(">>> Historial de distancias:", cm.historial)
