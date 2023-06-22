from django.db import models

# Create your models here.



class Disciplina(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)