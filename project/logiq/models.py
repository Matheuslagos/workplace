from django.db import models

# Create your models here.


class respons_tec(models.Model):
    nome = models.CharField(max_length=200)
    CNPJ = models.PositiveIntegerField()
    Num_Registro = models.PositiveIntegerField()


class Propriedade(models.Model):
    descricao = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    local = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class ProdutorRural(models.Model):
    nome = models.CharField(max_length=200)
    propriedade = models.ForeignKey('Propriedade', on_delete=models.CASCADE)


class Diagnostico(models.Model):
    cultura = models.CharField(max_length=100)
    produto_comercial = models.CharField(max_length=100)
    alvo = models.CharField(max_length=100)
    area_a_tratar = models.FloatField()
    volume_da_calda = models.FloatField()
    intervalo_de_seguranca = models.IntegerField()
    modalidade_aplicacao = models.CharField(max_length=100)
    equipamento_aplicacao = models.CharField(max_length=100)
    quantidade_a_adquirir = models.IntegerField()
    n_aplicacoes = models.IntegerField()
    epoca_aplicacao = models.DateField()


class PrecaucaoUso(models.Model):
    texto = models.TextField()


class equipamentos_epi():
    texto_equip = models.TextField()


class orientacoes_mip():
    texto_mip = models.TextField()


class local_devolucao():
    texto_dev = models.CharField(max_length=150)


class Precaucao_orientacoes(models.Model):
    texto = models.TextField()
