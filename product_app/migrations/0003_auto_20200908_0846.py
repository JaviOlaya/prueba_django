# Generated by Django 3.1 on 2020-09-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_producto_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripcion producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='man',
            field=models.BooleanField(default=True, verbose_name='Para Hombre'),
        ),
        migrations.AddField(
            model_name='producto',
            name='woman',
            field=models.BooleanField(default=True, verbose_name='Para Mujer'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Venta'),
        ),
    ]
