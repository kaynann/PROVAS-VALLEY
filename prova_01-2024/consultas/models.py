from django.db import models

class Consulta(models.Model):
  nome_paciente = models.CharField(max_length=120)
  idade = models.IntegerField()
  peso = models.FloatField()
  motivo_consulta = models.TextField()
  dia_consulta = models.DateField()
  hora = models.TimeField()
  data_cad = models.DateTimeField(auto_now_add=True)
  foto_paciente = models.ImageField(upload_to='pacientes')