import pickle


def media_nota(lista_carregada):
    soma = 0
    for pessoa in lista_carregada:
        soma += pessoa[1]
    return soma / len(lista_carregada)

def situacao_falta(lista_carregada):
    lista_situacao = []
    for pessoa in lista_carregada:
        if pessoa[1] >= 7 and pessoa[1] <= 20:
            lista_situacao.append(pessoa)
    return lista_situacao
    
def acima_de_nove(lista_carregada):
    lista_acima = []
    for pessoa in lista_carregada:
        if pessoa[1] > 9:
            lista_acima.append(pessoa)
    return lista_acima    

def uma_nota_abaixo_de_seis(lista_carregada):
    lista_abaixo = []
    for pessoa in lista_carregada:
        if pessoa[1] < 6 and pessoa[1] < 10:
            lista_abaixo.append(pessoa)
    return lista_abaixo
    
with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(media_nota(lista_carregada))
print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))
