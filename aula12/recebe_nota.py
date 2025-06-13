from Erro import FatecError

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
except ValueError:
    print("As notas precisam ser float")
    exit()

if nota1 < 0 or nota1 > 10:
    raise FatecError("Nota 1 inválida")
 
if nota2 < 0 or nota2 > 10:
    raise FatecError("Nota 2 inválida")
    
media = (nota1 + nota2) / 2

print(media)