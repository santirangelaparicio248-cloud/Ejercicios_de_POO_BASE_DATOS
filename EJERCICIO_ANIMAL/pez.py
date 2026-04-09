from animal import Animal

class pez (Animal):
    "Clase que representa el animal Pez"

    def ver_info(self):
        print("[ PEZ]")
        super().ver_info()
