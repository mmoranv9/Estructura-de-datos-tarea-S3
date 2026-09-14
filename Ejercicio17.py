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