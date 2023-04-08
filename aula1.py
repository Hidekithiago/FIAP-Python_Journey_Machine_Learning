def HelloWorld():
    print("Hello World")

def MostraNome():    
    nome = 'Hideki'
    print(nome)

def MostraNumero():
    a = 10
    print(a)

def PedeNome():
    nome = input("Digite o nome")
    print("O nome digitado foi " + nome)

def Calculadora():
    print("PROGRAMA CALCULADORA")
    valor1 = input("Por favor, digite o primeiro valor: ")
    valor2 = input("Poffavor, digite o segundo valor: ")
    soma = valor1 + valor2
    subtracao= valor1 - valor2
    divisao= valor1 / valor2
    multiplicacao= valor1 * valor2
    print("A soma entre os dois valores é de " + soma)
    print("A subtração entre os dois valores é de " + subtracao)
    print("A divisão entre os dois valores é de " + divisao)
    print("A multiplicação entre os dois valores é de " + multiplicacao)
    
    print("A soma entre os dois valores é de {}".format(soma))
    print("A subtração entre os dois valores é de {}".format(subtracao))
    print("A divisão entre os dois valores é de {}".format(divisao))
    print("A multiplicação entre os dois valores é de {}".format(multiplicacao))
    
def ValidaIdade():
    print("PROGRAMA VALIDADOR DE IDADE!")
    idade = int(input("Por favor, digite sua idade"))
    if(idade >= 12):
        print("Você pode jogar!")
        
def GestaoDoacao():
    print("PROGRAMA DE GESTÃO DE DOAÇÕES")
    doacao= float(input("Por favor, digite o valor da doação recebida!"))
    if(doacao< 1000.00):
        investimento = doacao * 0.05
        usoImediato= doacao-investimento
    else:
        investimento = doacao* 0.15
        usoImediato= doacao-investimento
    print("A doação de R$ {} implica em um investimento de R$ {}, restando R$ {} para uso imediato".format(doacao, investimento, uso_imediato))

def ValidaPassageiro():
    print("PROGRAMA VALIDADOR DE PASSAGEIROS")
    idade = int(input("Por favor, digite a idade do passageiro: "))
    if(idade < 16):print("O passageiro não pode votar nem embarcar")
    else:
        if(idade>=18):
            print("O passageiro deve votar e pode embarcar")
        else:
            print("O voto do passageiro é opcional e ele pode embarcar")
            
def ConversaoDollarReal():
    dollar = float(input("Qual o valor a ser convertido?"))
    conversao = float(input("Qual a taxa de conversao?"))
    print("O valor convertido é R$ {:.2f}".format(dollar*conversao))

def Km_Litro():
    #entradas
    kmInicial = float(input("Por favor, informe a Km inicial do veículo: "))
    kmFinal = float(input("Por favor, informe a Km final do veículo: "))
    qtdLitrosAbastecidos = float(input("Por favor, informe a quantidade de litros abastecidos: "))
    #operações
    kmFinal = kmFinal - kmInicial
    media = kmFinal/qtdLitrosAbastecidos
    #saídas
    print("O veículo fez uma média de {} km por litro" .format(media))
    
    
# get random forest model   