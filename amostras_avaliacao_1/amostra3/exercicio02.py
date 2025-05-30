import pickle


def remover_duplicados(lista_carregada):
    unicos = list(set(lista_carregada)) #Transformando em conjunto e transformando de volta em lista
    return unicos #Retornando a lista

def numero_ocorrencias(lista_carregada):
    dicionario = {} #Saída: dicionário. Criando dicionário
    for nome in lista_carregada: #Percorrendo a lista de nomes
        dicionario[nome] = dicionario.get(nome, 0) + 1 #Para cada nome, acrescenta 1 vez
    return dicionario


with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)