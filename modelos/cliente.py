# Clase que representa a un cliente

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} - Cédula: {self.cedula}"