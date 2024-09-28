# Generated by Django 4.2 on 2024-09-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=6, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=6, verbose_name='Apellido')),
                ('Telefono', models.CharField(max_length=6, verbose_name='Telefono')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
    ]