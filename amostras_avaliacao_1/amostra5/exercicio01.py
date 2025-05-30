import pickle

def menores_idade(lista_carregada):
    pessoas = [("Ana", 17), ("João", 20), ("Maria", 15), ("Pedro", 19)]
    menores = []
    for nome, idade in pessoas:
        if idade >= 18:
            menores.append((nome, idade))
    return (menores)

resultado = menores_idade()
print(resultado)

with open("exercicio01.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_menores = menores_idade(lista_carregada)
print(lista_menores)