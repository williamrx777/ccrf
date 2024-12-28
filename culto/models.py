from django.db import models

# Create your models here.

class Culto(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='galeria', default='')
    def __str__(self):
        return self.nome
    
class Mensagem(models.Model):
    capitulo = models.CharField(max_length=255, default='')
    versiculo = models.TextField(default='')

    def __str__(self):
        return self.capitulo

class Batismo(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='batismo', default='')

    def __str__(self):
        return self.nome
    
