import math

def login():
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

def contador():
    for i in range(0,1000,1):
        print("Nessa volta o contador possui o valor: {}".format(contador))
   
def tabuada():
    valor1 = int(input("Valor base da tabuada: "))
    for k in range (1,11,1):
        print(valor1 * k)
    
    
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
def fatorial(numero):
    if (numero == 0):
        print(1)
    else:
        fatorial = 1
        while (numero > 1):
            fatorial *= numero
            numero -= 1
    print(fatorial)

def fibonacci(numero):
    ultimo = 1
    penultimo = 1
    if numero == 1:
        print('0')
    elif numero == 2:
        print('0', '1')
    else:
        print('0')
        print(ultimo)
        print(penultimo)
    for i in range(2, numero):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        i += 1
        print(termo)
fibonacci(10)