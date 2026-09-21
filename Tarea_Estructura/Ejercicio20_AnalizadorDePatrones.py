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



#Ejercicio 2
class AnalizadorVocales:
    def contar_vocales(self, texto):
        conteo = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for letra in texto.lower():
            if letra in conteo:
                conteo[letra] += 1
        return conteo

    def palabras_con_vocal(self, vocal, texto):
        palabras = texto.split()
        resultado = []
        for p in palabras:
            if vocal in p:
                resultado.append(p)
        return resultado

    def vocales_unicas(self, texto):
        conjunto = set()
        for letra in texto.lower():
            if letra in "aeiou":
                conjunto.add(letra)
        return conjunto


av = AnalizadorVocales()
print(">>> Conteo de vocales:", av.contar_vocales("hola mundo"))
print(">>> Palabras con 'a':", av.palabras_con_vocal("a", "el gato está aquí"))
print(">>> Vocales únicas en 'perro':", av.vocales_unicas("perro"))

