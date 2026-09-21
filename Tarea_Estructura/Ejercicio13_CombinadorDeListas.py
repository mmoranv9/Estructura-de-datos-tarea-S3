class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        for i in range(max(len(lista1), len(lista2))):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []
        max_len = max(len(l) for l in listas)
        for i in range(max_len):
            for l in listas:
                if i < len(l):
                    resultado.append(l[i])
        return resultado


cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
print(cl.intercalar_multiples([1, 2, 3], [10, 20], [100, 200, 300]))