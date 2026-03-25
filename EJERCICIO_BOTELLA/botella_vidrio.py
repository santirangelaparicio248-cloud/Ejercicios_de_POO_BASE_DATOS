from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, nombre, material, retornable):
        super().__init__(nombre, material)
        self.retornable = retornable

    def __str__(self):
        return f"{super().__str__()} - Retornable: {self.retornable}"