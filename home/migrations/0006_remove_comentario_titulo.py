# Generated by Django 2.2.4 on 2019-08-18 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190818_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='titulo',
        ),
    ]
