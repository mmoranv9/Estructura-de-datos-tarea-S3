class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=lambda e: self.frecuencias[e])

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("c")
cf.agregar_elemento("a")

print("Frecuencias:", cf.frecuencias)
print("Elemento más frecuente:", cf.elemento_mas_frecuente())
print("Frecuencia de 'a':", cf.frecuencia_elemento("a"))
print("Frecuencia de 'b':", cf.frecuencia_elemento("b"))