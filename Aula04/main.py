class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percetual):
        self.preco = self.preco - (self.preco * (percetual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome
    
    # Setter
    @nome.setter
    def nome(self, nomeProduto):
        self._nome = nomeProduto.title()
            
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self._preco = valor
        
p1 = Produto('CANECA', 'R$200')
p1.desconto(10)
print(p1.nome)
print(p1.preco)


        
