from botella import Botella

class BotellaPlastico(Botella):
    def __init__(self, nombre, material, reciclable):
        super().__init__(nombre, material)
        self.reciclable = reciclable

    def __str__(self):
        return f"{super().__str__()} - Reciclable: {self.reciclable}"