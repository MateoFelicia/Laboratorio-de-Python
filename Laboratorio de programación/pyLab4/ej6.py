"""6- Administrador de tareas:
Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
Muestra la lista de tareas agregadas.
Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.
"""


tareas = []

while True:
    descripcion = input("Ingrese una descripcion de la tarea: ")
    fecha = input("Para que fecha es? ")

    tarea = {
        "descripcion": descripcion,
        "fecha": fecha,
        "completada": False  # Todas empiezan como pendientes
    }

    
    tareas.append(tarea)
    
    print("Lista de tareas:")
    i = 1
    for tarea in tareas:
        estado = "✔ Completada" if tarea["completada"] else "❌ Pendiente"
        print(f"{i}. Descripción: {tarea['descripcion']}, Fecha: {tarea['fecha']} | Estado: {estado}")
        i += 1
    
    eliminar = input("Desea eliminar una tarea? (si/no) ").lower()
    if eliminar == "si":
        numero = int(input("Ingrese el numero de la tarea a eliminar: "))
        if 1 <= numero <= len(tareas):
            tareas.pop(numero - 1)
            print("Tarea eliminada.")
        else:
            print("Número de tarea inválido.")
    if eliminar == "no":
        print("No se eliminara ninguna tarea.")
            
            
            
    marcar = input("Desea marcar una tarea como completada? (si/no) ").lower()
    if marcar == "si":
        numero = int(input("Ingrese el numero de la tarea a marcar como completada: "))
        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    