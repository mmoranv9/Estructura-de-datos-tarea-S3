class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[str(lista)] = invertida

        return resultado



inv = InversorSecuencia()


print(inv.invertir_lista([1, 2, 3]))

print(inv.invertir_multiples([1, 2, 3], [4, 5, 6], [7, 8]))


#Ejercicio 2

class OrdenadorDeSecuencia:
    def ordenar_lista(self, lista):
        nueva = []
        for numero in lista:
            nueva.append(numero)
        nueva.sort()
        return nueva

    def ordenar_multiples(self, *listas):
        resultado = {}
        for l in listas:
            resultado[str(l)] = self.ordenar_lista(l)
        return resultado


ord = OrdenadorDeSecuencia()

print(ord.ordenar_lista([5, 2, 8, 1]))
print(ord.ordenar_multiples([10, 4, 7], [3, 9, 2]))
