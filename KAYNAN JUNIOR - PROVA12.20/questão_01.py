"""
Questão 01

• Faça a abstração da superclasse Veículo. Você deve ter pelo menos duas subclasses, nove atributos e 12 metodos.

Obs: você deve fazer o str de cada uma delas

------------------
|    Veiculos    |
------------------

"""
class Veiculo:
  def __init__(self, placa, cor, marca, quantidade_pneus, tipo_combustivel):
    self.placa = placa
    self.cor = cor
    self.marca = marca
    self.quantidade_pneus = quantidade_pneus
    self.tipo_combustivel = tipo_combustivel

  def __str__(self):
    return f'Placa: { self.placa }, Cor: { self.cor }, Marca: { self.marca }, Quantidade de Pneus: { self.quantidade_pneus }, Tipo de combustivel: { self.tipo_combustivel }'

  # GETs
  def get_placa(self):
    return self.placa
  
  def get_cor(self):
    return self.cor
  
  def get_marca(self):
    return self.marca
  
  def get_quantidade_pneus(self):
    return self.quantidade_pneus
  
  def get_tipo_combustivel(self):
    return self.tipo_combustivel
  
  # SETs
  def set_cor(self, nova_cor):
    self.cor = nova_cor


class Carro(Veiculo):
  def __init__(self, placa, cor, marca, quantidade_pneus, tipo_combustivel, quantidade_portas, tipo_direcao):
    super().__init__(placa, cor, marca, quantidade_pneus, tipo_combustivel)
    self.quantidade_portas = quantidade_portas
    self.tipo_direcao = tipo_direcao
    self.tipo_combustivel =tipo_combustivel

  def __str__(self):
    return f'Placa: { self.placa }, Cor: { self.cor }, Marca: { self.marca }, Quantidade de Pneus: { self.quantidade_pneus }, Quantidade de portas: { self.quantidade_portas }, Tipo de direção: { self.tipo_direcao }, Tipo de combustivel: { self.tipo_combustivel }'

  # GETs
  def get_quantidade_portas(self):
    return self.quantidade_portas
  
  def get_tipo_direcao(self):
    return self.tipo_direcao
  
  #SETs
  def set_tipo_direcao(self, nova_direcao):
    self.tipo_direcao = nova_direcao


class Moto(Veiculo):
  def __init__(self, placa, cor, marca, quantidade_pneus, tipo_combustivel, quantidade_cilindros, tipo_freio):
    super().__init__(placa, cor, marca, quantidade_pneus, tipo_combustivel)
    self.quantidade_cilindros = quantidade_cilindros
    self.tipo_freio = tipo_freio

  def __str__(self):
    return f'Placa: { self.placa }, Cor: { self.cor }, Marca: { self.marca }, Quantidade de pneus: { self.quantidade_pneus }, Quantidade de cilindros: { self.quantidade_cilindros }, Tipo de freio: { self.tipo_freio }, Tipo de combustivel: { self.tipo_combustivel }'

  def get_quantidade_cilindros(self):
    return self.quantidade_cilindros
  
  def get_tipo_freio(self):
     return self.tipo_freio

  def set_tipo_freio(self, novo_tipo_freio):
    self.tipo_freio = novo_tipo_freio
    

# SuperClasse Veiculo
lambo = Veiculo('HGF-7430', 'Vermelho', 'Lamborguini', 4, 'Gasolina')
print(lambo)
print()

# SubClasse Carro
s10 = Carro('GFU-1756', 'Preto', 'Chevrolet', 4,'Diesel', 2, 'Hidráulica')
print(s10)
print()

# SubClasse Moto

cb300f = Moto('VRJ-5610', 'Azul', 'Honda', 2, 'Gasolina', 300, 'ABS')
print(cb300f)