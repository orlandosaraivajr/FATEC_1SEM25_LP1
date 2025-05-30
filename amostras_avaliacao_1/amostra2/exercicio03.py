import pickle
'''
pessoas = [
    ("Ana", "Araras", 87.5),
    ("Bruno", "Rio Claro", 42.3),
    ("Carla", "Piracicaba", 76.8),
    ("Daniel", "Santa Gertrudes", 55.1),
    ("Eduarda", "Araras", 92.4),
    ("Fábio", "Rio Claro", 66.6),
    ("Gabriela", "Piracicaba", 81.2),
    ("Henrique", "Santa Gertrudes", 23.9),
    ("Isabela", "Araras", 49.5),
    ("João", "Rio Claro", 35.6),
    ("Karla", "Piracicaba", 90.0),
    ("Lucas", "Santa Gertrudes", 74.4),
    ("Mariana", "Araras", 63.3),
    ("Nicolas", "Rio Claro", 58.7),
    ("Olívia", "Piracicaba", 45.1),
    ("Pedro", "Santa Gertrudes", 38.2),
    ("Quezia", "Araras", 84.6),
    ("Rafael", "Rio Claro", 29.8),
    ("Sabrina", "Piracicaba", 99.9),
    ("Tiago", "Santa Gertrudes", 12.5),
    ("Ursula", "Araras", 71.3),
    ("Vinícius", "Rio Claro", 61.0),
    ("Wesley", "Piracicaba", 36.9),
    ("Ximena", "Santa Gertrudes", 80.2),
    ("Yasmin", "Araras", 93.3),
    ("Zeca", "Rio Claro", 40.7),
    ("Amanda", "Piracicaba", 88.8),
    ("Bianca", "Santa Gertrudes", 54.2),
    ("Caio", "Araras", 27.1),
    ("Douglas", "Rio Claro", 73.0)
]

# Salvar no arquivo
with open("exercicio03.bin", "wb") as arquivo:
    pickle.dump(pessoas, arquivo)

'''

def buscar_pessoa_por_cidade(lista_carregada, cidade):
    cidade = cidade.lower()
    encontrados = []
    for pessoa in lista_carregada:
        if pessoa[1].lower() == cidade:
            encontrados.append(pessoa)
    return encontrados

def buscar_pessoa_por_numero(lista_carregada, numero):
    encontrados = []
    for pessoa in lista_carregada:
        if pessoa[2] <= numero:
            encontrados.append(pessoa)
    return encontrados

def buscar_pessoa_por_numero_e_cidade(lista_carregada, cidade, numero):
    encontrados = []
    encontrados = buscar_pessoa_por_numero(lista_carregada, numero)
    encontrados = buscar_pessoa_por_cidade(encontrados, cidade)
    return encontrados

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro'))

# print(buscar_pessoa_por_numero(lista_carregada, 20))
# print(buscar_pessoa_por_numero(lista_carregada, 29.8))

# print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'rio claro', 40))
