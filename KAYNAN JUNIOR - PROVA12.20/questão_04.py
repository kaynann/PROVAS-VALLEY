"""
Questão 04

• Faça a abstração de superclasse Bichinho Virtual. Você deve ter os atributos: nome, energia, brinca e dorme

Regras: ao brincar o bichinho gasta energia e se a energia atingir um nivel imposto por você ele deve dormir para recarregar.

Obs: você deve ter um str mostrando o status completo do seu bichinho virtual

-------------------------
|    BichinhoVirtual    |
-------------------------

"""
class BichinhoVirtual:
  def __init__(self, nome):
    self.nome = nome
    self.energia = 100
    self.brinca = 0
    self.dorme = None

  def __str__(self):
    return f'Olá, eu sou o { self.nome }. Minha energia está em { self.energia }. Meu nivel de brincadeira está em: { self.brinca }'
  
  def brincar(self, brincar):
    if brincar > self.energia:
       print('O nivel de brincar esta maior que a energia. Insira novamente.')

    elif self.energia == 5:
       print(f'Seu bichinho virtual com a energia em: { self.energia }. Ele precisa dormir para brincar novamente.')

    else:
        self.energia -= brincar
        self.brinca += brincar
        if self.brinca < 10:
           print('Brinca mais um pouco comigo! 😟')

        elif self.brinca >= 10 and self.brinca <= 50:
           print('Estou pouco sastifeito com meu nivel de brincadeira! 🙂')
        elif self.brinca > 50:
           print('Estou super sastifeito com meu nivel de brincadeira! 😁')
        print(f'Você brincou { brincar } com seu bichinho. Ele tem { self.energia } de energia restantes')

  def dormir(self, dorme):
    if dorme == 'dormir':
       if self.energia > 0 and self.energia < 100:
         self.energia += 10
         self.brinca -= 5
         print(f'O nivel energia do seu pet aumentou em 10. A energia atual esta em { self.energia }')
       elif self.energia == 100:
          print('Seu bichinho ja está descansado.')
          if self.brinca < 10:
             print(f'Eu preciso brincar! 😓 Meu nivel de brincadeira esta em { self.brinca }')

bicho = BichinhoVirtual('Tom')
print(bicho)
bicho.dormir('dormir')
bicho.brincar(5)
bicho.brincar(40)
bicho.brincar(40)
print(bicho)
bicho.brincar(10)
bicho.brincar(4)
bicho.dormir('dormir')