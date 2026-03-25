class BaseDatos:
    def __init__(self):
        self.botellas = []

    # CREATE
    def guardar(self, botella):
        self.botellas.append(botella)

    # READ
    def mostrar(self):
        if not self.botellas:
            print("No hay datos")
        else:
            for i, b in enumerate(self.botellas):
                print(i, b)

    # DELETE
    def eliminar(self, posicion):
        if 0 <= posicion < len(self.botellas):
            self.botellas.pop(posicion)
        else:
            print("Posición inválida")

    # INSERT
    def insertar(self, posicion, botella):
        self.botellas.insert(posicion, botella)

    # SEARCH
    def buscar(self, nombre):
        for b in self.botellas:
            if b.get_nombre() == nombre:
                return b
        return None