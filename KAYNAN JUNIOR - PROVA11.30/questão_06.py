"""
Questão 06

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. crie uma nova lista só com os numeros pares. -> ESCOLHIDA
02. crie uma nova lista só com os numeros impares. -> ESCOLHIDA
03. crie uma nova lista só com os multiplos de 2. -> ESCOLHIDA
04. some todos os itens da "lista" 
05. informe quais valores se repetem

"""

lista = [10,11,20,22,30,33,40,11,50,55,60,66,70,22,80,88,90,99]

# 01. Crie uma nova lista só com os numeros pares.
pares = [pairs for pairs in lista if pairs % 2 == 0]
print(F'Número pares da "lista": { pares }')
print() 

# 02. Crie uma nova lista só com os numeros ímpares.
impares = [odd for odd in lista if odd % 2 == 1]
print(f'Números impares da "lista": { impares }')
print()

# 03. Crie uma nova lista só com os multiplos de 2.
multiplo_dois = [multiplo for multiplo in lista if multiplo % 2 == 0 ]
print(f'Os múltiplos de dois são { multiplo_dois }')
print()

# 04. Some todos os itens da "lista" 
soma = sum(lista)
print(f'A soma dos itens da lista é { soma }')

# 05. Informe quais valores se repetem
valores = []
repetidos = set()
for i in lista:
  if i not in valores:
    valores.append(i)
  else:
    repetidos.add(i)
print(f'Valores repetidos { repetidos }') 