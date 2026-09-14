class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [p for p, c in self.productos.items() if c < minimo]


inv = Inventario()
inv.agregar_stock("pan", 50)
print("Restar stock de pan (30):", inv.restar_stock("pan", 30))
print("Productos bajo stock (mínimo 15):", inv.productos_bajo_stock(15))
print("Inventario actual:", inv.productos)