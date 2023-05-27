from django.db import models

# Create your models here.


class respons_tec(models.Model):
    nome = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=200)
    Num_Registro = models.CharField(max_length=200)
