class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <= 100:
            return True
        else:
            return False
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-60,80,40,200))
print(cal.promedio())



#Ejercicio 2 
class Edad:
    def __init__(self):
        self.edades = []

    def validar_edad(self, edad):
        return 1 <= edad <= 100

    def cargar_edades(self, *args):
        for e in args:
            if self.validar_edad(e):
                self.edades.append(e)
        return self.edades

    def promedio(self):
        if len(self.edades) == 0:
            return 0
        return sum(self.edades) / len(self.edades)


e = Edad()

print(e.cargar_edades(18, 20, 25, 150, -5, 30))
print(e.promedio())

