"""
Questão 10

• Escreva uma função que calcule o fatorial de um numero e lembre de imprimir todos os resultados:

01. o numero  deve ser solicitado ao usuario

"""
def calcula(number):
  resultado = 1
  for i in range(1, number +1):
    resultado = resultado * i
  return (resultado)
  #  print(f'O fatorial de { i } é { resultado }')

user_number = int(input('Digite um número: '))
print(calcula(user_number))