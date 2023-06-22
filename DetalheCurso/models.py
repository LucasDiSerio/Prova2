from django.db import models

# Create your models here.


class DetalheCurso(models.Model):
    curso = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)