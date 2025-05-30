import pickle


def menores_idade(lista_carregada):
    menores = [] #Saída: lista. Criando lista vazia
    for pessoa in lista_carregada: #Percorrendo a lista de pessoas
        if pessoa[1] < 18: #Selecionando as pessoas com menos de 18 anos
            menores.append(pessoa) #Adicionando elas à lista
    return menores #Devolvendo a lista apenas com as pessoas menores de idade


with open("exercicio01.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_menores = menores_idade(lista_carregada)
print(lista_menores)