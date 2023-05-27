from django.contrib import admin
from .models import respons_tec
# Register your models here.


@admin.register(respons_tec)
class respons_tecAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CNPJ', 'Num_Registro')
