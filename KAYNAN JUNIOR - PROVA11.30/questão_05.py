"""
Questão 05

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. monte um conjunto(SET) com o nome "meu_conjunto1", nele você deve colocar os indices impares da "minha_lista"
02. transforme a "minha_lista" em uma string separada por /
03. monte uma lista inversa da "minha_lista"
04. informe quantos elementos estão contidos em "minha_lista" e quantos estão contidos em "meu_conjunto"

"""

minha_lista = ["com", "um", "notebook", "e", "internet", "de", "banda", "larga", "qualquer", "jovem", "capacitado", "poderá", "trabalhar", "ou", "empreender", "do", "Ceará", "para", "o", "Brasil", "e", "o", "mundo", "e", "consequentemente", "transformando", "a", "sua", "vida", "e", "aquecendo", "a", "economia", "local"]

# REQUISIÇÃO 01:
meu_conjunto1 = set(minha_lista[1::2])
print(f'{ meu_conjunto1 }\n')

# REQUISIÇÃO 02:
conjunto_str = '/'.join(minha_lista)
print(f'{ conjunto_str }')

# REQUISIÇÃO 03:
lista_inverse = minha_lista[::-1]
print(f'\n{ lista_inverse }')

# REQUISIÇÃO 04:
print(f'\nNa variável "minha_lista" tem { len(minha_lista) } elementos')
print(f'Na variável "meu_conjunto1" tem { len(meu_conjunto1) } elementos')