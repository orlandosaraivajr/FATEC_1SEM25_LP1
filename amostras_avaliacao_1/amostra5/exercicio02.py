import pickle

def remover_duplicados(lista_carregada):
    nova_lista = set(lista_carregada)
    lista_sem_duplicacao = list(nova_lista)
    return lista_sem_duplicacao                        

def numero_ocorrencias(lista_carregada):
    dicionario = {}
    for palavra in lista_carregada:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)