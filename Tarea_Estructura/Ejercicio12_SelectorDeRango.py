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
