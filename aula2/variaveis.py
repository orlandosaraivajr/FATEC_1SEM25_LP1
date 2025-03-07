'''
Neste código, teremos exemplos de como criar variáveis
e alterar seus valores

'''

# variavel1 recebe um valor numérico inteiro(int). O valor é 10
variavel1 = 10
# variavel2 recebe um valor numérico ponto flutuante(float). O valor é 8.5
variavel2 = 8.5
# variavel3 recebe um valor textual(string). O valor é Fatec Rio Claro
variavel3 = 'Fatec Rio Claro'
# nome_faculdade também recebe um valor textual(string).
nome_faculdade = "Fatec Rio Claro"

print(variavel1)
print(variavel2)
print(variavel3)
print(nome_faculdade)

numero1 = 14
numero2 = 5
numero3 = 7
numero4 = 3
print(numero1 - numero2 + numero3 % numero4)

'''
Comando para receber valores do usuário.
'''
nome = input("Digite seu nome: ")
idade = input('Digite sua idade: ')
# type(idade) retorna string. Precisamos converver
idade = int(idade)
peso = input('Digite seu peso: ')
peso = float(peso)
# Tudo em um único comando:
idade = int(input('Digite sua idade'))

