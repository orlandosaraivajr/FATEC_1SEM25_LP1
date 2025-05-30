import pickle

def menores_idade(lista_carregada):

    menores = []
    for nome, idade in lista_carregada:
        if idade < 18:
            menores.append((nome, idade))
    return menores


with open("exercicio01.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_menores = menores_idade(lista_carregada)
print(lista_menores)