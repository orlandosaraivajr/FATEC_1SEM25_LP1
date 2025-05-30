import pickle

def remover_duplicados(lista_carregada):
    lista_sem_duplicacao = []
    for pessoa in lista_carregada:
        if pessoa not in lista_sem_duplicacao:
            lista_sem_duplicacao.append(pessoa)
    return lista_sem_duplicacao

def numero_ocorrencias(lista_carregada):
    ocorrencia = {}
    for pessoa in lista_carregada:
        ocorrencia [pessoa] = ocorrencia.get(pessoa,0) + 1
    return ocorrencia

with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)