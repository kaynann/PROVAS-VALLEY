"""
Questão 02

• Escreva um programa que, recebe uma palavra e uma frase, crie uma função que verifique se as letras da palavra aparecem na frase, e quantas vezes aparecem. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: você deve validar se a frase tem pelo menos 25 caracteres

Exemplos do resultado:
    palavra = "pato" 
    frase = "a capa do livro velho"
    P aparece 1 vez
    A aparece 3 vezes
    T não aparece
    O aparece três vezes
"""
def contar_letras_na_frase(palavra, frase):
    if len(palavra) < 3:
        print("A palavra deve ter pelo menos três letras.")
        return

    if len(frase) < 25:
        print("A frase deve ter pelo menos 25 caracteres.")
        return

    palavra = palavra.lower()
    frase = frase.lower()

    ocorrencias = {}
    for letra in palavra:
        ocorrencias[letra] = 0

    for letra in frase:
        if letra in ocorrencias:
            ocorrencias[letra] += 1
   
    for letra, quantidade in ocorrencias.items():
        if quantidade == 0:
            print(f"{letra.upper()} não aparece")
        else:
            print(f"{letra.upper()} aparece {quantidade} vez{'es' if quantidade > 1 else ''}")

palavra = input("Digite uma palavra: ")
frase = input("Digite uma frase (com pelo menos 25 caracteres): ")

contar_letras_na_frase(palavra, frase)