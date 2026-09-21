class AnalizadorPatrones:
    def __init__(self):
        self.textos_analizados = []

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = [p for p in palabras if p.startswith(patron)]
        self.textos_analizados.append(texto)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for p in palabras:
            longitud = len(p)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(p)
        self.textos_analizados.append(texto)
        return grupos

    def palabras_unicas(self):
        conjunto = set()
        for texto in self.textos_analizados:
            conjunto.update(texto.split())
        return conjunto


ap = AnalizadorPatrones()

print("Palabras que empiezan con 'a':", ap.encontrar_palabras("el gato está aquí ahora", "a"))
print("Agrupación por longitud:", ap.agrupar_por_longitud("el gato está aquí"))
print("Palabras únicas analizadas:", ap.palabras_unicas())