'''
Exemplo de if aninhado
'''
minutos = int(input("Digite os minutos no mês: "))

if minutos < 200:
    preco = 0.20
else:
    if minutos <400:
        preco = 0.18
    else:
        preco = 0.15

print("Preço por minuto: " + str(preco))
total = preco * minutos
print("Total: " + str(total))