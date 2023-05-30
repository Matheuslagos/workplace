from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Responsavel_Tecnico)
class Responsavel_TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CNPJ', 'Num_Registro')
# admin.site.register(Responsavel_Tecnico)


@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('nomefazenda', 'descricao', 'cnpj',
                    'local', 'latitude', 'longitude')


@admin.register(ProdutorRural)
class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('nome', 'propriedade')


@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('cultura', 'produto_comercial', 'alvo', 'area_a_tratar', 'volume_da_calda', 'intervalo_de_seguranca',
                    'modalidade_aplicacao', 'equipamento_aplicacao', 'quantidade_a_adquirir', 'n_aplicacoes', 'epoca_aplicacao')


# @admin.register(PrecaucaoUso)
# class PrecaucaoUsoAdmin(admin.ModelAdmin):
 #   list_display = ('texto',)


# @admin.register(equipamentos_protecao)
# class equipamentos_protecaoAdmin(admin.ModelAdmin):
 #   list_display = ('texto_equip',)


# @admin.register(orientacao_mip)
# class orientacao_mipAdmin(admin.ModelAdmin):
 #   list_display = ('texto_mip',)


# @admin.register(local_devolucao)
# class local_devolucaoAdmin(admin.ModelAdmin):
 #   list_display = ('texto_dev',)


# @admin.register(Precaucao_e_orientacao)
# class Precaucao_e_orientacaoAdmin(admin.ModelAdmin):
 #   list_display = ('texto',)
