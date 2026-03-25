class Botella:
    def __init__(self, nombre, material):
        self.__nombre = nombre
        self.__material = material

    def get_nombre(self):
        return self.__nombre

    def get_material(self):
        return self.__material

    def __str__(self):
        return f"Botella: {self.__nombre} - Material: {self.__material}"