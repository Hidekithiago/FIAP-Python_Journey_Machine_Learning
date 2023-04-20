class Cliente():

    def __init__(self, nome, endereco, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__situacao = False

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def ativar(self):
        self.situacao = True
        print("Cliente : ", self.__nome + " ativado(a) com sucesso!")

    def desativar(self):
        self.situacao = False
        print("Cliente : ", self.__nome + " desativado(a) com sucesso!")




