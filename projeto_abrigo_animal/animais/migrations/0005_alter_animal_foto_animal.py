# Generated by Django 4.2.5 on 2024-10-25 13:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0004_alter_animal_foto_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto_animal',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='media/images'), upload_to='images/'),
        ),
    ]
