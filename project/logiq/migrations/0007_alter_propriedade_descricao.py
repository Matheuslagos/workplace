# Generated by Django 4.1.7 on 2023-05-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logiq', '0006_alter_propriedade_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]
