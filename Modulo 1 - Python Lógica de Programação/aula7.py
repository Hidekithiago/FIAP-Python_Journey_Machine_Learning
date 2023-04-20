'''
Um grafo é um conjunto de conexões, onde temos os nós ou vértices (N) e as arestas ou arcos (A). 
Trata-se de um modelo ou representação da realidade e nos ajuda com simulações.

Grafo Dirigido
    •É uma dupla (N, A), que se pode definir a ordem nos pares de nós
Grafo Não Dirigido
    •Não pode definir a ordem nos pares de nós.
    
Grau de um Nó
    Grau 2 = uma saída mais uma entrada;
    Grau 5(3+2)= três saídas mais duas entradas.

Pesos das arestas
    O peso dos arcos representa o grau de importância na conexão entre dois nós.
    
Grafo Cíclico
    Existe um caminho de no mínimo três “nós” que começam e terminam no mesmo “Nó”
Grafo Acíclico
    Não ocorre nenhum ciclo em circuito nos “Nós”.
Lista de Adjacência
    Usa um vetor com n listas ligadas(filas). Cada posição do vetor corresponde a um Nó de G(N,A), e os arcos de um certo Nó para outros Nós são representados por listas ligadas
Matriz de Adjacência 
    Assume que os Nós são numerados de 1 até N. A matriz é construída com dimensão NxN de elementos eij.
    
Busca em Largura
    •A pesquisa em largura busca pelo caminho mínimo, ou seja, o mínimo de arestas a serem percorridas para chegar ao objetivo final.
    •A busca começa por um vértice especificado pelo usuário, depois consulta os vértices vizinhos e todos os vizinhos dos vizinhos.
    •O algoritmo numera os vértices na ordem em que eles são descobertos; para fazer isso, o algoritmo usa uma filade vértices. 

'''
from collections import deque

def BuscaGrafo():
    '''Implementação do algoritmo
        Para implementar o algoritmo, devemos:
        1.criar uma fila de todas as pessoas que serão verificadas(comece pelo centro);
        2.retirar uma pessoa da fila e verificar se é um pescador;
        3.caso seja, encontramos o que precisamos, senão, devemos adicionar todos os vizinhos dessa pessoa na fila;
        4.repetir o passo 2.'''
    
def Pesquisa(nome):
    grafo={}
    grafo['maria']=['joão','miriam','jose']
    grafo['joão']=['paulo','pedro']
    grafo['jose']=['miriam']
    grafo['miriam']=['elias']
    fila = deque()
    fila += grafo[nome]
    print(fila)
    verificadas = []
    while fila:
        pessoa = fila.popleft()
        if not pessoa in verificadas:
            if pescador(pessoa):
                print(pessoa + ' e pescador')
                return True
            else:
                fila += grafo[pessoa]
                verificadas.append(pessoa)
    print('Nao existe pescador')
    return False

def pescador(nome):
    return nome [-1] == 's'

Pesquisa('jose')


grafo = {}
grafo['inicial'] = {}
grafo['inicial']['a'] = 8
grafo['inicial']['b'] = 3    
grafo['a']= {}
grafo['a']['final'] = 2
grafo['b']={}
grafo['b']['a'] = 3
grafo['b']['final'] = 6
grafo['final'] = {}

infinito = float('inf')
custos = {}
custos['a'] = 8
custos['b'] = 3
custos['final'] = infinito

pais = {}
pais['a'] = 'inicial'
pais['b'] = 'inicial'
pais['final'] = None

processados=[]
    
def achar_melhor_custo(custos):
    custo_baixo = float('inf')
    vertice_melhor_custo = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < custo_baixo and vertice not in processados:
            custo_baixo = custo
            vertice_melhor_custo = vertice
    return vertice_melhor_custo

vertice = achar_melhor_custo(custos)

while vertice is not None:
    custo = custos[vertice]
    vizinhos = grafo[vertice]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = vertice
    processados.append(vertice)
    vertice = achar_melhor_custo(custos)
    
print(custos)