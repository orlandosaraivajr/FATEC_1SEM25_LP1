import pickle
'''
nomes_unicos = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fábio", "Gabriela", "Henrique",
    "Isabela", "João", "Karla", "Lucas", "Mariana", "Nicolas", "Olívia", "Pedro",
    "Quezia", "Rafael", "Sabrina", "Tiago", "Ursula", "Vinícius", "Wesley", "Ximena",
    "Yasmin", "Zeca", "Amanda", "Bianca", "Caio", "Douglas", "Elaine", "Fernando",
    "Gustavo", "Heloísa", "Ícaro"
]
pessoas = nomes_unicos + [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fábio",
    "Gabriela", "Henrique", "Isabela", "João", "Karla", "Lucas",
    "Mariana", "Nicolas", "Olívia"
]
pessoas = sorted(pessoas)

with open("exercicio02.bin", "wb") as arquivo:
    pickle.dump(pessoas, arquivo)
'''

def remover_duplicados(lista_carregada):
    return list(set(lista_carregada))

def numero_ocorrencias(lista_carregada):
    d = {}
    for nome in lista_carregada:
        d[nome] = d.get(nome, 0) + 1
    return d

with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)