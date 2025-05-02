# tarea.py

class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✅ Completada" if self.completada else "❌ Pendiente"
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nEstado: {estado}"
