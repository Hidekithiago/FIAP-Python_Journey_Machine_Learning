from random import random

class Item():
    def __init__(self, nome, valor, peso):
        self.nome = nome
        self.valor = valor
        self.peso = peso

class Individuo():
    def __init__(self, pesos, valores, limite_peso=10, geracao=0):
        self.pesos = pesos
        self.valores = valores
        self.limite_peso = limite_peso
        self.peso_total = 0
        self.avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []

        for i in range(len(pesos)):  # inicializar aleatoriamente a solução (indivíduo)
            if random() < 0.5:  # número randômico entre 0 e 1 com 50% de chance para cada (0.5)
                self.cromossomo.append("0") #inicialização do cromossomo adicionando genes
            else:
                self.cromossomo.append("1")

    def fitness(self):
        nota = 0
        soma_pesos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_pesos += self.pesos[i]
        if soma_pesos > self.limite_peso:
            nota = 1
        self.avaliacao = nota
        self.peso_total = soma_pesos

    def crossover(self, individuo):
        ponto_corte = round(random() * len(self.cromossomo)) #numero aleatório entre 0 e 1 X tamanho do cromossomo
        filho1 =  self.cromossomo[0:ponto_corte] + individuo.cromossomo[ponto_corte::]# da posição de corte até o restante
        filho2 =  individuo.cromossomo[0:ponto_corte] + self.cromossomo[ponto_corte::]

        filhos = [Individuo(self.pesos, self.valores, self.limite_peso, self.geracao + 1),
                  Individuo(self.pesos, self.valores, self.limite_peso, self.geracao + 1)]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos

    def mutacao(self, taxa_mutacao = 0.05):
        #print("Antes = %s " % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        #print("Depois = %s " % self.cromossomo)
        return self

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao=5):
        self.tamanho_populacao = tamanho_populacao
        self.geracao = 0
        self.melhor_solucao = 0
        self.populacao = []
        self.solucoes = []

    def comeca_populacao(self, pesos, valores):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(pesos, valores))
            self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.avaliacao,
                                reverse=True)

    def melhor_individuo(self, individuo):
        if individuo.avaliacao > self.melhor_solucao.avaliacao:
            self.melhor_solucao = individuo

    def total_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.avaliacao
        return soma

    def roleta_viciada(self, total_avaliacao):
        pai = -1
        valor_sorteado = random() * total_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].avaliacao
            pai += 1
            i += 1
        return pai

if __name__ == "__main__":
    lista_itens = []
    lista_itens.append(Item("Lanterna", 80, 1))
    lista_itens.append(Item("Faca", 85, 1))
    lista_itens.append(Item("Roupas", 90, 3))
    lista_itens.append(Item("Livros", 50, 0.5))
    lista_itens.append(Item("Saco de dormir", 105, 2))
    lista_itens.append(Item("Remédios", 90, 2))
    lista_itens.append(Item("Alimentos", 200, 4))
    lista_itens.append(Item("Rede de descanso", 100, 2.5))

valores = []
pesos = []

for item in lista_itens:
    valores.append(item.valor)
    pesos.append(item.peso)

algoritmo_genetico = AlgoritmoGenetico()
algoritmo_genetico.comeca_populacao(pesos,valores)

for individuo in algoritmo_genetico.populacao:
    individuo.fitness()

algoritmo_genetico.ordena_populacao()
algoritmo_genetico.melhor_individuo(algoritmo_genetico.populacao[0])
print("Melhor solução: %s" % algoritmo_genetico.melhor_solucao.cromossomo,
      "\nNota = %s " % str(algoritmo_genetico.melhor_solucao.avaliacao))

total_avaliacoes = algoritmo_genetico.total_avaliacoes()
print("Total: %s" % total_avaliacoes)

nova_populacao = []

for individuos in range(0, algoritmo_genetico.tamanho_populacao, 2):
    pai1 = algoritmo_genetico.roleta_viciada(total_avaliacoes)
    pai2 = algoritmo_genetico.roleta_viciada(total_avaliacoes)

    filhos = algoritmo_genetico.populacao[pai1].crossover(algoritmo_genetico.populacao[pai2])
    nova_populacao.append(filhos[0].mutacao())
    nova_populacao.append(filhos[1].mutacao())

algoritmo_genetico.populacao = list(nova_populacao)
for individuo in algoritmo_genetico.populacao:
    individuo.fitness()
algoritmo_genetico.ordena_populacao()
algoritmo_genetico.melhor_individuo(algoritmo_genetico.populacao[0])
soma = algoritmo_genetico.total_avaliacoes()

print("Solução escolhida: %s" % algoritmo_genetico.melhor_solucao.cromossomo, "\nValor: %s" % algoritmo_genetico.melhor_solucao.avaliacao)

"""

for i in range(algoritmo_genetico.tamanho_populacao):
    print("Individuo: %s" % i, "Pesos = %s" % str(algoritmo_genetico.populacao[i].pesos),
          "Valores = %s" % str(algoritmo_genetico.populacao[i].valores),
          "Cromossomo = %s" % str(algoritmo_genetico.populacao[i].cromossomo),
          "Avaliação: %s" % str(algoritmo_genetico.populacao[i].avaliacao))

individuo1 = Individuo(pesos, valores)
print("Indivíduo 1")
print("Pesos = %s" % str(individuo1.pesos))
print("Valores = %s" % str(individuo1.valores))
print("Cromossomo = %s" % str(individuo1.cromossomo))

individuo1.fitness()
print("Avaliação = %s " % individuo1.avaliacao)
print("Peso total:  = %s " % individuo1.peso_total)

print("----------------")

individuo2 = Individuo(pesos, valores)
print("Indivíduo 2")
print("Pesos = %s" % str(individuo2.pesos))
print("Valores = %s" % str(individuo2.valores))
print("Cromossomo = %s" % str(individuo2.cromossomo))

individuo2.fitness()
print("Avaliação = %s " % individuo2.avaliacao)
print("Peso total  = %s " % individuo2.peso_total)

filhos = individuo1.crossover(individuo2)
print("Filho 1 = %s" % filhos[0].cromossomo)
print("Filho 2 = %s" %filhos[1].cromossomo)

individuo1.mutacao()
individuo2.mutacao()

"""