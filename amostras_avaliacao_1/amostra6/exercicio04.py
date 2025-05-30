import pickle


def media_nota(lista_carregada):
    result = []
    for student in lista_carregada:
        nome = student[0]
        notas = student[1:4]
        media = round(sum(notas)/3, 2)
        result.append((nome, media))
    return result

def situacao_falta(lista_carregada):
    result = []
    for student in lista_carregada:
        nome = student[0]
        faltas = student[4]
        situacao = "Reprovado" if faltas >= 6 else "Aprovado"
        result.append((nome, situacao))
    return result

def acima_de_nove(lista_carregada):
    result = []
    for student in lista_carregada:
        nome = student[0]
        notas = student[1:4]
        if all(nota >= 9 for nota in notas):
            result.append(nome)
    return result

def uma_nota_abaixo_de_seis(lista_carregada):
    result = []
    for student in lista_carregada:
        notas = student[1:4]
        if any(nota < 6 for nota in notas):
            result.append(student[:4])  # Retorna apenas (nome, nota1, nota2, nota3)
    return result


with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(media_nota(lista_carregada))
print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))
