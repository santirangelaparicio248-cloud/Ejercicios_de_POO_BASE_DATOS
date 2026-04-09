class Animal:

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self._nombre = nombre      
        self._edad = edad
        self._habitat = habitat    
        self._dieta = dieta
        self._tamaño = tamaño
        self._color = color

    # Getters
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_habitat(self):
        return self._habitat
    def get_dieta(self):
        return self._dieta
    def get_tamaño(self):          
        return self._tamaño
    def get_color(self):
        return self._color

    # Setters
    def set_nombre(self, nuevo_dato):
        self._nombre = nuevo_dato
    def set_edad(self, nuevo_dato):
        self._edad = nuevo_dato
    def set_habitat(self, nuevo_dato):
        self._habitat = nuevo_dato
    def set_dieta(self, nuevo_dato):
        self._dieta = nuevo_dato
    def set_tamaño(self, nuevo_dato):
        self._tamaño = nuevo_dato
    def set_color(self, nuevo_dato):
        self._color = nuevo_dato   

    def ver_info(self):
        print(f"  Nombre:  {self._nombre}")
        print(f"  Edad:    {self._edad}")
        print(f"  Hábitat: {self._habitat}")   
        print(f"  Dieta:   {self._dieta}")
        print(f"  Tamaño:  {self._tamaño}")
        print(f"  Color:   {self._color}")