"""7. Integrador: Crear programa que permita
al usuario agregar tareas con descripción, 
fecha límite y prioridad, así como mostrar 
la lista de tareas. 
Este menú se repite hasta que el usuario elige salir."""

import os
os.system("cls") 

tareas = []
while True:
    print("\nMenú de tareas:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_limite = input("Ingrese la fecha límite (DD-MM-YYYY): ")
        prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ").lower()
        tarea = {"descripcion": descripcion, "fecha_limite": fecha_limite, "prioridad": prioridad}
        tareas.append(tarea)
        print("Tarea agregada.")
        
    elif opcion == "2":
        if not tareas:
            print("No hay tareas para mostrar.")
        else:
            print("Lista de tareas:")
            i = 1
            for tarea in tareas:
                print(f"{i}. Descripción: {tarea['descripcion']}, Fecha límite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}")
                i += 1
    
    elif opcion == "3":
        print("Saliendo del programa.")
        break