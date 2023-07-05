from iproduto import IProduto

class CDB(IProduto):
    def investir(self, valor) -> float:
        return valor * 1.01