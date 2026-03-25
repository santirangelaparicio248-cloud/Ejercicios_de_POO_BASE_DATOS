from carrodeportivo import CarroDeportivo
from carrotransporte import CarroTransporte
from carropesado import CarroPesado
from basedatos import BaseDatos

# ========== CREAR BASE DE DATOS ==========
bd = BaseDatos()

while True:
    print("\n--- MENÚ GESTIÓN DE VEHÍCULOS ---")
    print("1. Agregar carro deportivo")
    print("2. Agregar carro transporte")
    print("3. Agregar carro pesado")
    print("4. Mostrar todos los vehículos")
    print("5. Actualizar modelo")
    print("6. Actualizar color")
    print("7. Eliminar vehículo")
    print("8. Ver total de vehículos")
    print("9. Salir")

    op = input("\nSeleccione una opción: ")

    if op == "1":
        modelo = input("Ingrese modelo: ")
        color = input("Ingrese color: ")
        motor = input("Ingrese tipo de motor: ")
        puertas = int(input("Ingrese número de puertas: "))
        pasajeros = int(input("Ingrese capacidad de pasajeros: "))
        combustible = input("Ingrese tipo de combustible: ")
        
        deportivo = CarroDeportivo(modelo, color, motor, puertas, pasajeros, combustible)
        bd.agregar(deportivo)

    elif op == "2":
        modelo = input("Ingrese modelo: ")
        color = input("Ingrese color: ")
        motor = input("Ingrese tipo de motor: ")
        puertas = int(input("Ingrese número de puertas: "))
        pasajeros = int(input("Ingrese capacidad de pasajeros: "))
        combustible = input("Ingrese tipo de combustible: ")
        
        transporte = CarroTransporte(modelo, color, motor, puertas, pasajeros, combustible)
        bd.agregar(transporte)

    elif op == "3":
        modelo = input("Ingrese modelo: ")
        color = input("Ingrese color: ")
        motor = input("Ingrese tipo de motor: ")
        puertas = int(input("Ingrese número de puertas: "))
        pasajeros = int(input("Ingrese capacidad de pasajeros: "))
        combustible = input("Ingrese tipo de combustible: ")
        
        pesado = CarroPesado(modelo, color, motor, puertas, pasajeros, combustible)
        bd.agregar(pesado)

    elif op == "4":
        bd.mostrar_todos()

    elif op == "5":
        bd.mostrar_todos()
        indice = int(input("\nIngrese índice del vehículo a actualizar: "))
        nuevo_modelo = input("Ingrese nuevo modelo: ")
        bd.actualizar_modelo(indice, nuevo_modelo)

    elif op == "6":
        bd.mostrar_todos()
        indice = int(input("\nIngrese índice del vehículo a actualizar: "))
        nuevo_color = input("Ingrese nuevo color: ")
        bd.actualizar_color(indice, nuevo_color)

    elif op == "7":
        bd.mostrar_todos()
        indice = int(input("\nIngrese índice del vehículo a eliminar: "))
        bd.eliminar(indice)

    elif op == "8":
        bd.total()

    elif op == "9":
        print("\n ¡Gracias por usar el sistema! Hasta luego.")
        break

    else:
        print("\n Opción no válida. Intente de nuevo.")