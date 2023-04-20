from cliente import Cliente

class Conta():
    def __init__(self, nome, endereco, cpf, numero_conta):
        self.cliente = Cliente(nome, endereco, cpf)
        self.saldo = 0.0
        self.numero_conta = numero_conta

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor)->bool:
        if(self.saldo>=valor):
            self.saldo -= valor
            return True
        return False

    def transferir(self, conta, valor):
        teste = self.sacar(valor)
        if(teste==True):
            conta.depositar(valor)

    def exibir_saldo(self):
        print("Cliente: " + self.cliente.get_nome())
        print("Saldo: ", self.saldo)



