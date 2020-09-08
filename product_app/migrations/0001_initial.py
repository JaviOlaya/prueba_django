# Generated by Django 3.1 on 2020-09-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('marca', models.CharField(max_length=50, verbose_name='marca')),
                ('color', models.CharField(choices=[('0', 'BLACK'), ('1', 'BROWN'), ('2', 'BLUE'), ('3', 'GREEN'), ('4', 'ORANGE'), ('5', 'GOLD'), ('6', 'SILVER')], max_length=50, verbose_name='color')),
                ('talla', models.CharField(choices=[('0', '31'), ('1', '32'), ('2', '33'), ('3', '34'), ('4', '35'), ('5', '36'), ('6', '37'), ('7', '38'), ('8', '39'), ('9', '40'), ('10', '41'), ('11', '42'), ('12', '43'), ('13', '44'), ('14', '45')], max_length=50, verbose_name='talla')),
                ('precio', models.IntegerField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='producto', verbose_name='foto')),
            ],
            options={
                'ordering': ['marca'],
            },
        ),
    ]