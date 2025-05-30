import pickle

def remover_duplicados(lista_carregada):
    lista_sem_duplicatas = list(set(lista_carregada))
    return lista_sem_duplicatas

def numero_ocorrencias(lista_carregada):
    ocorrencia = {}
    for word in lista_carregada:
        if word in ocorrencia:
            ocorrencia[word] += 1
        else:
            ocorrencia[word] = 1
    return ocorrencia

with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)