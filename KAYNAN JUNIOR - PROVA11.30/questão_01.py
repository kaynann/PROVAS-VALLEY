"""
Questão 01

• Escreva um programa que, recebe uma palavra, crie uma função que verifica na lista "alfabeto" a que indice pertence cada letra da palavra. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: letras repetidas devem ser verificadas somente uma vez

Exemplos do resultado:
    palavra = "cidade" 
    C está no indice 2
    I está no indice 8
    D está no indice 3
    A está no indice 0
    E está no indice 4
"""

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

def verify(palavra, alfabeto):

    if len(palavra) < 3:
        print('A palavra deve conter três ou mais caracteres')
         
    palavra = palavra.lower()
    letras_unicas = set()

    for i in palavra:
        if i in letras_unicas:
                continue
        letras_unicas.add(i)
            
        if i in alfabeto:
            indice_letra = alfabeto.index(i)
            print(f'{ i.upper() } está no indice { indice_letra }')

user_word = input('Digite uma palavra: ')
verify(user_word, alfabeto)
        

