import json

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
def listas():    
    print(jedi)
    print(jedi[1])    
    jedi.append("Mace Windu") #Adicionando na ultima posicao
    Mostrar()
    jedi.insert(2, "Luminara") #Adicionando na segunda posicao
    Mostrar()
    jedi.pop() #Remove a ultima posicao
    Mostrar()
    jedi.pop(1) #Remove a prineira posicao
    Mostrar()
    contagem = jedi.count("Yoda")
    print("Nessa lista o nome Yoda aparece {} vezes".format(contagem))
    jedi.sort() #Ordena crescente
    jedi.reverse() #Inverte a lista
    
def Mostrar():
    print('\n')
    for nome in jedi:
        print(nome)

def OrdenarNotas():
    notas = []
    encerrar = "NÃO"
    while "N" in  encerrar.upper() :
        notas.append(float(input("Por favor, digite uma nova nota")))
        encerrar = input("Deseja FINALIZAR a digitação? S -SIM ou N -NÃO")
        print("Ao total, {} alunos tiraram nota 10!".format(notas.count(10)))
        notas.sort()
        notas.reverse()
        print("NOTAS DA TURMA:")
        for nota in notas:
            print(nota)

'''
As listssão incríveis, mas foram criadas para um cenário bem específico: trabalhar com listas de dados que serão modificados ao longo do programa.
Para fazer isso, elas acabam ocupando bastante espaço em memória.
Para casos de dados que não serão modificados durante a execução do script temos uma estrutura mais adequada: a tupla (tuple).
A tupla pode ser entendida como uma lista que não pode sofrer alterações.
'''
categorias_jedi= ("Youngling", "Padawan", "Knight", "Master")
def Tupla():    
    print(categorias_jedi)
    print(categorias_jedi[2])
    print(categorias_jedi[-1]) #Mostra ultimo elemento 
    for categoria in categorias_jedi: print(categoria)
    
def Personagens():
    #Criando as duas listas
    personagens=[]
    categorias=[]
    #Executando um loop 10 vezes
    for x in range(10):
        #pedindo que o usuário informe um nome e colocando na lista de personagens
        personagens.append(input("Informe o nome do personagem: "))
        #pedindo que o usuário informe a categoria e colocando na lista de categorias
        categorias.append(input("Informe a categoria do personagem: "))
        #Executando um loop 10 vezes
        for indice in range(10):
            #exibindo a cada volta o que está contido em um índice de personagens e categorias
            print("O personagem {} é um(a) {}".format(personagens[indice], categorias[indice]))
            
def Dicionario():
    personagens = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
    for valor in personagens.values(): print(valor)
    for chave in personagens.keys(): print(chave)
    for chave, valor in personagens.items(): print("O personagem {} é da categoria {}".format(chave, valor))
    personagens["Darth Vader"] = "Sith" #Adicionando nova chave
    personagens.pop("R2-D2") #Removendo chave
    personagens.popitem() #Removendo ultima chave
    personagens.clear() #Limpa o dicionario
    
def OrdenaNotasDicionario():
    notas = {}
    encerrar = "NÃO"
    while "N" in  encerrar.upper() :
        aluno =  input("Por favor, digite o nome do aluno")
        nota = float(input("Por favor, digite a nota do aluno"))
        notas[aluno] = notaencerrar = input("Deseja FINALIZAR a digitação? S -SIM ou N -NÃO")
    total = 0
    for nota in notas.values() :
        if nota == 10.00:
            total = total + 1
    print("Ao total, {} alunos tiraram nota 10!".format(total))
    print("NOTAS DA TURMA:")
    for aluno, nota in notas.items():
        print("O aluno {} tirou nota {}".format(aluno, nota))
        
def Json():
    contatos = {
        "Clark Kent":{
            "Celular":"123456",
            "Email":"super@krypton.com"
        },
        "Bruce Wayne":{
            "Celular":"654321",
            "Email":"bat@caverna.com.br"
        }
    }
    dados_json = json.dumps(contatos, indent=4)
    print(dados_json)
    #Cria um arquivo .json e salva os dados
    arquivo = open("c:\\agenda.json", "w")
    arquivo.write(dados_json)
    arquivo.close()
    #Abre e le um arquivo .json
    arquivo = open("c:\\arquivos\\agenda.json")
    conteudo_do_arquivo= arquivo.read()
    arquivo.close()
    agenda = json.loads(conteudo_do_arquivo) #Converte em dicionario
    
#def metodo(*args): #Passa quantos parametros precisar sem definir a quantidade
#def metodo(**args): #Passa um dicionario