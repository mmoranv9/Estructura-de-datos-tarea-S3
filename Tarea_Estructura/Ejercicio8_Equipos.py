class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        return max(self.equipos, key=lambda e: len(self.equipos[e]))


eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")

eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Luis")

print("Equipos:", eq.equipos)
print("Equipo con más integrantes:", eq.equipo_mayor_integrantes())


#Ejercicio 2

class Cursos:
    def __init__(self):
        self.nombres = []
        self.estudiantes = []

    def crear_curso(self, nombre_curso):
        if nombre_curso not in self.nombres:
            self.nombres.append(nombre_curso)
            self.estudiantes.append([])

    def agregar_estudiante(self, curso, estudiante):
        if curso in self.nombres:
            indice = self.nombres.index(curso)
            self.estudiantes[indice].append(estudiante)

    def curso_mayor_estudiantes(self):
        if not self.nombres:
            return None

        mayor = 0
        nombre_curso = ""

        for i in range(len(self.nombres)):
            if len(self.estudiantes[i]) > mayor:
                mayor = len(self.estudiantes[i])
                nombre_curso = self.nombres[i]

        return nombre_curso


c = Cursos()

c.crear_curso("Python")
c.crear_curso("Java")

c.agregar_estudiante("Python", "Carlos")
c.agregar_estudiante("Python", "Maria")
c.agregar_estudiante("Java", "Luis")
c.agregar_estudiante("Java", "Ana")
c.agregar_estudiante("Java", "Pedro")

print("Cursos:", c.nombres)
print("Estudiantes:", c.estudiantes)
print("Curso con más estudiantes:", c.curso_mayor_estudiantes())
