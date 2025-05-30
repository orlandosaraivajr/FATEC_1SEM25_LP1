import pickle

def media_nota(lista_carregada):
    resultado = []
    for aluno in lista_carregada:
        nome = aluno[0]
        notas = aluno[1:4]
        media = round(sum(notas) / 3, 2)
        resultado.append((nome, media))
    return resultado

def situacao_falta(lista_carregada):
    resultado = []
    for aluno in lista_carregada:
        nome = aluno[0]
        faltas = aluno[4]
        situacao = "Reprovado" if faltas >= 6 else "Aprovado"
        resultado.append((nome, situacao))
    return resultado

def acima_de_nove(lista_carregada):
    resultado = []
    for aluno in lista_carregada:
        nome = aluno[0]
        notas = aluno[1:4]
        if all(nota >= 9 for nota in notas):
            resultado.append(nome)
    return resultado

def uma_nota_abaixo_de_seis(lista_carregada):
    resultado = []
    for aluno in lista_carregada:
        notas = aluno[1:4]
        if any(nota < 6 for nota in notas):
            resultado.append(aluno[:4])  # Retorna apenas (nome, nota1, nota2, nota3)
    return resultado

with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(media_nota(lista_carregada))
print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))