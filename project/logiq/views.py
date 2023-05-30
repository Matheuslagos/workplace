from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'logiq/index.html', {'responsaveis': responsaveis, 'produtores': produtores, 'diagnosticos': diagnosticos, 'propriedades': propriedades})


def documento(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'logiq/documento.html', {'responsaveis': responsaveis, 'produtores': produtores, 'diagnosticos': diagnosticos, 'propriedades': propriedades})


def documentoCompleto(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'logiq/documentoCompleto.html', {'responsaveis': responsaveis, 'produtores': produtores, 'diagnosticos': diagnosticos, 'propriedades': propriedades})
