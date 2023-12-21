"""
Questão 04

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. crie uma função que faça a troca de caracteres de acordo com a escolha do usuario. Imprima em uma nova string.
02. utilizando um FOR troque os espaços em branco por -.

"""
texto = "Neste curso, os alunos(as) terão capacidades para trabalharem com toda a estrutura de dados que roda por trás de aplicações web. Compreendendo as necessidades de geração, captura e armazenamento de dados de uma aplicação web e a desenvolve, levando sempre em considerutilizando um FOR troque os espaços em branco por -.ação a agilidade, segurança e confiabilidade nos dados que serão gerados e, por vezes, integrados a outros sistemas de gestão estratégica.".lower()

# 01. Crie uma função que faça a troca de caracteres de acordo com a escolha do usuario. Imprima em uma nova string.
def troca_caracteres(caracter, new_caracter):
  new_texto = texto.replace(caracter, new_caracter)
  return new_texto 
 
caracter = input('Digite os caracteres para trocar: ').lower()
new_caracter = input('Digite os novos caracteres que você deseja adicionar: ').lower()

new_texto = troca_caracteres(caracter, new_caracter)
print(new_texto.capitalize())
print()

# 02. Utilizando um FOR troque os espaços em branco por -.
novo_texto = ""
for i in new_texto:
  if i == ' ':
    novo_texto += '-'
  else:
    novo_texto += i
print(novo_texto.capitalize())