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