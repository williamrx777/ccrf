from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    mensagem = Mensagem.objects.all()
    batismo = Batismo.objects.all().order_by('-data')
    return render(request, 'home.html', {'mensagens': mensagem, 'batismos': batismo})

def culto(request):
    culto = Culto.objects.all().order_by('-data')
    return render(request, 'culto.html', {'cultos': culto})

def quem_somos(request):
    return render(request, 'quem_somos.html')

def contato(request):
    return render(request, 'contato.html')