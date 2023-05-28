from django.db import models

# Create your models here.


class Responsavel_Tecnico(models.Model):
    nome = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=14)
    Num_Registro = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Responsaveis Tecnicos'

    def __str__(self):
        return self.nome


class Propriedade(models.Model):
    descricao = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    local = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name_plural = 'Propriedades'

    def __str__(self):
        return self.descricao


class ProdutorRural(models.Model):
    nome = models.CharField(max_length=200)
    propriedade = models.ForeignKey('Propriedade', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Produtores Rurais'


class Diagnostico(models.Model):
    cultura = models.CharField(max_length=100)
    produto_comercial = models.CharField(max_length=100)
    alvo = models.CharField(max_length=100)
    area_a_tratar = models.CharField(max_length=30)
    volume_da_calda = models.CharField(max_length=50)
    intervalo_de_seguranca = models.CharField(max_length=50)
    modalidade_aplicacao = models.CharField(max_length=100)
    equipamento_aplicacao = models.CharField(max_length=100)
    quantidade_a_adquirir = models.IntegerField()
    n_aplicacoes = models.IntegerField()
    epoca_aplicacao = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Diagnosticos'


class PrecaucaoUso(models.Model):
    texto = models.TextField()

    class Meta:
        verbose_name_plural = 'Precaucoes de Uso'


class equipamentos_protecao(models.Model):
    texto_equip = models.TextField()

    class Meta:
        verbose_name_plural = 'Equipamentos de Protecao Individual'


class orientacao_mip(models.Model):
    texto_mip = models.TextField()

    class Meta:
        verbose_name_plural = 'Orientacoes MIP'


class local_devolucao(models.Model):
    texto_dev = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Locais de Devolucao'


class Precaucao_e_orientacao(models.Model):
    texto = models.TextField()

    class Meta:
        verbose_name_plural = 'Precaucoes e Orientacoes'
