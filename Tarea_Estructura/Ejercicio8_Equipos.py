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