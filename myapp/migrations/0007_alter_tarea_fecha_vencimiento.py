# Generated by Django 4.2.2 on 2023-07-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_tarea_idtarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_vencimiento',
            field=models.DateField(),
        ),
    ]
