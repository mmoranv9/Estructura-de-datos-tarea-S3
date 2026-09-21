class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        conjunto = set()
        for inicio, fin in rangos:
            conjunto.update(range(inicio, fin + 1))
        return sorted(list(conjunto))


sr = SelectorRango()

print("Rango (1,3):", sr.crear_rango(1, 3))
print("Elementos en múltiples rangos:", sr.elementos_en_multiples_rangos((1, 3), (2, 4)))
print("Elementos en múltiples rangos:", sr.elementos_en_multiples_rangos((5, 7), (6, 9)))



#Ejercicio 2 

class SelectorMultiplos:
    def crear_rango_multiplos(self, inicio, fin, base):
        resultado = []
        for i in range(inicio, fin+1):
            if i % base == 0:
                resultado.append(i)
        return tuple(resultado)

    def multiplos_en_multiples_rangos(self, base, *rangos):
        conjunto = set()
        for inicio, fin in rangos:
            for i in range(inicio, fin+1):
                if i % base == 0:
                    conjunto.add(i)
        return sorted(list(conjunto))

    def contar_multiplos(self, base, inicio, fin):
        contador = 0
        for i in range(inicio, fin+1):
            if i % base == 0:
                contador += 1
        return contador


sm = SelectorMultiplos()
print(">>> Múltiplos de 3 en rango (1,15):", sm.crear_rango_multiplos(1, 15, 3))
print(">>> Múltiplos de 4 en múltiples rangos:", sm.multiplos_en_multiples_rangos(4, (1,10), (5,20)))
print(">>> Cantidad de múltiplos de 5 en (1,30):", sm.contar_multiplos(5, 1, 30))


