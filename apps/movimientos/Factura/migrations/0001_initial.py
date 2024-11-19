# Generated by Django 4.2 on 2024-11-13 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MetodoPago', '0001_initial'),
        ('Menus', '0001_initial'),
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=20, unique=True)),
                ('propina_general', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('descuento_general', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('numero_mesa', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cliente_principal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='facturas', to='Cliente.cliente')),
            ],
            options={
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_pagado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='Cliente.cliente')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='Factura.factura')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MetodoPago.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, editable=False, max_digits=8)),
                ('subtotal', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('propina_individual', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='Cliente.cliente')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='Factura.factura')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.menu')),
            ],
            options={
                'verbose_name_plural': 'Detalles de Facturas',
            },
        ),
    ]
