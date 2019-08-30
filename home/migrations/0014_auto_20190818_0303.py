# Generated by Django 2.2.4 on 2019-08-18 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190818_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='redator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Redator'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='artigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Artigo'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='leitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Redator'),
        ),
        migrations.AlterField(
            model_name='visualizacao',
            name='artigo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Artigo'),
        ),
    ]
