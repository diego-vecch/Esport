# Generated by Django 4.0.5 on 2022-08-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_rename_productos_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
