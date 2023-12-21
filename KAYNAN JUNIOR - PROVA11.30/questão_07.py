"""
Questão 07

• Crie uma função que gere uma lista com tuplas em seus elementos, nas tuplas devem conter dois valores nome e idade 

Ex.: [('paulo', 28), ('Jose', 23), ('Roberto', 17)] 

Ainda deve fazer:
• excluir o ultimo valor
• adicionar uma nova tupla no inicio da lista
• Crie uma cópia da lista para não utilizar o mesmo endereço de memoria

"""
# 01. Crie uma função que gere uma lista com tuplas em seus elementos, nas tuplas devem conter dois valores nome e idade  
def nome_idade():
  lista = []
  num_users = int(input('Informe quantas pessoas serão adicionadas: '))

  for i in range(num_users):
    user_name = input(f'Digite o { i + 1 }º nome: ')
    user_year = input(f'Digite a { i + 1 }º idade: ')

    lista.append((user_name, user_year))
  return lista

lista_dados = nome_idade()
print(lista_dados)
print()

# 02. Excluir ultimo valor
lista_dados.pop()
print(lista_dados)
print()

# 03. Adicionar uma niva tupla no inicio da lista
new_tuple = ('Maria', 15)
lista_dados.insert(0, new_tuple)
print(lista_dados)
print()

# 04. Crie uma cópia da lista para não utilizar o mesmo endereço de memória
lista_copy = lista_dados.copy()
print(f'Cópia da lista com novo endereço de memória\n{lista_copy}')