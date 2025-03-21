'''
Código para lançamento
'''
import time

N = int(input("Digite um número: "))
'''
while N > 0:
    print(N)
    N = N - 1
print('Liberado Vôo')
'''

while N != 0:
    print(N)
    time.sleep(0.5)
    N = N - 1

print('Liberado Vôo')