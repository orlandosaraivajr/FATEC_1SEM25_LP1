import pickle

def remover_duplicados(lista_carregada):
    
    return list(set(lista_carregada))

def numero_ocorrencias(lista_carregada):
    
    ocorrencias = {}
    for nome in lista_carregada:
        if nome in ocorrencias:
            ocorrencias[nome] += 1
        else:
            ocorrencias[nome] = 1
    return ocorrencias

with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)