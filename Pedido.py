class Pedido:
    def __init__(self):
        self.lista_pedido = []

    def add_elemento(self, elemento):
        self.lista_pedido.append(elemento)

    def mostrar_pedido(self):
        pedido = self.calcular_cant()
        print()
        print('El pedido consiste en:')
        for i in range(len(pedido)):
            print(f'-{pedido[i][0]}: {pedido[i][1]}')
        print()
        return pedido

    def calcular_cant(self):
        final = []
        elementos = list(set(self.lista_pedido))
        for elemento in elementos:
            cant = self.lista_pedido.count(elemento)
            final.append([elemento, cant])
        return final

    def eliminar_elemento(self, nombre):
        while nombre in self.lista_pedido:
            self.lista_pedido.remove(nombre)
        self.mostrar_pedido()




