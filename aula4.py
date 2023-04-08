def exercicio1():
    arquivo = open(path)
    linhas_do_arquivo = arquivo.readlines()
    print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))
    linhas_do_arquivo.sort()
    print(linhas_do_arquivo)
    arquivo.close()
    
def exercicio2(texto):    
    arquivo = open(path, "w")
    arquivo.write(texto)
    arquivo.close()
    
def exercicio3(texto):    
    with open(path, "w") as arquivo:
        arquivo.write(texto)
        arquivo.close()


if __name__ == "__main__":
    path = r"C:\Users\Hideki\Desktop\GitHub\FIAP-Python_Journey_Machine_Learning\aula4.txt"
    texto = "TESTE de escrita"
    #exercicio1()
    #exercicio2(texto)
    #exercicio3(texto)