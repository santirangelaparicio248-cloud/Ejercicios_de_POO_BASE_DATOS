from vehiculo import Vehiculo

class CarroDeportivo(Vehiculo):
    """Clase que representa un carro deportivo."""
    
    def ver_info(self):
        print("  [🏎️  CARRO DEPORTIVO]")
        super().ver_info()