# Generated by Django 2.2.2 on 2019-06-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquiagem',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Foto'),
        ),
    ]
