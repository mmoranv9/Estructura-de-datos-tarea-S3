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