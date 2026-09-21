class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)

        return resultado



c = CarroCompras()


c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 5.00)
c.agregar_articulo("cafe", 8.00)


print("Total:", c.total_carrito())


print("Artículos en rango:", c.articulos_por_rango(2, 8))


#Ejercicio 2

class Restaurante:
    def __init__(self):
        self.platos = {}

    def agregar_plato(self, nombre, precio):
        self.platos[nombre] = precio

    def total_pedido(self):
        return sum(self.platos.values())

    def platos_por_rango(self, precio_min, precio_max):
        lista = []
        for nombre, precio in self.platos.items():
            if precio_min <= precio <= precio_max:
                lista.append(nombre)
        return lista


r = Restaurante()

r.agregar_plato("Hamburguesa", 5.00)
r.agregar_plato("Pizza", 8.00)
r.agregar_plato("Ensalada", 4.00)

print(r.total_pedido())
print(r.platos_por_rango(4, 6))