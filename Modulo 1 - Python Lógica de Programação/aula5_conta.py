from aula5_cliente import Cliente

class Conta():
    def __init__(self, nome, endereco, cpf, numero):
        self.cliente = Cliente(nome, endereco, cpf)
        self.saldo = 0.0
        self.numero = numero
    def setSaldo(self, saldo):
        self.saldo = saldo
    def setNumero(self, numero):
        self.numero = numero
    def getSaldo(self):
        return self.saldo
    def getNumero(self):
        return self.numero
            
if __name__ == '__main__':
    conta1 = Conta('Hideki', 'Rua A', '12345678910', 1)
    conta1.setSaldo = 14.0
    print(conta1.getNumero())
    
    print(conta1.setSaldo())