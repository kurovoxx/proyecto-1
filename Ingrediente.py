class Ingrediente:
    def __init__(self, nombre: str, cantidad: int):
        self.nombre = nombre.lower()
        self.cantidad = cantidad
