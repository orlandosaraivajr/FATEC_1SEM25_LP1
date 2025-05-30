import pickle


def media_nota(lista_carregada):
    medias = [] #Saída: lista de tuplas. Criando a lista
    for tupla in lista_carregada: #Percorrendo a lista de entrada
        media = round(((tupla[1] + tupla[2] + tupla[3])/ 3), 2) #Calculando e formatando a média
        medias.append((tupla[0], media)) #Acrescentando a nova tupla à lista
    return medias #Retornando a lista de tuplas

def situacao_falta(lista_carregada):
    faltas = [] #Saída: lista de tuplas. Criando a lista
    for tupla in lista_carregada: #Percorrendo a lista de entrada
        if tupla[4] < 6: #Selecionando alunos com menos de seis faltas
            faltas.append((tupla[0], 'Aprovado')) #Adicionando a nova tupla de aprovados à lista
        elif tupla[4] >= 6: #Selecionando alunos com muitas faltas
            faltas.append((tupla[0], "Reprovado")) #Adicionando a nova tupla de reprovados à lista
    return faltas #Retornando a lista de tuplas

def acima_de_nove(lista_carregada):
    noves = [] #Saída: lista com nomes dos alunos. Criando a lista
    for tupla in lista_carregada: #Percorrendo a lista de tuplas
        if tupla[1] >= 9 and tupla[2] >= 9 and tupla[3] >= 9: #Selecionando as 3 notas maiores que 9
            noves.append(tupla[0]) #Adicionando os nomes dos alunos
    return noves #Retornando a lista com nomes dos alunos

def uma_nota_abaixo_de_seis(lista_carregada):
    abaixo_seis = [] #Saída: lista com tuplas. Criando a lista
    for tupla in lista_carregada: #Percorrendo a lista de tuplas
        if tupla[1] <= 6 or tupla[2] <= 6 or tupla[3] <= 6: #Selecionando qualquer nota igual ou abaixo de 6
            abaixo_seis.append((tupla[0], tupla[1], tupla[2], tupla[3])) #Adicionando a nova tupla à lista
    return abaixo_seis #Retornando a lista de tuplas


with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(media_nota(lista_carregada))
print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))