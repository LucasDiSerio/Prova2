from django.db import models

# Create your models here.


class Professor(models.Model):
    sexo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)