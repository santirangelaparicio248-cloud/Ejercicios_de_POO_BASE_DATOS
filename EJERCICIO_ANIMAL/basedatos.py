class BaseDatos:
    """Clase que implementa un CRUD completo para gestionar animales."""

    def __init__(self):
        self.__lista_animales = []  # atributo privado

    # ── CREATE ──────────────────────────────────────────────
    def agregar(self, animal):
        if animal:
            self.__lista_animales.append(animal)
            print(f" Animal '{animal.get_nombre()}' agregado correctamente.")
        else:
            print("Error: Animal inválido.")

    # ── READ - mostrar todos ─────────────────────────────────
    def mostrar_todos(self):
        if len(self.__lista_animales) == 0:
            print(" No hay animales en la base de datos.")
        else:
            print("\n" + "="*45)
            print("    BASE DE DATOS DE ANIMALES")
            print("="*45)
            for i, animal in enumerate(self.__lista_animales):
                print(f"\n[Animal {i}]")
                animal.ver_info()
            print("\n" + "="*45)

    # ── READ - buscar por índice ─────────────────────────────
    def buscar(self, indice):
        if 0 <= indice < len(self.__lista_animales):
            return self.__lista_animales[indice]
        else:
            print(" Índice no válido.")
            return None

    # ── UPDATE ───────────────────────────────────────────────
    def actualizar_nombre(self, indice, nuevo_nombre):
        animal = self.buscar(indice)
        if animal:
            animal.set_nombre(nuevo_nombre)
            print(f" Nombre actualizado a '{nuevo_nombre}'.")
    
    def actualizar_edad(self, indice, nueva_edad):
        animal = self.buscar(indice)
        if animal:
            animal.set_edad(nueva_edad)
            print(f" Edad actualizada a '{nueva_edad}'.")
    
    def actualizar_habitat(self, indice, nuevo_habitat):
        animal = self.buscar(indice)
        if animal:
            animal.set_habitat(nuevo_habitat)
            print(f" Hábitat actualizado a '{nuevo_habitat}'.")

    def actualizar_dieta(self, indice, nueva_dieta):
        animal = self.buscar(indice)
        if animal:
            animal.set_dieta(nueva_dieta)
            print(f" Dieta actualizada a '{nueva_dieta}'.")

    def actualizar_color(self, indice, nuevo_color):
        animal = self.buscar(indice)
        if animal:
            animal.set_color(nuevo_color)
            print(f" Color actualizado a '{nuevo_color}'.")

    def actualizar_tamaño(self, indice, nuevo_tamaño):
        animal = self.buscar(indice)
        if animal:
            animal.set_tamaño(nuevo_tamaño)
            print(f" Tamaño actualizado a '{nuevo_tamaño}'.")

    # ── DELETE ───────────────────────────────────────────────
    def eliminar(self, indice):
        if 0 <= indice < len(self.__lista_animales):
            eliminado = self.__lista_animales.pop(indice)
            print(f" Animal '{eliminado.get_nombre()}' eliminado.")
        else:
            print(" Índice no válido.")

    # ── EXTRA ────────────────────────────────────────────────
    def total(self):
        print(f"\n Total de animales: {len(self.__lista_animales)}")