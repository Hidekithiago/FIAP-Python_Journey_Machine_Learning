from conta import Conta
from typing import Type
from iproduto import IProduto

class ContaCorrente(Conta):
    def __init__(self, nome, endereco, cpf, numero_conta):
        super().__init__(nome, endereco, cpf, numero_conta)
        self.saldo_investimento = 0.0

    def calcular_investimento(self, produto: Type[IProduto], valor):
        teste = self.sacar(valor)
        if(teste==True):
          self.saldo_investimento += produto.investir(valor)