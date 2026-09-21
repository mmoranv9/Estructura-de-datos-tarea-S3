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


#Ejercicio 2 

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, titulo, cantidad):
        if titulo in self.libros:
            self.libros[titulo] += cantidad
        else:
            self.libros[titulo] = cantidad

    def prestar_libro(self, titulo, cantidad):
        if titulo in self.libros and self.libros[titulo] >= cantidad:
            self.libros[titulo] -= cantidad
            return True
        return False

    def libros_bajo_stock(self, minimo):
        return [t for t, c in self.libros.items() if c < minimo]


b = Biblioteca()
b.agregar_libro("Cien años de soledad", 3)
b.agregar_libro("El principito", 5)

print(">>> Prestar 'Cien años de soledad' (1):", b.prestar_libro("Cien años de soledad", 1))
print(">>> Libros bajo stock (mínimo 2):", b.libros_bajo_stock(2))
print(">>> Inventario actual:", b.libros)

