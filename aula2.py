import math
'''
login = False
k = 0
while(login is False):
    user = input("DIgite o login")
    password = input("DIgite a senha")
    k+=1
    if user.upper() == "ADMIN" and password.upper() == "123":
        print("Esta logado")
        login = True
    else:
        print("Dados de acesso incorreto")
    print("Quantidade de tentativas ")

'''

'''
for i in range(0,1000,1):
    print(i) 
'''    

'''    
valor1 = int(input("Valor base da tabuada: "))
for k in range (1,11,1):
    print(valor1 * k)
'''

'''
def menu():
    print("Escolha a opção:")
    print("1 - Digitar os valores")
    print("2 - Realizar Soma")
    print("3 - Realizar Subtracao")
    print("4 - Realizar Multiplicação")
    print("5 - Realizar Divisão")
    print("6 - Sair do sistema")
    itemMenu = input("Digite o menu")
def resultado():
    print("Resultado da conta: "+str(resultado))
def conta():
    if itemMenu == 1:
    elif itemMenu == 2:
    elif itemMenu == 3:
    elif itemMenu == 4:    
def atribuicao():
    v1 = input("Digite o valor 1: ")
    v2 = input("Digite o valor 2: ")
    
    
'''

'''Exibir numeros pares
for x in (0,101,2)
    print (x)
'''

'''Exibir a soma dos numeros de 0 a 100
for x in (0,101,1)
    res = res + x
'''
'''Exibir a soma dos numeros de 0 a 100 exceto do 50 a 75
for x in (0,101,1)
    if x < 50 or x > 75:
        print(x)
'''
# 4. usuário informa um número e o sistema calcula o fatorial deste número
'''
x = int(input("DIgite um valor para fatorial: "))
print(math.factorial(x))
''' 
# 5. usuário informa uma qtd de termos e o sistema calcula a série Fibonacci
xx = int(input("DIgite um valor para fatorial: "))
inicio = 0
fim =  1
res = 0
for x in range(1, xx, 1):
    
    inicio = res    
    fim = inicio + fim
    
    res = inicio + fim
print (fim)