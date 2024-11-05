# Generated by Django 4.2.16 on 2024-11-05 16:14

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0006_alter_animal_foto_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='porte',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='raca',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='tipo',
        ),
        migrations.AddField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='fotos_gatos/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='idade',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')], default='Macho', max_length=10),
        ),
        migrations.AlterField(
            model_name='animal',
            name='status',
            field=models.CharField(choices=[('Disponível', 'disponivel'), ('Adotado', 'adotado')], default='Disponível', max_length=10),
        ),
    ]
