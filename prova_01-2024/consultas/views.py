from django.shortcuts import render, redirect
from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages

def index(request):
  consultas = Consulta.objects.all()
  return render(request, 'consultas/index.html', {'consultas': consultas})

def register(request):
  if request.method == 'POST':
    form = ConsultaForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'Consulta cadastrada')
      form = ConsultaForm()
    else:
      messages.error(request, 'Erro ao cadastrar consulta')
  else:
    form = ConsultaForm()
  return render(request, 'consultas/register.html', {'form': form})

def delete(request, id):
  consulta = Consulta.objects.get(id=id)
  if request.method == 'POST':
    consulta.delete()
    return redirect('/')
  return render(request, 'consultas/delete.html')