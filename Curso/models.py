from django.db import models

# Create your models here.


class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)