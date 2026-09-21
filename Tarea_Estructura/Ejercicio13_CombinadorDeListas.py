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


#Ejercicio 2
class UnificadorListas:
    def sumar_pares(self, lista1, lista2):
        resultado = []
        for i in range(min(len(lista1), len(lista2))):
            resultado.append(lista1[i] + lista2[i])
        return resultado

    def sumar_multiples(self, *listas):
        longitud = min(len(l) for l in listas)
        resultado = []
        for i in range(longitud):
            suma = 0
            for l in listas:
                suma += l[i]
            resultado.append(suma)
        return resultado

    def maximo_por_posicion(self, *listas):
        longitud = min(len(l) for l in listas)
        resultado = []
        for i in range(longitud):
            maximo = max(l[i] for l in listas)
            resultado.append(maximo)
        return resultado


ul = UnificadorListas()
print(">>> Suma de pares:", ul.sumar_pares([1,2,3], [4,5,6]))
print(">>> Suma de múltiples listas:", ul.sumar_multiples([1,2], [3,4], [5,6]))
print(">>> Máximos por posición:", ul.maximo_por_posicion([1,9], [3,4], [5,2]))

