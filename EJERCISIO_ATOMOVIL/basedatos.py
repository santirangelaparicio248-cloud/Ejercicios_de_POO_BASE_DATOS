class BaseDatos:
    """Clase que implementa un CRUD completo para gestionar vehículos."""
    
    def __init__(self):
        self.__lista_vehiculos = []  # aquí se guardan todos los vehículos (atributo privado)

    # CREATE - agregar vehículo
    def agregar(self, vehiculo):
        if vehiculo:
            self.__lista_vehiculos.append(vehiculo)
            print(f"✓ Vehículo '{vehiculo.get_modelo()}' agregado correctamente.")
        else:
            print("Error: Vehículo inválido.")

    # READ - mostrar todos
    def mostrar_todos(self):
        if len(self.__lista_vehiculos) == 0:
            print("❌ No hay vehículos en la base de datos.")
        else:
            print("\n" + "="*45)
            print("  BASE DE DATOS DE VEHÍCULOS")
            print("="*45)
            for i, vehiculo in enumerate(self.__lista_vehiculos):
                print(f"\n[Vehículo {i}]")
                vehiculo.ver_info()
            print("\n" + "="*45)

    # READ - buscar por índice
    def buscar(self, indice):
        if 0 <= indice < len(self.__lista_vehiculos):
            return self.__lista_vehiculos[indice]
        else:
            print("❌ Índice no válido.")
            return None

    # UPDATE - modificar modelo de un vehículo
    def actualizar_modelo(self, indice, nuevo_modelo):
        vehiculo = self.buscar(indice)
        if vehiculo:
            vehiculo.set_modelo(nuevo_modelo)
            print(f"✓ Modelo actualizado a '{nuevo_modelo}'.")

    # UPDATE - modificar color de un vehículo
    def actualizar_color(self, indice, nuevo_color):
        vehiculo = self.buscar(indice)
        if vehiculo:
            vehiculo.set_color(nuevo_color)
            print(f"✓ Color actualizado a '{nuevo_color}'.")

    # DELETE - eliminar vehículo
    def eliminar(self, indice):
        if 0 <= indice < len(self.__lista_vehiculos):
            eliminado = self.__lista_vehiculos.pop(indice)
            print(f"✓ Vehículo '{eliminado.get_modelo()}' eliminado.")
        else:
            print("❌ Índice no válido.")

    # Mostrar cuántos hay
    def total(self):
        print(f"\n📊 Total de vehículos: {len(self.__lista_vehiculos)}")
