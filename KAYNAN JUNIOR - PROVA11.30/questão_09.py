"""
Questão 08

• Escreva uma função que calcule o tempo de viagem de uma pessoa lembre de imprimir todos os resultados:

01. peça a distancia e a velocidade media
02. a formula é: distância / velocidade média(hora)
03. não esqueça de limitar a resposta em apenas duas casas decimais 

"""

def time_viagem():
  distancia = float(input('Informe a distância percorrida em km: ' ))
  velocidade_media = float(input('Informe a velocidade média em km/h: '))

  tempo_viagem = distancia / velocidade_media

  print(f'O tempo de viagem foi de {tempo_viagem:.2f} horas')

time_viagem()  