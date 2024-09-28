# Generated by Django 4.2 on 2024-09-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreDepartamento', models.CharField(max_length=50, verbose_name='NombreDepartamento')),
                ('CodigoDepartamento', models.CharField(max_length=50, verbose_name='CodigoDepartamento')),
            ],
            options={
                'verbose_name_plural': 'Departamento',
            },
        ),
    ]