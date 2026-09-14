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