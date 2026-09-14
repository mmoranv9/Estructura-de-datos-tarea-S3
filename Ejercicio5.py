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