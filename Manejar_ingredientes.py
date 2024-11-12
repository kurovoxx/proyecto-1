from Ingrediente import Ingrediente


class Despensa:
    def __init__(self):
        self.ingredientes = {}
        self.init_ingredientes()

    def init_ingredientes(self):
        self.ingredientes = {
            'papa': 0,
            'bebida': 0,
            'tomate': 0,
            'vienesa': 0,
            'pan de completo': 0,
            'pan de hamburguesa': 0,
            'lamina de queso': 0,
            'churrasco de carne': 0,
            'palta': 0
        }

    def add_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes[ingrediente.nombre] += ingrediente.cantidad

    def remove_ingrediente(self, nombre: str):
        if self.ingredientes[nombre] != 0:
            self.ingredientes[nombre] = 0

    def disponible(self):
        borrar = None
        for ingrediente, cantidad in self.ingredientes.items():
            if self.ingredientes[ingrediente] == 0:
                borrar = ingrediente
        if borrar is not None:
            del self.ingredientes[borrar]

    def mostrar_ingredientes(self):
        print()
        print('En la despensa hay:')
        for ingrediente, cant in self.ingredientes.items():
            print(f'{ingrediente}: {cant}')
        print()

    @staticmethod
    def ingredientes_posibles():
        ing = ['papa', 'bebida', 'pan de completo', 'vienesa', 'tomate', 'palta', 'pan de hamburguesa',
               'lamina de queso', 'churrasco de carne']
        return ing
