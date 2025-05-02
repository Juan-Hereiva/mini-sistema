# main.py

from gestor import GestorTareas

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción: ")
            gestor.agregar_tarea(nombre, descripcion)
            print("✅ Tarea agregada.")

        elif opcion == "2":
            gestor.mostrar_tareas()

        elif opcion == "3":
            indice = int(input("Índice de la tarea a marcar como completada: "))
            gestor.marcar_completada(indice)
            print("✅ Tarea marcada como completada.")

        elif opcion == "4":
            indice = int(input("Índice de la tarea a eliminar: "))
            gestor.eliminar_tarea(indice)
            print("🗑️ Tarea eliminada.")

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("❗ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
