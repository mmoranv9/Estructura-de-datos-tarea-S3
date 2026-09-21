class AnalizadorNumeros:
    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        pares = []
        impares = []
        for n in numeros:
            if self.es_par(n):
                pares.append(n)
            else:
                impares.append(n)
        return {'pares': pares, 'impares': impares}

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)
        return (len(resultado['pares']), len(resultado['impares']))


an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares(1, 2, 3, 4, 5))


#Ejercicio 2

class AnalizadorDeVelocidades:
    def __init__(self):
        self.rapidas = []
        self.lentas = []

    def es_rapida(self, velocidad):
        return velocidad >= 80

    def separar(self, *velocidades):
        self.rapidas = []
        self.lentas = []

        for v in velocidades:
            if self.es_rapida(v):
                self.rapidas.append(v)
            else:
                self.lentas.append(v)

        return {"rapidas": self.rapidas, "lentas": self.lentas}

    def cantidad_rapidas_lentas(self):
        return (len(self.rapidas), len(self.lentas))


a = AnalizadorDeVelocidades()

print(a.separar(60, 90, 75, 100, 80, 50))
print(a.cantidad_rapidas_lentas())
