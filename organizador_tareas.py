"""
ORGANIZADOR DE TAREAS
Crea un programa que permita al usuario agregar tareas a una lista y mostrarlas cuando lo desee.
El programa ofrecerá tres opciones principales: agregar tarea, ver todas las tareas y salir.
El programa termina cuando el usuario elige salir.
"""

# Lista de tareas vacía para comenzar.
lista_tareas = []

# Si la condición es verdadera, se repetirá la pregunta esperando una respuesta (opción 1-3).
while True:
    print("\n¿Qué desea hacer?\n1) Agregar tarea.\n2) Ver todas las tareas.\n3) Salir.")
    opcion = int(input("\nElige una opción (1-3): "))

# Si las opciones son números fuera de los opcionales (1-3), nos devolverá como respuesta un mensaje de error.
    if opcion < 1 or opcion > 3:
        print("\n¡Opción no válida! Reintente nuevamente ingresando la opción requerida.")

# Si la respuesta fue opción 1, se preguntará y esperará cuál es la nueva tarea que se quiere agregar al listado.
    elif opcion == 1:
        nueva_tarea = input("¿Qué tarea desea agregar?: ").capitalize()
        lista_tareas.append(nueva_tarea)
        print("\n¡Su tarea ha sido agregada exitosamente!")

# Si la respuesta fue opción 2, se mostrará en pantalla las tareas. Si no se agregó ninguna tarea previamente, se notificará que no hay ninguna.
    elif opcion == 2:
        if lista_tareas:
            print("\nSus tareas hasta la fecha son:")
            for orden, tarea in enumerate(lista_tareas):
                print(f"{orden+1}. {tarea}")
        else:
            print("\nNo se han encontrado tareas en su lista.")
            
# Si la respuesta fue opción 3, simplemente finaliza el programa.
    else:
        print("Finalizando organizador de tareas. Adiós.\n")
        break
    
# Fin del ciclo