class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisores[:-1])  
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
        return resultado


df = DivisorFinder()

print("Divisores de 12:", df.encontrar_divisores(12))
print("¿28 es perfecto?:", df.es_perfecto(28))
print("Divisores de varios números:", df.encontrar_multiples_divisores(6, 12, 15))


#Ejercicio 2

class MultiplicadorFinder:
    def encontrar_multiplicadores(self, numero, limite):
        resultado = []
        for i in range(numero, limite+1, numero):
            resultado.append(i)
        return tuple(resultado)

    def es_multiplo(self, numero, base):
        return numero % base == 0

    def multiplicadores_de_lista(self, *pares):
        salida = {}
        for numero, limite in pares:
            salida[numero] = self.encontrar_multiplicadores(numero, limite)
        return salida


mf = MultiplicadorFinder()
print(">>> Múltiplos de 3 hasta 20:", mf.encontrar_multiplicadores(3, 20))
print(">>> ¿12 es múltiplo de 3?:", mf.es_multiplo(12, 3))
print(">>> Múltiplos de varios números:", mf.multiplicadores_de_lista((2, 10), (5, 30)))

