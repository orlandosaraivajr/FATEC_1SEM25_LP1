'''
Exemplo de if aninhado

Com ajustes do Cesar
0 - 200 para 0.20
201 - 400 para 0.18
401 - ..  0.15

Exemplos:
150 => (150 * 0.2)
300 =>  (200 * 0.2) + (100 * 0.18)
1000 =>  (200 * 0.2) + (200 * 0.18) + (600 * 0.15)
'''
minutos = int(input("Digite os minutos no mês: "))
total = 0

if minutos < 200:
    preco = 0.20
    total = minutos * preco
else:
    if minutos <400:
        minutos = minutos - 200
        preco = 0.18
        total = (200 * 0.2) + (minutos * preco)
    else:
        minutos = minutos - 400
        preco = 0.15
        total = (200 * 0.2) + (200 * 0.18) + (minutos * preco)
        

print("Preço por minuto: " + str(preco))
print("Total: " + str(total))