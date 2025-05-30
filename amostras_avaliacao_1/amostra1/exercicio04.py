import pickle


def media_nota(lista_carregada):
    
    medias = []
    for nome, nota1, nota2, nota3, faltas in lista_carregada:
        media = ((nota1 + nota2 + nota3) / 3)
        media_formatada = f"{media:.2f}"
        medias.append((nome, media_formatada))
    return medias

def situacao_falta(lista_carregada):
    
    situacoes = []
    for nome, nota1, nota2, nota3, faltas in lista_carregada:
        if faltas >= 6:
            situacao = "Reprovado"
        else:
            situacao = "Aprovado"
        situacoes.append((nome, situacao))
    return situacoes

def acima_de_nove(lista_carregada):

    nerds = []
    for nome, nota1, nota2, nota3, faltas in lista_carregada:
        if nota1 >= 9 and nota2 >= 9 and nota3 >= 9:
            nerds.append(nome)
    return nerds

def uma_nota_abaixo_de_seis(lista_carregada):
    
    menos_q_seis = []
    for nome, nota1, nota2, nota3, faltas in lista_carregada:
        if nota1 < 6 or nota2 < 6 or nota3 < 6:
            menos_q_seis.append((nome, nota1, nota2, nota3))
    return menos_q_seis


with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(media_nota(lista_carregada))
print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))
