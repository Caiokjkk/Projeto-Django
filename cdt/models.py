from django.db import models

class Pessoa(models.Model):
    foto = models.ImageField(upload_to='fotos')
    nome = models.CharField(max_length=250)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    rua = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome

# Create your models here.
