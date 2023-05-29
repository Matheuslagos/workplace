from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    models = Responsavel_Tecnico.objects.all()
    return render(request, 'logiq/index.html', {'models': models})
