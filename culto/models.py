from django.db import models

# Create your models here.

class Culto(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
    
class Mensagem(models.Model):
    capitulo = models.CharField(max_length=255, default='')
    versiculo = models.TextField(default='')
    culto = models.ForeignKey(Culto, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

class Galeria(models.Model):
    imagem = models.ImageField(upload_to='galeria')
    culto = models.ForeignKey(Culto, on_delete=models.CASCADE)

    def __str__(self):
        return self.imagem.name
    
