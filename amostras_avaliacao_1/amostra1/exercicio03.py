import pickle

def buscar_pessoa_por_cidade(lista_carregada, cidade):
    
    cidade_corrigida = cidade.lower()
    resultado = []
    for nome, cidade_lista, valor in lista_carregada:
        if cidade_lista.lower() == cidade_corrigida:
            resultado.append((nome, cidade_lista, valor))
    return resultado


def buscar_pessoa_por_numero(lista_carregada, numero):
     
    resultado = []
    for nome, cidade_lista, valor in lista_carregada:
        if valor <= numero:
            resultado.append((nome, cidade_lista, valor))
    return resultado

def buscar_pessoa_por_numero_e_cidade(lista_carregada, cidade, numero):

    cidade_corrigida = cidade.lower()
    resultado = []
    for nome, cidade_lista, valor in lista_carregada:
        if cidade_lista.lower() == cidade_corrigida and valor <= numero:
            resultado.append((nome, cidade_lista, valor))
    return resultado

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(buscar_pessoa_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro'))

print(buscar_pessoa_por_numero(lista_carregada, 20))
# print(buscar_pessoa_por_numero(lista_carregada, 29.8))

print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'rio claro', 40))
