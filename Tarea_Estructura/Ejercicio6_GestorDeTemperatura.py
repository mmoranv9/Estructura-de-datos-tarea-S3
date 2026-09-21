class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas) if self.temperaturas else None


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)

print("Temperaturas registradas:", gt.temperaturas)
print("Mínima:", gt.minima())
print("Máxima:", gt.maxima())
print("Promedio:", gt.promedio())


#Ejercicio 2 
class GestorDeVentas:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self, venta):
        self.ventas.append(venta)

    def registrar_multiples(self, *ventas):
        self.ventas.extend(ventas)

    def menor_venta(self):
        if not self.ventas:
            return 0
        menor = self.ventas[0]
        for v in self.ventas:
            if v < menor:
                menor = v
        return menor

    def mayor_venta(self):
        if not self.ventas:
            return 0
        mayor = self.ventas[0]
        for v in self.ventas:
            if v > mayor:
                mayor = v
        return mayor

    def total_ventas(self):
        if not self.ventas:
            return 0
        total = 0
        for v in self.ventas:
            total += v
        return total


gv = GestorDeVentas()

gv.registrar_multiples(120, 250, 180, 300, 150)

print("Ventas:", gv.ventas)
print("Menor venta:", gv.menor_venta())
print("Mayor venta:", gv.mayor_venta())
print("Total de ventas:", gv.total_ventas())