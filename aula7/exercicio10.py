#primeira forma:
numeros = [1, 3, 5, 9, 7]
nova_lista = sorted(numeros)
print(nova_lista[0] + nova_lista[1] + nova_lista[2] + nova_lista[3])
print(nova_lista[1] + nova_lista[2] + nova_lista[3] + nova_lista[4])

#segunda forma:
print('Segunda forma')
menor = 0
for n in nova_lista[0:-1]: # sublista com os menores valores
    menor = menor + n
print(menor)
maior = 0
for n in nova_lista[1:]: # sublista com os menores valores
    maior = maior + n
print(maior)

#terceira forma
print('Terceira forma')
print(sum(numeros) - max(numeros))
print(sum(numeros) - min(numeros))

