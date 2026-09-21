class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados

    def mejor_estudiante(self):
        if not self.notas:
            return None
        nombre = max(self.notas, key=lambda e: self.notas[e])
        return (nombre, self.notas[nombre])


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 82)

print("Estudiantes aprobados (nota mínima 75):", rn.estudiantes_aprobados(75))
print("Mejor estudiante:", rn.mejor_estudiante())


#Ejercicio 2 

class NumeroAnalizador:
    def calcular_factorial(self, numero):
        resultado = 1
        for i in range(1, numero+1):
            resultado *= i
        return resultado

    def es_cuadrado_perfecto(self, numero):
        raiz = int(numero**0.5)
        return raiz * raiz == numero

    def analizar_lista(self, *numeros):
        salida = {}
        for n in numeros:
            salida[n] = {
                "factorial": self.calcular_factorial(n),
                "cuadrado_perfecto": self.es_cuadrado_perfecto(n)
            }
        return salida


na = NumeroAnalizador()
print(">>> Factorial de 5:", na.calcular_factorial(5))
print(">>> ¿16 es cuadrado perfecto?:", na.es_cuadrado_perfecto(16))
print(">>> Análisis de lista:", na.analizar_lista(4, 5, 9))

