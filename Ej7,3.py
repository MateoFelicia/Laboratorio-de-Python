"""En esta actividad, ampliarás el programa de gestión de tareas
proporcionado para incluir la capacidad de marcar una tarea como
completada. Esto te permitirá practicar la modificación de
funciones existentes y la adición de nuevas funcionalidades 
a un programa en Python.
"""


def agregar_tarea(tareas, tarea, fecha_limite, prioridad):
    nueva_tarea = {"Tarea": tarea, "Fecha limite": fecha_limite, "Prioridad": prioridad, "Completada": False}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")


def mostrar_tareas(tareas, completadas=None):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):

            estado = tarea["Completada"]  # ← clave

            if completadas is None:
                mostrar = True
            elif completadas is True:
                mostrar = estado is True
            else:
                mostrar = estado is False
                
            if mostrar:
                print(f"\nTarea {i}:")
                for clave, valor in tarea.items():
                    print(f"{clave}: {valor}")

if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha limite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            if not lista_tareas:
                print("No hay tareas pendientes.")
                continue # Si no hay tareas, no tiene sentido preguntar si se quieren mostrar solo las completadas o no
                
            print("\n1. Mostrar todas")
            print("2. Mostrar completadas")
            print("3. Mostrar pendientes")

            filtro = input("Seleccione una opción: ")
            if filtro == "1":
                mostrar_tareas(lista_tareas)
            elif filtro == "2":
                mostrar_tareas(lista_tareas, True)
            elif filtro == "3":
                mostrar_tareas(lista_tareas, False)
            else:
                print("Opción inválida.")
            
            
        elif opcion == "3":
            numero = int(input("Ingrese el numero de la tarea a marcar como completada: "))
            if 1 <= numero <= len(lista_tareas):
                lista_tareas[numero - 1]["Completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
            

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intente nuevamente.")