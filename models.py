from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    pontuacao = models.IntegerField(blank=True, null=True)
    habilitacao = models.BooleanField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
        
class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)    
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

