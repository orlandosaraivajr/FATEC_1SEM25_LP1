import pickle

def buscar_pessoa_por_cidade(lista_carregada, cidade):
    lista_cidade = []
    for pessoa in lista_carregada:
        if pessoa[2] == cidade:
            lista_cidade.append(pessoa)
    return lista_cidade    

def buscar_pessoa_por_numero(lista_carregada, numero):
    lista_numero = []
    for pessoa in lista_carregada:
        if pessoa[1] == numero:
            lista_numero.append(pessoa)
    return lista_numero    

def buscar_pessoa_por_numero_e_cidade(lista_carregada, cidade, numero):
    lista_numero_cidade = []
    for pessoa in lista_carregada:
        if pessoa[2] == cidade and pessoa[3] == numero:
            lista_numero_cidade.append(pessoa)
    return lista_numero_cidade       

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(buscar_pessoa_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro'))

print(buscar_pessoa_por_numero(lista_carregada, 29.8))
# print(buscar_pessoa_por_numero(lista_carregada, 29.8))

print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'rio claro', 40))
