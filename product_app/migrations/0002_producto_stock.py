# Generated by Django 3.1 on 2020-09-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock'),
        ),
    ]
