import pickle


def buscar_pessoa_por_cidade(lista_carregada, cidade):
    mesma_cidade = [] #Saída: lista. Criando a lista
    cidade = cidade.lower() #Formatando a entrada, atualizando a variável
    for tupla in lista_carregada: #Percorrendo a lista de tuplas
        if tupla[1].lower() == cidade: #Selecionando as tuplas (formatadas) que contém a mesma cidade
            mesma_cidade.append(tupla) #Adicionando as tuplas à nova lista
    return mesma_cidade #Retornando a lista com as tuplas com a mesma cidade

def buscar_pessoa_por_numero(lista_carregada, numero):
    numero_menor = [] #Saída: lista. Criando a lista
    for tupla in lista_carregada: #Percorrendo a lista de tuplas
        if tupla[2] <= numero: #Selecionando as tuplas que contém o número igual ou menor que a entrada
            numero_menor.append(tupla) #Adicionando às tuplas à nova lista
    return numero_menor #Retornando a lista com as tuplas com o número igual ou menor

def buscar_pessoa_por_numero_e_cidade(lista_carregada, cidade, numero): #Juntando as duas funções
    cidade_numero = [] #Saída: lista. Criando a lista
    cidade = cidade.lower() #Formatando e atualizando a entrada 'cidade'
    for tupla in lista_carregada: #Percorrendo a lista de tuplas
        if tupla[1].lower() == cidade and tupla[2] <= numero: #Selecionando as tuplas pelos critérios
            cidade_numero.append(tupla) #Adicionando as tuplas selecionadas
    return cidade_numero #Retornando a lista


with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(buscar_pessoa_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro'))

print(buscar_pessoa_por_numero(lista_carregada, 20))
# print(buscar_pessoa_por_numero(lista_carregada, 29.8))

print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'rio claro', 40))
# print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'Piracicaba', 90))