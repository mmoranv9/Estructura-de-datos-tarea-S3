class NumeroPrimo:
    def __init__(self):
        self.historial = []
    
    def es_primo(self, numero):
        self.historial.append(numero)
        if numero < 2:
            return False
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                return False
        return True
    
    def primos_en_rango(self, *args):
        primos = []
        for numero in args:
            if self.es_primo(numero):
                primos.append(numero)
        return primos
    
    def cantidad_verificados(self):
        return len(self.historial)
    
    def limpiar_historial(self):
        self.historial = []


np = NumeroPrimo()

resultado = np.es_primo(7)
print(f"¿7 es primo? {resultado}")

primos = np.primos_en_rango(10, 11, 12, 13, 14, 15)
print(f"Primos en el rango [10-15]: {primos}")

print(f"Historial: {np.historial}")
print(f"Total verificados: {np.cantidad_verificados()}")




#Ejercicio 2
class NumeroPar:
    def __init__(self):
        self.historial = []

    def es_par(self, numero):
        self.historial.append(numero)
        return numero % 2 == 0

    def pares_en_lista(self, *args):
        pares = []
        for numero in args:
            if self.es_par(numero):
                pares.append(numero)
        return pares

    def cantidad_verificados(self):
        return len(self.historial)

    def limpiar_historial(self):
        self.historial = []


np = NumeroPar()

resultado = np.es_par(8)
print(f"¿8 es par? {resultado}")

pares = np.pares_en_lista(3, 4, 7, 10, 12, 15)
print(f"Números pares: {pares}")

print(f"Historial: {np.historial}")
print(f"Total verificados: {np.cantidad_verificados()}")
