from vehiculo import Vehiculo

class CarroTransporte(Vehiculo):
    """Clase que representa una van o carro de transporte."""
    
    def ver_info(self):
        print("  [🚐 CARRO DE TRANSPORTE]")
        super().ver_info()