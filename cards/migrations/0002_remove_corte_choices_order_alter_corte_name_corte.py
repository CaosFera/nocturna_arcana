# Generated by Django 5.0.3 on 2024-05-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corte',
            name='choices_order',
        ),
        migrations.AlterField(
            model_name='corte',
            name='name_corte',
            field=models.CharField(choices=[('Pajem de Paus', 'Pajem de Paus'), ('Cavaleiro de Paus', 'Cavaleiro de Paus'), ('Rainha de Paus', 'Rainha de Paus'), ('Rei de Paus', 'Rei de Paus'), ('Pajem de Copas', 'Pajem de Copas'), ('Cavaleiro de Copas', 'Cavaleiro de Copas'), ('Rainha de Copas', 'Rainha de Copas'), ('Rei de Copas', 'Rei de Copas'), ('Pajem de Espadas', 'Pajem de Espadas'), ('Cavaleiro de Espadas', 'Cavaleiro de Espadas'), ('Rainha de Espadas', 'Rainha de Espadas'), ('Rei de Espadas', 'Rei de Espadas'), ('Pajem de Ouros', 'Pajem de Ouros'), ('Cavaleiro de Ouros', 'Cavaleiro de Ouros'), ('Rainha de Ouros', 'Rainha de Ouros'), ('Rei de Ouros', 'Rei de Ouros')], max_length=20, unique=True, verbose_name='Nome'),
        ),
    ]