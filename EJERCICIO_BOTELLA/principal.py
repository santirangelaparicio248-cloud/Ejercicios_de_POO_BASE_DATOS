from base_datos import BaseDatos
from botella_plastico import BotellaPlastico
from botella_vidrio import BotellaVidrio

bd = BaseDatos()

while True:
    print("\n--- MENÚ ---")
    print("1. Guardar botella plástico")
    print("2. Guardar botella vidrio")
    print("3. Mostrar")
    print("4. Eliminar")
    print("5. Salir")

    op = input("Seleccione: ")

    if op == "1":
        nombre = input("Nombre: ")
        reciclable = input("¿Reciclable (si/no)?: ")
        b = BotellaPlastico(nombre, "Plástico", reciclable)
        bd.guardar(b)

    elif op == "2":
        nombre = input("Nombre: ")
        retornable = input("¿Retornable (si/no)?: ")
        b = BotellaVidrio(nombre, "Vidrio", retornable)
        bd.guardar(b)

    elif op == "3":
        bd.mostrar()

    elif op == "4":
        pos = int(input("Posición a eliminar: "))
        bd.eliminar(pos)

    elif op == "5":
        break
