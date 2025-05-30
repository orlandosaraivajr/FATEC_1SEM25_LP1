import pickle

def buscar_aluno_por_cidade(lista_carregada, cidade):
    cidade = cidade.lower()
    resultado = []
    for aluno in lista_carregada:
        if aluno[1].lower() == cidade:
            resultado.append(aluno)
    return resultado  

def buscar_aluno_por_numero(lista_carregada, numero):
    return [aluno for aluno in lista_carregada if aluno[2] <= numero]

def buscar_aluno_por_numero_e_cidade(lista_carregada, cidade, numero):
    cidade = cidade.lower()
    return [aluno for aluno in lista_carregada if aluno[1].lower() == cidade and aluno[2] <= numero]

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(buscar_aluno_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_aluno_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_aluno_por_cidade(lista_carregada, 'Rio Claro'))

print(buscar_aluno_por_numero(lista_carregada, 20))
# print(buscar_aluno_por_numero(lista_carregada, 29.8))

print(buscar_aluno_por_numero_e_cidade(lista_carregada, 'rio claro', 40))