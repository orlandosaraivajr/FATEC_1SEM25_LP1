def min_max():
    numeros2 = []  # vai receber os 5 valores, excluindo o maior
    numeros1 = []  # vai receber os 5 valores, excluindo o menor
    maior_numero = 0
    menor_numero = 0
    valor_maior = 0
    valor_menor = 0

    for i in range(5):
        numeros = int(input(f'Digite o {i+1}º número: '))
        numeros1.append(numeros)
        numeros2.append(numeros)
        for c in numeros2:
            if c > maior_numero:
                maior_numero = c
                valor_maior = i
            if c < menor_numero or menor_numero == 0:
                menor_numero = c
                valor_menor = i

    del numeros2[valor_maior]  # Exclui o maior número
    del numeros1[valor_menor]  # Exclui o menor número

    soma_maior = 0  # Maior valor possível de uma soma de 4 números
    soma_menor = 0  # Menor valor possível de uma soma de 4 números

    for adicao in range(4):
        soma_menor += numeros2[adicao]
        soma_maior += numeros1[adicao]

    return f'{soma_menor} {soma_maior}'

print(min_max())
