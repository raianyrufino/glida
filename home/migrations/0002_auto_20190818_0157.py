# Generated by Django 2.2.4 on 2019-08-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
