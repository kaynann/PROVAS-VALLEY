"""
Questão 05

• Faça a abstração de superclasse Formas Geométricas.

Obs: você deve fazer o cálculo da área e do perímetro das formas
Obs: você deve fazer quantos str forem necessarios para sua abstração

----------------------------
|    FormasGeometricas    |
----------------------------

"""
class FormasGeometricas:
  def __init__(self, nome_forma_geo):
     self.nome_forma_geo = nome_forma_geo

  def __str__(self):
     return f'Forma Geométrica: { self.nome_forma_geo }'

class Quadrado(FormasGeometricas):
   def __init__(self,nome_forma_geo, base, altura):
      super().__init__(nome_forma_geo)
      self.base =  int(base)
      self.altura = int(altura)
      self.area = 0
      self.perímetro = 0

   def __str__(self):
      return f'Forma Geométrica: { self.nome_forma_geo }, Base: { self.base }, Altura: { self.altura }, Àrea: { self.area }, Perímetro: { self.perímetro }'

   def set_area(self):
      self.area = self.base * self.altura
      return self.area
   
   def set_perimetro(self):
       self.perímetro = self.base * 4
       return self.perímetro
   
class Triangulo(FormasGeometricas):
   def __init__(self, nome_forma_geo, tamanho_lado,):
      super().__init__(nome_forma_geo)
      self.tamanho_lado = int(tamanho_lado)
      self.area = 0
      self.perimetro = 0
   
   def __str__(self):
      return f'Forma Geométrica: { self.nome_forma_geo }, Tamanho dos lados: { self.tamanho_lado }, Àrea: { self.area }, Perímetro: { self.perimetro }'

   def set_area(self):
      self.area = (self.tamanho_lado * self.tamanho_lado * self.tamanho_lado) / 2
      return self.area
   
   def set_perimetro(self):
      self.perimetro = self.tamanho_lado * 3
      return self.tamanho_lado


   
q = Quadrado('Quadrado', 10, 10)
q.set_area()
q.set_perimetro()
print(q)

t = Triangulo('Triângulo', 5)
t.set_area()
t.set_perimetro()
print(t)
