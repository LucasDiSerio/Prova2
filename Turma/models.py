from django.db import models

# Create your models here.


class Turma(models.Model):
    codigo = models.CharField(max_length=100)
    codigoTurma = models.CharField(max_length=100)