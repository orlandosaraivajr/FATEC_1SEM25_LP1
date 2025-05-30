import pickle

def buscar_pessoa_por_cidade(lista_carregada, cidade):
    result = []
    for citizen in lista_carregada:
        city_citizen = citizen[1]
        if city_citizen.lower() == cidade.lower():
            result.append(citizen)
    return result


def buscar_pessoa_por_numero(lista_carregada, numero):
    return [citizen for citizen in lista_carregada if citizen[2] <= numero]

def buscar_pessoa_por_numero_e_cidade(lista_carregada, cidade, numero):
    city = cidade.lower()
    return [citizen for citizen in lista_carregada if citizen[1].lower() == city and citizen[2] <= numero]

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(buscar_pessoa_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro'))

print(buscar_pessoa_por_numero(lista_carregada, 20))
# print(buscar_pessoa_por_numero(lista_carregada, 29.8))

print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'rio claro', 40))
