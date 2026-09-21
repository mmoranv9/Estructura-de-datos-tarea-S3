class AgrupadorEdades:
    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in grupos:
                grupos[categoria] = []
            grupos[categoria].append(edad)
        return grupos

    def edad_promedio_categoria(self, categoria, *edades):
        grupos = self.agrupar_por_categoria(*edades)
        if categoria in grupos and grupos[categoria]:
            return sum(grupos[categoria]) / len(grupos[categoria])
        return None


ae = AgrupadorEdades()
resultado = ae.agrupar_por_categoria(5, 15, 30, 70)
print("Agrupación:", resultado)
print("Promedio de adultos:", ae.edad_promedio_categoria("adulto", 5, 15, 30, 70))


#Ejercicio 2

class AgrupadorAlturas:
    def clasificar_altura(self, altura):
        if altura < 150:
            return "baja"
        elif altura <= 170:
            return "media"
        elif altura <= 190:
            return "alta"
        else:
            return "muy alta"

    def agrupar_por_categoria(self, *alturas):
        grupos = {"baja": [], "media": [], "alta": [], "muy alta": []}
        for h in alturas:
            categoria = self.clasificar_altura(h)
            grupos[categoria].append(h)
        return grupos

    def altura_promedio_categoria(self, categoria, *alturas):
        grupos = self.agrupar_por_categoria(*alturas)
        if grupos[categoria]:
            return sum(grupos[categoria]) / len(grupos[categoria])
        return 0


ae = AgrupadorAlturas()
print(">>> Agrupación de alturas:", ae.agrupar_por_categoria(145, 160, 175, 200))
print(">>> Promedio de 'alta':", ae.altura_promedio_categoria("alta", 145, 160, 175, 200))

