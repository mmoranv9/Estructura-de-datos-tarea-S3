class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        if not self.personas:
            return None
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 22)

print("Mayores de 18:", gp.personas_mayores(18))
print("Edad promedio:", gp.edad_promedio())


#Ejercicio 2

class GestorDePeliculas:
    def __init__(self):
        self.titulos = []
        self.duraciones = []

    def agregar_pelicula(self, titulo, duracion):
        self.titulos.append(titulo)
        self.duraciones.append(duracion)

    def peliculas_largas(self, duracion_minima):
        resultado = []
        for i in range(len(self.titulos)):
            if self.duraciones[i] >= duracion_minima:
                resultado.append(self.titulos[i])
        return resultado

    def duracion_promedio(self):
        if not self.duraciones:
            return 0
        suma = 0
        for d in self.duraciones:
            suma += d
        return suma / len(self.duraciones)


gp = GestorDePeliculas()

gp.agregar_pelicula("Avatar", 162)
gp.agregar_pelicula("Toy Story", 81)
gp.agregar_pelicula("Titanic", 194)

print("Películas de más de 100 minutos:", gp.peliculas_largas(100))
print("Duración promedio:", gp.duracion_promedio())
