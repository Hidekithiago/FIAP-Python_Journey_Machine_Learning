from iproduto import IProduto

class Fundos(IProduto):
    def investir(self, valor) -> float:
        return valor * 1.1