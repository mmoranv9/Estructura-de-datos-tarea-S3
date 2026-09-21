class AnalizadorTexto:

    def __init__(self):
        self.conjunto = set()
        self.lista = []

    def agregar_palabra(self, palabra):
        if palabra not in self.conjunto:
            self.conjunto.add(palabra)
            self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)



analizador = AnalizadorTexto()

analizador.agregar_palabra("hola")
analizador.agregar_palabra("mundo")
analizador.agregar_palabra("hola")


analizador.agregar_multiples("python", "clase", "mundo", "programacion")


print(analizador.lista)


print("Cantidad de palabras únicas:", analizador.contar_palabras())



#Ejercicio 2 
class RegistroNombres:
    def __init__(self):
        self.nombres = []
        self.unicos = set()

    def agregar_nombre(self, nombre):
        self.nombres.append(nombre)
        self.unicos.add(nombre)

    def contar_nombres(self):
        return len(self.unicos)

    def agregar_multiples(self, *args):
        for nombre in args:
            self.agregar_nombre(nombre)


r = RegistroNombres()

r.agregar_multiples("Carlos", "Ana", "Carlos", "Pedro", "Ana", "Luis")

print(r.nombres)
print(r.unicos)
print(r.contar_nombres())