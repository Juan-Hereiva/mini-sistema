# gestor.py

from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        nueva = Tarea(nombre, descripcion)
        self.tareas.append(nueva)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.\n")
        else:
            for idx, tarea in enumerate(self.tareas):
                print(f"\n[{idx}]")
                print(tarea)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
