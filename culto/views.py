from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def culto(request):
    culto = Culto.objects.all()
    mensagem = Mensagem.objects.all()
    galeria = Galeria.objects.all()
    return render(request, 'culto.html', {'cultos': culto, 'mensagens': mensagem, 'galerias': galeria})

def quem_somos(request):
    return render(request, 'quem_somos.html')

def contato(request):
    return render(request, 'contato.html')