# Recebendo como string
nota = input(' Digite a nota do aluno entre 0 a 100: ')
# Substituir , por .
nota = nota.replace(',','.')
# Converter string em float
nota = float(nota)

if nota >= 90:
  print(' Aprovado com excelência ')
elif nota >=70:
  print('Aprovado ')
elif nota >= 50:
  print( 'Recuperação' )
else:
  print('Reprovado')
 