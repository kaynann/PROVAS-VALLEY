"""
Questão 02

• Faça a abstração da superclasse Extintor de Incendio.

Obs: você deve fazer o str dela mostrando o nivel da carga do extintor

---------------------------
|    ExtintorDeIncendio   |
---------------------------

"""
class ExtintorDeIncendio:
  def __init__(self):
    self.nivel_carga = 100

  def __str__(self):
    return f'O nivel de carga do extintor esta em { self.nivel_carga }'

  # COMUNS
  def usar_extintor(self, quantidade_uso):
    if self.nivel_carga == 0:
      print('O nivel da carga está em 0. Por favor recarregue o nivel de carga do extintor.')

    else:
      if self.nivel_carga > 0:
        self.nivel_carga -= quantidade_uso
        print(f'Você usou { quantidade_uso } de carga do extintor. A quantidade de carga restante do extintor é: { self.nivel_carga }')
  
  def recarregar_extintor(self, nova_recarga):
      if nova_recarga <= 0:
        print('Valor de recarga inválido')

      carga = self.nivel_carga + nova_recarga
      if carga >= 100:
        print('O extintor ja está cheio')
      else: 
        if carga < 100:
         self.nivel_carga += nova_recarga
         print(f'Você recarregou { nova_recarga } de carga. Carga atual: { self.nivel_carga }')

      

extintor = ExtintorDeIncendio()
print(extintor)
extintor.usar_extintor(70)
extintor.recarregar_extintor(3)
print(extintor)