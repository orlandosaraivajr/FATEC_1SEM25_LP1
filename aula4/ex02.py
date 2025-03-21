t = int(input("Digite um valor: "))

for i in range(1, 11):
    print(f'{t} x {i} = {t * i}')
    
print("Segunda Tabuada")
i = 1
while i <= 10:
    print(f'{t} x {i} = {t * i}')
    i += 1

print('Terceira Tabuada')
x = 1
while True:
    if x == 11:
        break
    else:
        print(f'{t} x {x} = {t * x}')
        x += 1
        