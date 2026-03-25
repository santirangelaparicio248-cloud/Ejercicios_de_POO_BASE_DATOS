from vehiculo import Vehiculo

class CarroPesado(Vehiculo):
    """Clase que representa un carro pesado o camión."""
    
    def ver_info(self):
        print("  [🚚 CARRO PESADO]")
        super().ver_info()