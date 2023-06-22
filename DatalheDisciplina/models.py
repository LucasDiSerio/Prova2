from django.db import models

# Create your models here.


class DatalheDisciplina(models.Model):
    curso = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)