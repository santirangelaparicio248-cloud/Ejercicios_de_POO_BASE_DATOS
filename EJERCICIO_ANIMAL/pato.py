from animal import Animal

class pato (Animal):
    "Clase que representa el animal pato"

    def ver_info(self):
        print("[ PATO]")
        super().ver_info()
