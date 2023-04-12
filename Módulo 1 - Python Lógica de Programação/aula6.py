'''

Métodosde Ordenação/ Classificação
Existem 4 métodos gerais de ordenação:
✓Inserção:
    ✓Inserção direta
    ✓Incremento decrescente (Shell Sort)
✓Troca:
    ✓Método da bolha (Bubble Sort)
    ✓Método da troca e partição (Quick Sort)
✓Seleção
    ✓Seleção direta (SelectionSort)
    ✓Seleção em árvore (HeapSort)
✓Intercalação
    ✓Merge Sort

'''

import random
def insercao_direta(vetor):
    '''    
    •Dado um vetor para ordenação, percorre elemento por elemento deslocando-o e inserindo-o na posição ordenada.
    •A ideia é formar um bloco de valores ordenados e outro de desordenados e ir passando os valores de um bloco a outro.
    •Usado para conjunto pequeno de dados.
    •Baixa eficiência    
    '''
    n = len(vetor)
    for j in range(1, n):
        temp= vetor[j]
        i = j -1
        while i >= 0 and vetor[i] > temp:
            vetor[i + 1] = vetor[i]
            i = i -1
        vetor[i + 1] = temp
             
def shell_sort(vetor, n):
    '''
    •Extensão do algoritmo de inserção direta
    •Diferença: o vetor usado no processo de classificação é dividido em vários segmentos (blocos).
    •Faz classificações parciais do vetor, aumentando o desempenho nos passos seguintes.
    '''
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp= vetor[i]
            j = i
            while j >= intervalo and vetor[j -intervalo] > temp:
                vetor[j] = vetor[j -intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo = intervalo // 2
     
def bubble_sort(vetor):
    '''
    •Simples e fácil implementação.
    •Ordenação por troca de valores entre posições consecutivas, fazendo com que os valores mais altos (ou mais baixos) “borbulhem” para o final do arranjo.
    •Ele envolve repetidas comparações.•Seu desempenho é muito ruim.
    '''
    for i in range(len(vetor), 0, -1):
        troca = False
        for j in range(0, i -1):
            if vetor[j] > vetor[j + 1]:
                vetor[j + 1], vetor[j] = vetor[j], vetor[j + 1]
                troca = True
                if not troca:
                    break 
        
def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def quick_sort(vetor, inicial, final):
    '''
    •É baseado em uma estratégia de dividir para conquistar
    •É um dos algoritmos de ordenação mais populares.
    •Seu desempenho é melhor na maioria das vezes.
    Baseia-se na divisão de um vetor em dois subvetores, de tal forma que todos os elementos do vetor 1 sejam < = a todos os elementos do vetor 2.
    Estabelecida a divisão, o problema estará resolvido, pois aplica-se recursivamente a mesma técnica a cada um dos subvetores, no final o vetor estará ordenado ao se obter um  subvetorde apenas 1 elemento.
    '''
    if inicial < final:
        resultado_divisao= dividir(vetor, inicial, final) 
        quick_sort(vetor, inicial, resultado_divisao-1) 
        quick_sort(vetor, resultado_divisao+ 1, final)     

def dividir(vetor, inicial, final):
    x = vetor[inicial] 
    i = inicial 
    j = inicial + 1
    while(j<=final):
        if vetor[j] < x:
            i += 1 
            trocar(vetor, i, j)
        j += 1
        trocar(vetor, inicial, i)
        return i
def trocar(vetor, n, m):
    temp= vetor[n]
    vetor[n] = vetor[m]
    vetor[m] = temp

lista = random.sample(range(1,100), 20)

'''
print("Lista não ordenada: ", lista)
#insercao_direta(lista)
#shell_sort(lista, len(lista))
#bubble_sort(lista)
print("Lista ordenada:", lista)
'''
print(soma(5))
print(fatorial(5))
for x in range(1, 2): 
    fibonacci(x)
print()

print("Lista não ordenada: ", lista)
quick_sort(lista, 0 , len(lista)-1)


def selection_sort(vetor):
    '''
    •SelectionSorté um dos algoritmos de ordenação mais simples. 
    •Percorre o vetor ao longo das iterações e seleciona o menor elemento atual e o troca de lugar.
    '''
    if not vetor:
        return vetor
    for i in range(len(vetor)):
        min = i
        for j in range(i + 1, len(vetor)):
            if vetor[j] < vetor[min]:
                min = j
        vetor[i], vetor[min] = vetor[min], vetor[i]