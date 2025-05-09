def int_to_roman(n):
    valores = [
        (1000,'M'), (900,'CM'), (500, 'D'), (400,'CD'), 
        (100,'C'), (90,'XC'), (50,'L'), (40, 'XL'), 
        (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1, 'I')
    ]
    resultado=''
    for valor, simbolo in valores:
        while n>=valor:
            resultado+=simbolo
            n-=valor
    return resultado

resultado= int(input('dugite um número: '))
print(f'{int_to_roman(resultado)}')
