"""
Questão 03

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. imprima quantas vezes aparece a letra "a" no "texto". -> ESCOLHIDA
02. imprima qual a posição do primeiro "z". 
03. leve o "texto" para uma nova variavel e trocando "aprendizado compartilhado" por "vivencia profissional". -> ESCOLHIDA

"""
texto = "Somos uma escola de tecnologia de informação que cria pontes entre pessoas, conhecimento e empresas. Ambiente que proporciona conexão, troca de conhecimentos e aprendizado compartilhado entre participantes, instrutores e empresas parceiras."

# REQUISIÇÃO 01:
print(f'A letra "a" aparece { texto.count("a") } vezes no texto\n')
print()

# REQUISIÇÃO 02:
print(f'O primeiro "z" está na posição { texto.find("z") }')
print()

# REQUISIÇÃO 03:
novo_texto = texto.replace("aprendizado compartilhado", "vivencia profissional")
print(novo_texto)