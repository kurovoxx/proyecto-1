from Manejar_ingredientes import Despensa


class Cocina:
    def __init__(self, main, despensa: Despensa):
        self.despensa = despensa
        self.main = main

    def make_papas(self):
        if self.despensa.ingredientes['papa'] >= 5:

            self.despensa.ingredientes['papa'] -= 5

            print('Se han cocinado unas papas fritas!')
            self.ver_despensa()
            self.main.pedido.add_elemento('Papas Fritas')
            self.main.update_tree_ingredientes()
            self.main.update_tree_pedido()
        else:
            print('No hay ingredientes suficientes.')
            self.main.cartas.tarjeta_papas.destroy()

    def make_bebida(self):
        if self.despensa.ingredientes['bebida'] >= 1:

            self.despensa.ingredientes['bebida'] -= 1

            print('Se ha hecho una bebida!')
            self.ver_despensa()
            self.main.pedido.add_elemento('Pepsi')
            self.main.update_tree_ingredientes()
            self.main.update_tree_pedido()
        else:
            print('No hay ingredientes suficientes.')

    def make_completo(self):
        if (self.despensa.ingredientes['pan de completo'] >= 1 and
                self.despensa.ingredientes['vienesa'] >= 1 and
                self.despensa.ingredientes['tomate'] >= 1 and
                self.despensa.ingredientes['palta'] >= 1):

            self.despensa.ingredientes['pan de completo'] -= 1
            self.despensa.ingredientes['vienesa'] -= 1
            self.despensa.ingredientes['tomate'] -= 1
            self.despensa.ingredientes['palta'] -= 1

            print('Se ha cocinado un completo!')
            self.ver_despensa()
            self.main.pedido.add_elemento('Completo')
            self.main.update_tree_ingredientes()
            self.main.update_tree_pedido()
        else:
            print('No hay ingredientes suficientes.')

    def make_hamburguesa(self):
        if (self.despensa.ingredientes['pan de hamburguesa'] >= 1 and
                self.despensa.ingredientes['lamina de queso'] >= 1 and
                self.despensa.ingredientes['churrasco de carne'] >= 1):

            self.despensa.ingredientes['pan de hamburguesa'] -= 1
            self.despensa.ingredientes['lamina de queso'] -= 1
            self.despensa.ingredientes['churrasco de carne'] -= 1

            print('Se ha cocinado una hamburguesa!')
            self.ver_despensa()
            self.main.pedido.add_elemento('Hamburguesa')
            self.main.update_tree_ingredientes()
            self.main.update_tree_pedido()
        else:
            print('No hay ingredientes suficientes.')

    def ver_despensa(self):
        self.despensa.mostrar_ingredientes()


'''mi_despensa = Despensa()

mi_despensa.add_ingrediente(Ingrediente('lechuga', 20))
mi_despensa.add_ingrediente(Ingrediente('papas', 10))
mi_despensa.add_ingrediente(Ingrediente('lechuga', 5))
mi_despensa.add_ingrediente(Ingrediente('hamburguesa', 5))
mi_despensa.add_ingrediente(Ingrediente('pan', 10))

mi_cocina = Cocina(mi_despensa)

mi_cocina.ver_despensa()
for i in range(10):
    mi_cocina.make_hamburguesa()'''


'''
-Debería hacer un ingreso de todos los ingredientes = 0 para evitar ingredientes[tal] no existe?
-Hacer lo de arriba me permitiría tener una vista general del stock y podría agregar un combobox para seleccionar
ingredientes en ves de un entry (lo que evitaría el riesgo de ingresar mal el nombre de un ingrediente u olvidar que
ingredientes hay disponibles para agregar)
-Sería más organizado tener una lista de las condiciónes para cada alimento o las pongo todas en el if directamente?
'''