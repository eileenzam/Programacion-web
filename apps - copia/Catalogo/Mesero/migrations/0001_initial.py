# Generated by Django 4.2 on 2024-09-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreMesero', models.CharField(max_length=50)),
                ('NumeroMesero', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Hora', models.TimeField()),
            ],
        ),
    ]
