class Vehiculo:
    """Clase base para representar un vehículo con atributos privados."""
    
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.__modelo = modelo
        self.__color = color
        self.__motor = motor
        self.__numero_puertas = numero_puertas
        self.__capacidad_pasajeros = capacidad_pasajeros
        self.__tipo_combustible = tipo_combustible

    # Getters
    def get_modelo(self):
        return self.__modelo
    def get_color(self):
        return self.__color
    def get_motor(self):
        return self.__motor
    def get_numero_puertas(self):
        return self.__numero_puertas
    def get_capacidad_pasajeros(self):
        return self.__capacidad_pasajeros
    def get_tipo_combustible(self):
        return self.__tipo_combustible

    # Setters
    def set_modelo(self, nuevo_dato):
        self.__modelo = nuevo_dato
    def set_color(self, nuevo_dato):
        self.__color = nuevo_dato
    def set_motor(self, nuevo_dato):
        self.__motor = nuevo_dato
    def set_numero_puertas(self, nuevo_dato):
        self.__numero_puertas = nuevo_dato
    def set_capacidad_pasajeros(self, nuevo_dato):
        self.__capacidad_pasajeros = nuevo_dato
    def set_tipo_combustible(self, nuevo_dato):
        self.__tipo_combustible = nuevo_dato

    def ver_info(self):
        print(f"  Modelo: {self.__modelo}")
        print(f"  Color: {self.__color}")
        print(f"  Motor: {self.__motor}")
        print(f"  Número de puertas: {self.__numero_puertas}")
        print(f"  Capacidad pasajeros: {self.__capacidad_pasajeros}")
        print(f"  Tipo de combustible: {self.__tipo_combustible}")