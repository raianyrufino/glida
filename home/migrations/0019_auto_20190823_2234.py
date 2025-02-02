# Generated by Django 2.2.4 on 2019-08-23 22:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_artigo_tema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.AlterField(
            model_name='visualizacao',
            name='artigo',
            field=models.ForeignKey(default=5, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Artigo'),
        ),
    ]
