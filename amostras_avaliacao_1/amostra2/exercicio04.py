import pickle
'''
alunos = [
    ("Ana", 8.5, 7.2, 6.8, 2),
    ("Bruno", 6.0, 5.5, 7.0, 4),
    ("Carlos", 9.0, 8.5, 9.3, 1),
    ("Daniela", 4.5, 6.0, 5.8, 6),
    ("Eduardo", 7.5, 8.0, 7.2, 3),
    ("Fernanda", 6.3, 7.1, 6.9, 2),
    ("Gustavo", 5.5, 6.2, 7.4, 4),
    ("Helena", 9.2, 8.7, 9.0, 0),
    ("Igor", 3.5, 4.2, 5.0, 7),
    ("Juliana", 6.8, 7.0, 7.1, 3),
    ("Karina", 7.3, 6.5, 7.7, 2),
    ("Lucas", 8.1, 7.9, 8.4, 1),
    ("Marcos", 5.8, 5.9, 6.0, 5),
    ("Natália", 9.0, 9.1, 8.9, 0),
    ("Otávio", 6.5, 6.2, 6.8, 4),
    ("Patrícia", 4.0, 5.5, 6.0, 8),
    ("Quésia", 8.7, 8.5, 9.0, 1),
    ("Rafael", 7.0, 6.5, 7.2, 3),
    ("Sabrina", 6.3, 7.4, 7.0, 2),
    ("Thiago", 5.5, 5.8, 6.2, 5),
    ("Ursula", 9.1, 9.3, 8.8, 0),
    ("Vitor", 6.2, 6.0, 6.5, 4),
    ("Wesley", 7.8, 7.4, 7.9, 2),
    ("Xênia", 4.9, 5.2, 6.1, 6),
    ("Yasmin", 8.3, 8.6, 8.9, 1),
    ("Zeca", 6.0, 6.3, 6.7, 3),
    ("Alan", 5.1, 5.5, 5.8, 5),
    ("Bianca", 9.2, 9.0, 9.4, 0),
    ("Caio", 7.4, 7.2, 7.1, 3),
    ("Diana", 6.6, 6.9, 7.3, 2),
    ("Elias", 4.3, 4.5, 5.0, 7),
    ("Fabiana", 7.9, 8.0, 7.6, 2),
    ("Gilberto", 6.5, 5.9, 6.3, 4),
    ("Heloísa", 8.6, 8.2, 8.9, 1),
    ("Irene", 5.3, 5.0, 5.7, 6),
    ("João", 7.2, 7.5, 7.9, 2),
    ("Kelly", 9.3, 9.1, 9.0, 0),
    ("Leandro", 6.0, 6.2, 6.1, 5),
    ("Milena", 5.6, 5.4, 5.8, 5),
    ("Neto", 7.5, 7.2, 7.6, 3),
    ("Olívia", 8.4, 8.3, 8.5, 1),
    ("Paulo", 4.8, 5.1, 5.5, 6),
    ("Quitéria", 6.9, 7.0, 6.8, 3),
    ("Renato", 5.0, 5.2, 5.3, 7),
    ("Samara", 8.2, 8.1, 8.4, 1),
    ("Tales", 7.0, 6.8, 7.3, 3),
    ("Ubirajara", 6.3, 6.0, 6.7, 4),
    ("Valéria", 9.0, 9.2, 9.1, 0),
    ("Wellington", 6.6, 6.4, 6.9, 3),
    ("Yuri", 5.2, 5.1, 5.4, 6),
    ("Zuleide", 7.7, 7.9, 7.8, 2),
]


# Salvar no arquivo
with open("exercicio04.bin", "wb") as arquivo:
    pickle.dump(alunos, arquivo)
'''

def media_nota(lista_carregada):
    lista = []
    for aluno in lista_carregada:
        media = round((aluno[1] + aluno[2] + aluno[3]) / 3 , 2)
        registro = (aluno[0], media)
        lista.append(registro)
    return lista

def situacao_falta(lista_carregada):
    lista = []
    for aluno in lista_carregada:
        if aluno[4] >= 6:
            registro = (aluno[0], 'Reprovado')
        else:
            registro = (aluno[0], 'Aprovado')
        lista.append(registro)
    return lista

def acima_de_nove(lista_carregada):
    nota_referencia = 9
    lista = []
    for aluno in lista_carregada:
        if aluno[1] >= nota_referencia and aluno[2] >= nota_referencia and aluno[3] >= nota_referencia:
            lista.append(aluno[0])
    return lista

def uma_nota_abaixo_de_seis(lista_carregada):
    nota_referencia = 6
    lista = []
    for aluno in lista_carregada:
        if aluno[1] < nota_referencia or aluno[2] < nota_referencia or aluno[3] < nota_referencia:
            registro = ((aluno[0], aluno[1], aluno[2], aluno[3]))
            lista.append(registro)
    return lista


with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

# print(lista_carregada)
# print(media_nota(lista_carregada))
# print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))
