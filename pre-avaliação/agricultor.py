import pickle

'''

Como eu criei a massa de dados

dados_climaticos = [
    (32.5, 20.1, 0), (28.7, 35.4, 1), (25.3, 45.2, 1), (38.0, 12.5, 0), (30.1, 29.7, 0),
    (21.8, 70.3, 1), (19.4, 82.5, 1), (36.2, 15.6, 0), (33.7, 22.9, 0), (29.5, 39.8, 1),
    (27.6, 50.0, 1), (24.1, 65.7, 1), (31.4, 25.3, 0), (37.8, 10.9, 0), (35.0, 18.0, 0),
    (23.6, 75.1, 1), (26.3, 59.4, 1), (22.0, 68.2, 1), (34.6, 20.4, 0), (39.1, 11.2, 0),
    (20.7, 88.5, 1), (18.9, 91.0, 1), (33.0, 27.6, 0), (28.3, 42.1, 1), (26.7, 53.0, 1),
    (21.5, 73.8, 1), (29.9, 38.5, 1), (35.7, 19.1, 0), (30.8, 32.4, 0), (25.0, 48.9, 1),
    (17.6, 95.2, 1), (16.4, 97.5, 1), (36.4, 14.0, 0), (38.6, 9.8, 0), (19.0, 89.0, 1),
    (31.2, 26.7, 0), (27.4, 46.2, 1), (23.1, 67.8, 1), (22.5, 71.4, 1), (34.3, 21.5, 0),
    (39.8, 8.7, 0), (20.3, 85.9, 1), (18.2, 93.4, 1), (32.0, 28.3, 0), (26.1, 56.7, 1),
    (24.5, 62.9, 1), (37.0, 13.3, 0), (30.5, 34.6, 0), (28.0, 41.2, 1), (22.8, 69.1, 1),
    (15.9, 98.8, 1), (16.8, 96.7, 1)
]

with open("dados_climativos_1.bin", "wb") as arquivo:
    pickle.dump(dados_climaticos, arquivo)

'''
def agro_decisor_tupla(tupla):
    # tupla = (35.0, 40.0, 0)
    T, U, P = tupla
    if P == 1:
        return 'NÃO REGAR'
    if T > 30 and U < 50:
        return 'REGAR'
    else:
        return 'NÃO REGAR'
    

def agro_decisor(tamanho_lista, lista):
    print(tamanho_lista)
    for previsao in lista:
        print(agro_decisor_tupla(previsao))


print(' ' + 'CENÁRIO 1'.center(40) + ' ' )
dados_climaticos = [(35.0, 40.0, 0), (28.0, 60.0, 1), (32.0, 45.0, 0)]
tamanho = len(dados_climaticos)
print(dados_climaticos)
agro_decisor(tamanho, dados_climaticos)

print(' ' + 'CENÁRIO 2'.center(40) + ' ' )
dados_climaticos = [(25.0, 60.0, 0), (28.0, 40.0, 1)]
print(dados_climaticos)
tamanho = len(dados_climaticos)
agro_decisor(tamanho, dados_climaticos)

'''
print(' ' + 'CENÁRIO 3'.center(40) + ' ' )
with open("dados_climativos_1.bin", "rb") as arquivo:
    dados_climaticos = pickle.load(arquivo)
print(dados_climaticos)
agro_decisor(len(dados_climaticos), dados_climaticos)
'''
