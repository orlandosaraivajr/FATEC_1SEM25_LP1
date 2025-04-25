lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Primeira resolução

lista3 = []
for item in lista1:
    if not item in lista3:
        lista3.append(item)

for item in lista2:
    if not item in lista3:
        lista3.append(item)

print(lista3)

# Segunda resolução

lista4 = list(set(lista1 + lista2))
print(lista4)