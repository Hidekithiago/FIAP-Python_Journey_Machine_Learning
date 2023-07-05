from conta_corrente import ContaCorrente
from lca import LCA
from cdb import CDB
from fundos import Fundos

conta_maria = ContaCorrente("Maria", "Rua 123 de oliveira 4", "123456799", 1)
print("Cliente: " + conta_maria.cliente.get_nome())

conta_jose = ContaCorrente("José", "Rua 123 de oliveira 4", "123456789", 2)
print("Cliente: " + conta_jose.cliente.get_nome())

conta_jose.depositar(1000)
conta_maria.depositar(2000)

conta_jose.sacar(500)
conta_maria.sacar(1000)

conta_maria.exibir_saldo()
conta_jose.exibir_saldo()

conta_jose.transferir(conta_maria, 100)

conta_maria.exibir_saldo()
conta_jose.exibir_saldo()

cdb = CDB()
lca = LCA()
fundos = Fundos()

conta_jose.calcular_investimento(lca, 200)

conta_jose.exibir_saldo()
print(conta_jose.saldo_investimento)