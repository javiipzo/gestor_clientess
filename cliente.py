class Cliente:
    def __init__(self,DNI,nombre,apellido):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return str(self.DNI) + " - " + str(self.nombre) + " - " + str(self.apellido)