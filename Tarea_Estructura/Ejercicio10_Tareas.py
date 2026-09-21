class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [t for t in self.lista_tareas if t[1] == "alta"]

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [t for t in self.lista_tareas if t[0] != descripcion]


t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Ejercitarse", "alta")

print("Todas las tareas:", t.lista_tareas)
print("Tareas prioritarias:", t.tareas_prioritarias())

t.eliminar_completada("Leer")
print("Después de eliminar 'Leer':", t.lista_tareas)


#Ejercicio 2

class Proyectos:
    def __init__(self):
        self.lista = []

    def agregar_proyecto(self, nombre, estado):
        self.lista.append((nombre, estado))

    def proyectos_por_estado(self, estado):
        return [p for p in self.lista if p[1] == estado]

    def eliminar_proyecto(self, nombre):
        self.lista = [p for p in self.lista if p[0] != nombre]


pj = Proyectos()
pj.agregar_proyecto("App móvil", "en progreso")
pj.agregar_proyecto("Página web", "pendiente")
pj.agregar_proyecto("Sistema ERP", "completado")

print(">>> Proyectos en progreso:", pj.proyectos_por_estado("en progreso"))
pj.eliminar_proyecto("Página web")
print(">>> Lista actual:", pj.lista)

