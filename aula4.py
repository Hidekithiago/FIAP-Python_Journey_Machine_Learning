import pandas as pd
import numpy as np

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
    
def arrayNP():
    novo_array= np.array([1,2,3])
    print("Abaixo está seu array")
    print(novo_array)
    print("Esse é um ndarraycom {} dimensões".format(novo_array.ndim))
    print("As dimensões desse ndarraypossuem os seguintes tamanhos: {}".format(novo_array.shape))
    print("Ao todo, esse ndarraycontém {} elementos".format(novo_array.size))
    print("Os elementos presentes nesse ndarraysão do tipo {}".format(novo_array.dtype))
    print("Os elementos presentes nesse ndarrayocupam {} bytes".format(novo_array.itemsize))

def arrayTuplasNP():
    array_tupla= np.array([(1,2,3), (4,5,6)])
    print("Abaixo está seu arrayformado através de tuplas")
    print(array_tupla)
    array_lista= np.array([[1,2,3], [4,5,6]])
    print("Abaixo está seu arrayformado através de listas")
    print(array_lista)
    
def ndArrayZeroNP():
    array_zerado= np.zeros((3, 4))
    print("O arraygerado com zeros ficou assim:")
    print(array_zerado)
    array_de_uns= np.ones((5,2), dtype=np.int32)
    print("O arraygerado com uns ficou assim:")
    print(array_de_uns)
    array_aleatorio= np.empty((6,3), dtype=np.int32)
    print("O arraygerado com valores aleatórios ficou assim:")
    print(array_aleatorio)
    array_gerado= np.arange(10).reshape(2,5) #Altera a dimensao do array
    print("O arraygerado com  ficou assim:")
    print(array_gerado)
    
def dtFrame():
    indice_datas= pd.date_range("20200101", periods=6)
    print("Abaixo está a estrutura que contém o índice das datas")
    print(indice_datas)
    array_aleatorio= np.empty((6,4), dtype=np.int32)
    print("Abaixo está nosso arrayaleatorioque representa os dados do dataframe")
    print(array_aleatorio)
    dataframe= pd.DataFrame(array_aleatorio, index=indice_datas, columns=['A', 'B', 'C', 'D'])
    print("Abaixo está nosso dataframe")
    print(dataframe)