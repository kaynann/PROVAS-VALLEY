"""
Questão 08

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. peça três frutas para o usuario e calcule o total da compra dele
02. informe o qual fruta tem o menor valor
03. faça uma promoção e diminua o preco de duas frutas para metade
04. insira duas novas frutas e seus preços

"""

frutas = ["abacaxi", "uva", "maçã", "abacate", "tangerina"]
precos = [3.50, 4.99, 6.49, 9.10, 4.99]

# 01. Peça três frutas para o usuário e calcule o total da compra
compra_usuario = 0
for i in range(3):
    print(f'Frutas da feira: { frutas }')
    fruta = input(f'Digite o nome da { i + 1 }ª fruta: ')
    print()
    if fruta.lower() in frutas:
        indice = frutas.index(fruta.lower())
        compra_usuario += precos[indice]
    else:
        print(f'Fruta { fruta } não encontrada. Verifique o nome.')

print(f'O total da compra é: R${compra_usuario:.2f}')

# 02. Informe qual fruta tem o menor valor
menor_valor_indice = precos.index(min(precos))
fruta_menor_valor = frutas[menor_valor_indice]
print(f'A fruta com menor valor é { fruta_menor_valor }.')
print()

# 03. Faça uma promoção e diminua o preço de duas frutas para metade
nova_lista = dict(zip(frutas, precos))
nova_lista['uva'] = nova_lista['uva'] / 2
nova_lista['abacate'] = nova_lista['abacate'] / 2

print('!!! PROMOÇÃO !!!')
for f, p in nova_lista.items():
    print(f'{ f.capitalize() }: R$ {p:.2f}')

# 04. Insira duas novas frutas e seus preços
novas_frutas = [['melancia', 4], ['pitaya', 10]]
nova_lista.update(novas_frutas)

print("\nFrutas e preços atualizados:")
for fruta, preco in nova_lista.items():
    print(f'{ fruta.capitalize() }: R$ {preco:.2f}')