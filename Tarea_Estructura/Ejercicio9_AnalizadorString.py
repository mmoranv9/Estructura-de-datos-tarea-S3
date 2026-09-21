class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}
        for c in texto:
            if c.isdigit():
                conteo["digitos"] += 1
            elif c.isalpha():
                if self.solo_vocales(c):
                    conteo["vocales"] += 1
                else:
                    conteo["consonantes"] += 1
        return conteo


astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
print("Texto más largo analizado:", astr.texto_mas_largo)


#Ejercicio 2

class AnalizadorProductos:
    def __init__(self):
        self.precio_mayor = 0

    def es_barato(self, precio):
        return precio < 20

    def analizar(self, precios):
        baratos = 0
        normales = 0
        caros = 0

        for precio in precios:
            if precio < 20:
                baratos += 1
            elif precio <= 50:
                normales += 1
            else:
                caros += 1

            if precio > self.precio_mayor:
                self.precio_mayor = precio

        return {
            "baratos": baratos,
            "normales": normales,
            "caros": caros
        }


analizador = AnalizadorProductos()

print(analizador.analizar([15, 30, 60, 10, 45, 80]))
print("Precio mayor:", analizador.precio_mayor)