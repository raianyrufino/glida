# Generated by Django 2.2.4 on 2019-08-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_contato_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sugestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=180, verbose_name='Informe seu nome')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('assunto', models.CharField(choices=[('ideia', 'Ideia'), ('duvida', 'Dúvida'), ('problema', 'Problema'), ('bug', 'Bug'), ('outro', 'Outro')], default='outro', max_length=80, verbose_name='Escolha um assunto')),
                ('mensagem', models.TextField(max_length=255, verbose_name='Mensagem')),
                ('visto', models.BooleanField(default=False)),
            ],
        ),
    ]
