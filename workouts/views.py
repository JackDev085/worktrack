from django.shortcuts import render
from .models import Exercicio

def index(request):
  return render(request, "index.html")


def pesquisa(request):
  url_paramns= request.GET.get("search") 
  exercicios = Exercicio.objects.filter(name__icontains=url_paramns)
  return render(request, "ver_exercicios.html", {"exercicios": exercicios, "search":url_paramns})

def exercicio(request, id):
  exercicio = Exercicio.objects.get(pk=id)
  musculos = exercicio.musculo.all()
  return render(request, "ver_exercicio.html", {"exercicio": exercicio, "musculos": musculos})