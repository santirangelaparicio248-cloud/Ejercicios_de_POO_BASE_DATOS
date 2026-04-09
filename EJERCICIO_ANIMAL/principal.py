from basedatos import BaseDatos
from caballo import caballo
from cocodrilo import cocodrilo
from escarabajo import escarabajo
from pato import pato
from pez import pez

bd = BaseDatos()

while True:
    print("\n--- Menú de Gaestión de animales ---")
    print("1. Agregar animal")
    print("2. Mostrar datos BS")
    print("3. Buscar uno")
    print("4. Actualizar Algo")
    print("5. Eliminar")
    print("6. Salir")
    
    op = input("\nSeleccione una opción: ")

    if op == "1":

        while True:
            print("\n¿Que animal quieres agregar?")
            print("1.  Caballo")
            print("2.  Cocodrilo")
            print("3.  Escarabajo")
            print("4.  Pato")
            print("5.  Pez")
            print("6.  Volver al menú principal")
            op2 = input("\nSeleccione una opción: ")

            if op2 == "1":

                nombre = input("Ingrese el nombre del caballo: ")
                edad = int(input("Ingrese la edad del caballo: "))
                habitat = input("Ingrese el hábitat del caballo: ")
                dieta = input("Ingrese la dieta del caballo: ")
                tamaño = input("Ingrese el tamaño del caballo: ")
                color = input("Ingrese el color del caballo: ")
                nuevo_caballo = caballo(nombre, edad, habitat, dieta, tamaño, color)
                bd.agregar(nuevo_caballo)
                break

            elif op2 == "2":

                nombre = input("Ingrese el nombre del cocodrilo: ")
                edad = int(input("Ingrese la edad del cocodrilo: "))
                habitat = input("Ingrese el hábitat del cocodrilo: ")
                dieta = input("Ingrese la dieta del cocodrilo: ")
                tamaño = input("Ingrese el tamaño del cocodrilo: ")
                color = input("Ingrese el color del cocodrilo: ")
                nuevo_cocodrilo = cocodrilo(nombre, edad, habitat, dieta, tamaño, color)
                bd.agregar(nuevo_cocodrilo)
                break

            elif op2 == "3":

                nombre = input("Ingrese el nombre del escarabajo: ")
                edad = int(input("Ingrese la edad del escarabajo: "))
                habitat = input("Ingrese el hábitat del escarabajo: ")
                dieta = input("Ingrese la dieta del escarabajo: ")
                tamaño = input("Ingrese el tamaño del escarabajo: ")
                color = input("Ingrese el color del escarabajo: ")
                nuevo_escarabajo = escarabajo(nombre, edad, habitat, dieta, tamaño, color)
                bd.agregar(nuevo_escarabajo)
                break

            elif op2 == "4":

                nombre = input("Ingrese el nombre del pato: ")
                edad = int(input("Ingrese la edad del pato: "))
                habitat = input("Ingrese el hábitat del pato: ")
                dieta = input("Ingrese la dieta del pato: ")
                tamaño = input("Ingrese el tamaño del pato: ")
                color = input("Ingrese el color del pato: ")
                nuevo_pato = pato(nombre, edad, habitat, dieta, tamaño, color)
                bd.agregar(nuevo_pato)
                break

            elif op2 == "5":

                nombre = input("Ingrese el nombre del pez: ")
                edad = int(input("Ingrese la edad del pez: "))
                habitat = input("Ingrese el hábitat del pez: ")
                dieta = input("Ingrese la dieta del pez: ")
                tamaño = input("Ingrese el tamaño del pez: ")
                color = input("Ingrese el color del pez: ")
                nuevo_pez = pez(nombre, edad, habitat, dieta, tamaño, color)
                bd.agregar(nuevo_pez)
                break

            elif op2 == "6":

                print("\n Volver al menú principal")
                break

            else:

                print("\n Opción no válida. Intente nuevamente.")

    elif op == "2":

        bd.mostrar_todos() 

    elif op == "3":

        bd.mostrar_todos()
        indice = int(input("\nIngrese el índice del animal a buscar: "))
        animal = bd.buscar(indice)

        if animal:
            print("\nInformación del animal encontrado:")
            animal.ver_info()

    elif op == "4":
        bd.mostrar_todos()
        indice = int(input("Índice a actualizar: "))


        while True:
            print("¿Qué quieres actualizar?")
            print("1. Nombre")
            print("2. Edad")
            print("3. Color")
            print("4. Hábitat")
            print("5. Dieta")
            print("6. Tamaño")
            print("7. Volver al menú principal")
            op3 = input("\nSeleccione una opción: ")
            if op3 == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                bd.actualizar_nombre(indice, nuevo_nombre)
                break
            elif op3 == "2":
                nueva_edad = int(input("Ingrese la nueva edad: "))
                bd.actualizar_edad(indice, nueva_edad)
                break
            elif op3 == "3":
                nuevo_color = input("Ingrese el nuevo color: ")
                bd.actualizar_color(indice, nuevo_color)
                break
            elif op3 == "4":
                nuevo_habitat = input("Ingrese el nuevo hábitat: ")
                bd.actualizar_habitat(indice, nuevo_habitat)
                break
            elif op3 == "5":
                nueva_dieta = input("Ingrese la nueva dieta: ")
                bd.actualizar_dieta(indice, nueva_dieta)
                break
            elif op3 == "6":
                nuevo_tamaño = input("Ingrese el nuevo tamaño: ")
                bd.actualizar_tamaño(indice, nuevo_tamaño)
                break
            elif op3 == "7":
                print("\n Volver al menú principal")
                break
            else:
                print("\n Opción no válida. Intente nuevamente.")





    elif op == "5":
        bd.mostrar_todos()
        indice = int(input("\nIngrese el índice del animal a eliminar: "))
        bd.eliminar(indice)
    elif op == "6":
        print("\n ¡Gracias por usar el sistema! Hasta luego.")
        break
    else:
        print("\n Opción no válida. Intente de nuevo.")


