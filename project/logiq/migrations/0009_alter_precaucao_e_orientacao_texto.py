# Generated by Django 4.1.7 on 2023-05-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logiq', '0008_alter_responsavel_tecnico_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precaucao_e_orientacao',
            name='texto',
            field=models.CharField(max_length=2000),
        ),
    ]
