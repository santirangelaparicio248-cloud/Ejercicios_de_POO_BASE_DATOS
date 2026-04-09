from animal import Animal

class caballo (Animal):
    "Clase que representa el animal caballo"

    def ver_info(self):
        print("[ CABALLO ]")
        super().ver_info()
        