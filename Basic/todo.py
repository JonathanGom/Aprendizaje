tareas = []



def menu ():

    print("Seleccione una opción:")
    print("1. Agregar tarea")
    print("2. Ver lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción: ")
    return opcion

activo = True
while activo:
    opcion = menu()
    if opcion == "1":
        tarea = input("Nombre de la tarea: ")
        tareas.append({"tarea": tarea, "completada": False})
        print(f"Tarea '{tarea}' agregada!")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        else:
            print("\nTAREAS:")
            for i, t in enumerate(tareas, 1):
                estado = "completada" if t["completada"] else "incompleta "
                print(f"{i}. [{estado}] {t['tarea']}")

    elif opcion == "3":
        if not tareas:
            print("No hay tareas para marcar.")
        else:
            num = int(input("Número de tarea a completar: ")) - 1
            if 0 <= num < len(tareas):
                tareas[num]["completada"] = True
                print(f"Tarea '{tareas[num]['tarea']}' completada!")
            else:
                print("Número inválido")

    elif opcion == "4":
        if not tareas:
            print("No hay tareas para eliminar.")
        else:
            num = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                eliminada = tareas.pop(num)
                print(f"Tarea '{eliminada['tarea']}' eliminada!")
            else:
                print("Número inválido")

    elif opcion == "5":
        print("¡Hasta luego!")
        activo = False

    else:
        print("Opción no válida")