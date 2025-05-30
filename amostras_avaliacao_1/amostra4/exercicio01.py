import pickle

def menores_idade(lista_carregada):
    lista_menores = []
    for pessoa in lista_carregada:
        if pessoa[1] < 18:
            lista_menores.append(pessoa)
    return lista_menores

with open("exercicio01.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_menores = menores_idade(lista_carregada)
print(lista_menores)
