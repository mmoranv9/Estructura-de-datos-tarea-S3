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