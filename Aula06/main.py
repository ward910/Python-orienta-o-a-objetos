"""
public, protected, private
_
__
"""

class Carro:
    def __init__(self):
        self.__modelosCarros = {}

    @property
    def dados(self):
        return self.__modelosCarros

    @dados.setter
    def dados(self, valor):
        self.__modelosCarros = valor
        
    def inserirModelos(self, modelo, cor):
        self.__modelosCarros[modelo] = cor

    def listar(self):
        print(self.__modelosCarros)

    def deleter(self, id):
        del self.__modelosCarros[id]

carro = Carro()
carro.inserirModelos('Kombi', 'azul')
carro.inserirModelos('Fusca', 'rosa')
carro.deleter('Kombi')
carro.listar()

        
