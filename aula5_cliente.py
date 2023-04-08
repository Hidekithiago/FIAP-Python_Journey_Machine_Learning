class Cliente():
    def __init__(self, nome, endereco, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__telefone = False    
    def setNome(self, nome):
        self.__nome = nome
    def setEndereco(self, endereco):
        self.__endereco = endereco
    def setCpf(self, cpf):
        self.__cpf = cpf
    def setTelefone(self):
        self.__telefone = cpf
        
if __name__ == '__main__':
    cliente1 = Cliente('Hideki', 'Rua A, 32', 12345678910)
    cliente1.ativar()