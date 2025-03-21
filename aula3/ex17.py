'''
Exercício 17: Simulação de saque bancário
• O usuário informa o valor do saque.
• O programa deve calcular quantas notas de R$ 100, R$ 50, R$ 20 e R$ 10 serão entregues,
sempre com o menor número possível de cédulas.

300 = (3x100)
170 = (1x100) + (1x50) + (1x20)
90 = (1x50) + (2x20)
80 = (1x50) + (1x20) + (1x10)
'''

valor = int(input('Digite o valor do saque: '))

notas_cem = int(valor / 100)
valor %= 100
notas_cinquenta = int(valor / 50)
valor = valor % 50
notas_vinte = int(valor / 20)
valor = valor % 20
notas_dez = int(valor / 10)
valor %= 10

print('Notas de R$ 100: ' + str(notas_cem))
print('Notas de R$ 50: ' + str(notas_cinquenta))
print('Notas de R$ 20: ' + str(notas_vinte))
print('Notas de R$ 10: ' + str(notas_dez))

