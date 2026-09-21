class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado


cc = CodificadorCesar()
print("Codificación de 'hola' con desplazamiento 3:", cc.codificar_palabra("hola", 3))
print("Historial:", cc.historial)


#Ejercicio 2
class CodificadorSaltos:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, salto):
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            return chr((ord(letra) - base + salto) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, salto):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, salto)
        self.historial[palabra] = resultado
        return resultado

    def decodificar_palabra(self, palabra_codificada, salto):
        resultado = ""
        for letra in palabra_codificada:
            if letra.isalpha():
                base = ord('a') if letra.islower() else ord('A')
                resultado += chr((ord(letra) - base - salto) % 26 + base)
            else:
                resultado += letra
        return resultado


cs = CodificadorSaltos()
print(">>> Codificación de 'perro' con salto 4:", cs.codificar_palabra("perro", 4))
print(">>> Decodificación:", cs.decodificar_palabra(cs.historial["perro"], 4))
print(">>> Historial:", cs.historial)
